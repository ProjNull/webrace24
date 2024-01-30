import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BeForm } from '../be';

@Injectable({
  providedIn: 'root'
})
export class BeApiService {

  private baseUrl = 'http://192.168.0.1:8000';

  constructor(private http: HttpClient) { }

  senfForm(data: BeForm) {
    return this.http.post(this.baseUrl+'/form/send', data);
  }
}
