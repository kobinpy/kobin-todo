import {Component, OnInit} from 'angular2/core';

import {Task} from './task.model'
import {TaskService} from "./task.service";
import {TaskDetailComponent} from './task-detail.component'

@Component({
    selector: 'app-task-list',
    template: `
        <div class="task-add form-inline">
            <div class="form-group">
                <label>New Task: </label>
                <input #newTask class="form-control" />
            </div>
            <button class="btn btn-default" (click)="addTask(newTask.value); newTask.value=''">Add Task</button>
        </div>
        
        <div class="error" *ngIf="errorMessage">{{errorMessage}}</div>
        
        <div class="row">
            <div class="col-sm-4">
                <ul>
                    <li [class.selected]="task === selectedTask" *ngFor="#task of tasks" (click)="onSelect(task)">
                        <input type="checkbox" (click)="toggleDone(task)" [checked]="task.done"> {{task.title}}
                    </li>
                </ul>
            </div>
            <div class="col-sm-8">
                <app-task-detail [task]="selectedTask"></app-task-detail>
            </div>
        </div>
    `,
    providers: [TaskService],
    directives: [TaskDetailComponent],
    styles: [`
        li { list-style: none; padding: 10px 0; }
        ul { padding-left: 0px; }
        .selected { background-color: #ddd; }
        .task-add { padding: 10px 0; }
    `],
})
export class TaskListComponent implements OnInit {
    tasks: Task[];
    selectedTask: Task;
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

    toggleDone(task: Task) {
        task.done = !task.done;
        this._taskService.updateTask(task)
            .subscribe(
                task => {
                    this.tasks.filter(t => t.id === task.id)
                        .map(t => t.done = task.done)
                },
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
