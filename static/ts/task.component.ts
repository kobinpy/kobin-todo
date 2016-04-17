import {Component, OnInit} from 'angular2/core'
import {HTTP_PROVIDERS} from 'angular2/http'

import {Task} from './task'
import {TaskService} from './task.service'
import {TaskDetailComponent} from "./task-detail.component";

@Component({
    selector: 'app-task',
    template: `
        <h1>Todo App</h1>
        
        New Task:
        <input #newTask />
        <button (click)="addTask(newTask.value); newTask.value=''">Add Task</button>
        
        <div class="error" *ngIf="errorMessage">{{errorMessage}}</div>
        
        <ul>
            <li [class.selected]="task === selectedTask" *ngFor="#task of tasks" (click)="onSelect(task)">
                {{task.id}} {{task.title}}
            </li>
        </ul>
        <app-task-detail [task]="selectedTask"></app-task-detail>
    `,
    styles: [
        `.selected { background-color: #ddd; }`
    ],
    providers: [
        HTTP_PROVIDERS,
        TaskService,
    ],
    directives: [TaskDetailComponent],
})
export class TaskComponent implements OnInit {
    tasks: Task[];
    errorMessage: string;
    selectedTask: Task;
    
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
    
    onSelect(task: Task) {
        this.selectedTask = task;
    }
}
