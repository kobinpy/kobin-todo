import {Component, OnInit} from 'angular2/core'
import {HTTP_PROVIDERS} from 'angular2/http'

import {Task} from './task'
import {TaskService} from './tasks.service'

@Component({
    selector: 'app-task',
    template: `
        <h1>Todo App</h1>
        <p>{{errorMessage}}</p>
        <ul>
            <li *ngFor="#task of tasks">{{task.id}} {{task.message}}</li>
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
        console.log(this.tasks);
    }
    
    ngOnInit() {
        this.getTasks();
    }
}
