import {Component, OnInit} from 'angular2/core'
import {HTTP_PROVIDERS} from 'angular2/http'

import {Task} from './task'
import {TaskService} from './tasks.service'

@Component({
    selector: 'app-task',
    template: `
        <h1>Todo App</h1>
        
        New Task:
        <input #newTask />
        <button (click)="addTask(newTask.value); newTask.value=''">Add Task</button>
        
        <div class="error" *ngIf="errorMessage">{{errorMessage}}</div>
        
        <ul>
            <li *ngFor="#task of tasks">{{task.id}} {{task.title}}</li>
        </ul>
    `,
    providers: [
        HTTP_PROVIDERS,
        TaskService,
    ]
})
export class TaskComponent implements OnInit {
    tasks: Task[];
    errorMessage: string;
    
    constructor(
        private _taskService: TaskService
    ) {}
    
    getTasks() {
        this._taskService.getTasks()
            .subscribe(
                tasks => this.tasks = tasks,
                error => this.errorMessage = <any>error
            );
    }

    addTask(title: string) {
        if (!title) {
            return;
        }
        this._taskService.addTask(title)
            .subscribe(
                task => this.tasks.push(task),
                error => this.errorMessage = <any>error
            );
    }
    
    ngOnInit() {
        this.getTasks();
    }
}
