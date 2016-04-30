import {Task} from './task.model'
import {Injectable} from 'angular2/core'
import {Http, Response, Headers, RequestOptions} from 'angular2/http';
import {Observable} from "rxjs/Observable";

@Injectable()
export class TaskService {
    constructor(
        private http: Http
    ) { }
    
    private _tasksUrl = 'api/tasks';
    private defaultRequestOptions: RequestOptions = new RequestOptions({
        headers: new Headers({ 'Content-Type': 'application/json' }),
    });

    getTasks(): Observable<Task[]> {
        return this.http.get(this._tasksUrl)
            .map(this.extractTasks)
            .catch(this.handleError);
    }

    addTask(title: string): Observable<Task> {
        let body = JSON.stringify({ title });
        return this.http.post(this._tasksUrl, body, this.defaultRequestOptions)
            .map(this.extractTask)
            .catch(this.handleError);
    }

    updateTask(task: Task): Observable<Task> {
        let body = JSON.stringify({ task });
        return this.http.patch(`api/tasks/${task.id}`, body, this.defaultRequestOptions)
            .map(this.extractTask)
            .catch(this.handleError)
    }

    deleteTask(task: Task): Observable<Response> {
        return this.http.delete(`api/tasks/${task.id}`, this.defaultRequestOptions)
            .map(res => res)
            .catch(this.handleError)
    }

    private extractTasks(res: Response) {
        if (res.status < 200 || res.status >= 300) {
            throw new Error('Bad response status: ' + res.status);
        }
        let body = res.json();
        return body.tasks || {};
    }
    
    private extractTask(res: Response) {
        if (res.status < 200 || res.status >= 300) {
            throw new Error('Bad response status: ' + res.status);
        }
        let body = res.json();
        return body || {};
    }

    private handleError(error: any) {
        let errMsg = error.message || 'Server error';
        console.error(errMsg);
        return Observable.throw(errMsg);
    }
}
