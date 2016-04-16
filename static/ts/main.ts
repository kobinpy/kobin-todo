import "es6-shim";
import "reflect-metadata";
import "rxjs/Rx";
import "zone.js/dist/zone";

import {bootstrap} from "angular2/platform/browser";
import {Component} from "angular2/core";

@Component({
    selector: 'my-app',
    template: `<h1>My First Angular 2 App</h1>`
})
class AppComponent { }

bootstrap(AppComponent);
