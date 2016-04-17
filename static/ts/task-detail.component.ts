import {Component, Input} from 'angular2/core'
import {Task} from './task'

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
        </div>
    `,
})
export class TaskDetailComponent {
    @Input() task: Task
}
