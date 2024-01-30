import { TestBed } from '@angular/core/testing';

import { BeApiService } from './be-api.service';

describe('BeApiService', () => {
  let service: BeApiService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(BeApiService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
