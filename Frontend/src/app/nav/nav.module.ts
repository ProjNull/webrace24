import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavRootComponent } from './nav-root/nav-root.component';
import { NavLinkComponent } from './nav-link/nav-link.component';
import { RouterLink } from '@angular/router';



@NgModule({
  declarations: [
    NavRootComponent,
    NavLinkComponent
  ],
  imports: [
    CommonModule,
    RouterLink
  ],
  exports: [
    NavRootComponent,
    NavLinkComponent
  ]
})
export class NavModule { }
