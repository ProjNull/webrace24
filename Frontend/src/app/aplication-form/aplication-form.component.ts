import { Component, forwardRef } from '@angular/core';
import { FormControl, FormGroup, NG_VALUE_ACCESSOR, ReactiveFormsModule } from '@angular/forms';
import { BeForm, BeFormUnverified } from '../../be';
import { BeApiService } from '../be-api.service';

@Component({
  selector: 'app-aplication-form',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './aplication-form.component.html',
  styleUrl: './aplication-form.component.css',
  providers: [
    {
      provide: NG_VALUE_ACCESSOR,
      useExisting: forwardRef(() => Selection),
      multi: true,
    }
  ]
})
export class AplicationFormComponent {
  validate = false;
  rawData: BeFormUnverified = {
    firstName: new FormControl(''),
    lastName: new FormControl(''),
    email: new FormControl(''),
    phone: new FormControl(''),
    githubUrl: new FormControl(''),
    preferences: new FormControl('Fullstack'),
    massage: new FormControl(''),
    
  }

  constructor(private api: BeApiService) { }

  onSubmit($event: Event) {
    $event.preventDefault();
    this.validate = true;
    if (this.rawData.firstName.value === '') {
      return;
    }
    if (this.rawData.lastName.value === '') {
      alert('Please enter your last name');
      return;
    }
    if (this.rawData.email.value === '') {
      alert('Please enter your email');
      return;
    }
    if (this.rawData.phone.value === '') {
      alert('Please enter your phone');
      return;
    }
    if (this.rawData.githubUrl.value === '') {
      alert('Please enter your githubUrl');
      return;
    }
    if (this.rawData.preferences.value === '') {
      alert('Please enter your preferences');
      return;
    }
    if (this.rawData.massage.value === '') {
      alert('Please enter your massage');
      return;
    }
    
    const data: BeForm = {
      firstName: this.rawData.firstName.value,
      lastName: this.rawData.lastName.value,
      email: this.rawData.email.value,
      phone: this.rawData.phone.value,
      githubUrl: this.rawData.githubUrl.value,
      preferences: this.rawData.preferences.value,
      massage: this.rawData.massage.value,
    }

    this.api.sendForm(data).subscribe((res) => {
    });

  }
}
