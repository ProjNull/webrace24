import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NavModule } from './nav/nav.module';
import { HeroComponent } from './hero/hero.component';
import { SectionComponent } from './section/section.component';
import { AplicationFormComponent } from './aplication-form/aplication-form.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [NavModule, HeroComponent, SectionComponent, AplicationFormComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Frontend';
}
