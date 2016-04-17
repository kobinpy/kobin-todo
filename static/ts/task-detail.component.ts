import {Component, Input} from 'angular2/core'
import {Task} from './task.model'
import {TaskService} from './task.service'

@Component({
    selector: 'app-task-detail',
    template: `
        <div *ngIf="task">
            <div class="form-group">
                <label>title: </label>
                <input [(ngModel)]="task.title" placeholder="title" class="form-control"  />
            </div>
            <div class="form-group">
                <label>detail: </label>
                <textarea [(ngModel)]="task.detail" placeholder="detail" class="form-control" rows="8" ></textarea>
            </div>
            <div class="form-group">
                <input type="checkbox" [(ngModel)]="task.done" />
                This task is done.
            </div>
            <button class="btn btn-default" (click)="updateTask(task)">Update Task</button>
            
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
