import { Component } from '@angular/core';
import { AplicationFormComponent } from '../aplication-form/aplication-form.component';

@Component({
  selector: 'app-hero',
  standalone: true,
  imports: [AplicationFormComponent],
  templateUrl: './hero.component.html',
  styleUrl: './hero.component.css'
})
export class HeroComponent {

}
