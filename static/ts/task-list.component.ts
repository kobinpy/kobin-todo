import {Component, OnInit} from 'angular2/core';

import {Task} from './task.model'
import {TaskService} from "./task.service";
import {TaskDetailComponent} from './task-detail.component'

@Component({
    selector: 'app-task-list',
    template: `
        <header>
            <img class="logo" src="/static/img/kobin.png">
            <div class="task-add form-inline">
                <div class="form-group">
                    <input #newTask class="form-control" />
                </div>
                <button class="btn btn-default" (click)="addTask(newTask.value); newTask.value=''">ADD</button>
            </div>
            
            <div class="alert alert-danger" role="alert" *ngIf="errorMessage">
                <span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
                <span class="sr-only">Error: </span>
                {{errorMessage}}
            </div>
            
            <div class="task-titles">
                <ul>
                    <li [class.selected]="task === selectedTask" *ngFor="#task of tasks" (click)="onSelect(task)">
                        <input type="checkbox" (click)="toggleDone(task)" [checked]="task.done"> {{task.title}}
                    </li>
                </ul>
            </div>
            <div class="bottom">
                <a href="https://github.com/login/oauth/authorize?client_id=9fbe39b8584d366afd85">Github Auth</a>
                <p>Progress: {{ doneTaskLength() }} / {{ tasks.length }}</p>
                <p>Powered by Kobin</p>
            </div>
        </header>
        
        <main>
            <app-task-detail [task]="selectedTask" [tasks]="tasks"></app-task-detail>
        </main>
    `,
    providers: [TaskService],
    directives: [TaskDetailComponent],
    styles: [`
        li { list-style: none; padding: 10px 0 10px 20px; }
        ul { padding-left: 0px; }
        .selected { background-color: #2980b9; }
        .task-add { padding: 10px 10px 10px 20px; }
    `],
})
export class TaskListComponent implements OnInit {
    tasks: Task[] = [];
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
                task => {
                    this.tasks.push(task);
                    this.selectedTask = task;
                },
                error => this.errorMessage = <any>error
            );
    }
    
    doneTaskLength() {
        return this.tasks
            .filter(task => task.done)
            .length
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
