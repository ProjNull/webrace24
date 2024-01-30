import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NavModule } from './nav/nav.module';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, NavModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Frontend';
}
