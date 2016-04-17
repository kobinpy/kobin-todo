import {Component} from 'angular2/core'
import {HTTP_PROVIDERS} from 'angular2/http'

import {TaskListComponent} from './task-list.component'

@Component({
    selector: 'app-task',
    template: `
        <app-task-list>Now loading...</app-task-list>
    `,
    providers: [HTTP_PROVIDERS],
    directives: [TaskListComponent]
})
export class TaskComponent {
}
