import { Routes } from '@angular/router';
import { PageHomeComponent } from './page-home/page-home.component';
import { PageAboutComponent } from './page-about/page-about.component';
import { PageFormComponent } from './page-form/page-form.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';

export const routes: Routes = [
    {path: '', component: PageHomeComponent},
    {path: 'about', component: PageAboutComponent},
    {path: 'form', component: PageFormComponent},
    {path: '**', component: PageNotFoundComponent},
];
