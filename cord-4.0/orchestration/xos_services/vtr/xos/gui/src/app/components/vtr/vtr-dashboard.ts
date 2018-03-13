
/*
 * Copyright 2017-present Open Networking Foundation

 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at

 * http://www.apache.org/licenses/LICENSE-2.0

 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


import * as _ from 'lodash';
import {subscribeOn} from 'rxjs/operator/subscribeOn';

class VtrDashboardComponent {
  static $inject = [
    '$timeout',
    'XosModelStore',
    'XosVtrTruckroll'
   ];

  public subscribers = [];
  public truckroll: any;
  public loader: boolean;
  public error: string;

  private services = [];
  private Truckroll;

  constructor(
    private $timeout: ng.ITimeoutService,
    private XosModelStore: any,
    private XosVtrTruckroll: any
  ) {

    this.Truckroll = this.XosVtrTruckroll.getResource();

    // load subscribers
    this.XosModelStore.query('CordSubscriberRoot', '/volt/cordsubscriberroots')
      .subscribe(
        res => {
          this.subscribers = res;
        }
      );

    this.XosModelStore.query('VTRService')
      .subscribe(
        res => {
          this.services = res;
        }
      );
  }

  public runTest() {

    // clean previous tests
    delete this.truckroll.id;
    delete this.truckroll.result;
    delete this.truckroll.is_synced;
    delete this.truckroll.result_code;
    delete this.truckroll.backend_status;
    delete this.error;

    this.truckroll.target_type = this.getSubscriberContentTypeId(this.truckroll.target_id);
    this.truckroll.owner_id = this.getServiceInstanceOwnerId();

    console.log(this.truckroll);

    const test = new this.Truckroll(this.truckroll);
    this.loader = true;
    test.$save()
    .then((res) => {
      this.waitForTest(res.id);
    });
  };

  private getSubscriberContentTypeId(subscriberId: number) {
    return _.find(this.subscribers, {id: subscriberId}).self_content_type_id;
  }

  private getServiceInstanceOwnerId(): number {
    return this.services[0].id;
  }

  private waitForTest(id: number) {

        this.Truckroll.get({id: id}).$promise
        .then((testResult, status) => {
          // this is becasue error returning a string in an array
          if (testResult[0] && testResult[0].length === 1) {
            this.loader = false;
            this.error = 'An error occurred, please try again later';
            return;
          }

          // if error
          // or
          // if is synced
          if (
              testResult.backend_code == 2 ||
              testResult.backend_code == 1 ||
              angular.isDefined(testResult.result) ||
              testResult.is_synced
            ) {
            this.truckroll = angular.copy(testResult);
            this.loader = false;
            this.Truckroll.delete({id: id});
          }
          // else keep polling
          else {
            this.$timeout(() => {
              this.waitForTest(id);
            }, 2000);
          }
        });
      };

}

export const xosVtrDashboardComponent: angular.IComponentOptions = {
  template: require('./vtr-dashboard.html'),
  controllerAs: 'vm',
  controller: VtrDashboardComponent
};
