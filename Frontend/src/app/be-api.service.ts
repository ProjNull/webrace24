import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BeForm } from '../be';

@Injectable({
  providedIn: 'root'
})
export class BeApiService {

  private baseUrl = 'http://localhost:3000';

  constructor(private http: HttpClient) { }

  senfForm(data: BeForm) {
    return this.http.post(this.baseUrl+'/form', data);
  }
}
