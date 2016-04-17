import {Component, Input} from 'angular2/core'
import {Task} from './task.model'
import {TaskService} from './task.service'

@Component({
    selector: 'app-task-detail',
    template: `
        <div *ngIf="task">
            <h2>{{task.title}}</h2>
            <div><label>id: </label>{{task.id}}</div>
            <div>
                <label>title: </label>
                <input [(ngModel)]="task.title" placeholder="title" />
            </div>
            <div>
                <label>detail: </label>
                <input [(ngModel)]="task.detail" placeholder="detail" />
            </div>
            <div><label>done: </label>{{task.done}}</div>
            <button (click)="updateTask(task)">Update Task</button>
            
            <div class="error" *ngIf="errorMessage">{{errorMessage}}</div>
        </div>
    `,
})
export class TaskDetailComponent {
    @Input() task: Task;
    errorMessage: string;

    constructor(
        private _taskService: TaskService
    ) {}

    updateTask(task: Task) {
        this._taskService.updateTask(task)
            .subscribe(
                task => this.task = task,
                error => this.errorMessage = <any>error
            );
    }
}
