import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BeForm } from '../be';

@Injectable({
  providedIn: 'root'
})
export class BeApiService {

  private baseUrl = 'https://webrace2024.onrender.com/';

  constructor(private http: HttpClient) { }

  sendForm(data: BeForm) {
    return this.http.post(this.baseUrl+'/form/send', data);
  }
}
