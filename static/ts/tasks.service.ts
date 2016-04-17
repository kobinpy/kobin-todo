import {Task} from './task'
import {Injectable} from 'angular2/core'
import {Http, Response} from 'angular2/http';
import {Observable} from "rxjs/Observable";

@Injectable()
export class TaskService{
    constructor(
        private http: Http
    ) { }
    
    private _tasksUrl = 'api/tasks';
    
    getTasks(): Observable<Task[]> {
        return this.http.get(this._tasksUrl)
            .map(this.extractData)
            .catch(this.handleError);
    }
    
    private extractData(res: Response) {
        if (res.status < 200 || res.status >= 300) {
            throw new Error('Bad response status: ' + res.status);
        }
        let body = res.json();
        return body.tasks || {};
    }
    
    private handleError(error: any) {
        let errMsg = error.message || 'Server error';
        console.error(errMsg);
        return Observable.throw(errMsg);
    }
}
