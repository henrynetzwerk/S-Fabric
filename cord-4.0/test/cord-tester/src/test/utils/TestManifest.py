
# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


#
# Copyright 2016-present Ciena Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import json
import os
import shutil
import platform
from CordTestServer import CORD_TEST_HOST, CORD_TEST_PORT

class TestManifest(object):

    def __init__(self, manifest = None, args = None):
        self.manifest = manifest
        if args is not None and manifest is None:
            self.onos_ip = None
            self.radius_ip = None
            self.head_node = platform.node()
            self.log_level = args.log_level.upper()
            self.onos_instances = args.onos_instances
            self.async_mode = args.async_mode
            self.shared_volume = args.shared_volume
            self.olt = args.olt
            self.olt_config = args.olt_config
            self.start_switch = args.start_switch
            self.image_prefix = args.prefix
            self.onos_image = args.onos
            self.test_controller = args.test_controller
            if self.test_controller:
                ips = self.test_controller.split('/')
                self.onos_ip = ips[0]
                if len(ips) > 1:
                    self.radius_ip = ips[1]
            self.onos_cord = args.onos_cord if args.onos_cord else None
            self.service_profile = args.service_profile if args.service_profile else None
            self.synchronizer = args.synchronizer if args.synchronizer else None
            self.docker_network = args.network if args.network else None
            self.iterations = None
            self.server = args.server
            self.jvm_heap_size = args.jvm_heap_size if args.jvm_heap_size else None
            self.karaf_version = args.karaf
            self.voltha_loc = args.voltha_loc
            self.voltha_intf = args.voltha_intf
            self.voltha_enable = args.voltha_enable
            self.voltha_container_mode = args.voltha_container_mode
            self.expose_port = args.expose_port
        else:
            with open(self.manifest, 'r') as fd:
                data = json.load(fd)
            self.onos_ip = data.get('onos', None)
            self.radius_ip = data.get('radius', None)
            self.test_controller = '' if self.onos_ip is None else self.onos_ip
            if self.onos_ip and self.radius_ip:
                self.test_controller = '{}/{}'.format(self.onos_ip, self.radius_ip)
            self.onos_cord = data.get('onos_cord', None)
            self.service_profile = data.get('service_profile', None)
            self.synchronizer = data.get('synchronizer', None)
            self.head_node = data.get('head_node', platform.node())
            self.log_level = data.get('log_level', 'INFO').upper()
            self.onos_instances = data.get('onos_instances', 1)
            self.shared_volume = data.get('shared_volume', True)
            self.async_mode = True if self.onos_instances > 1 else False
            self.olt = data.get('olt', True)
            self.olt_config = data.get('olt_config', 'olt_config.json')
            self.start_switch = data.get('start_switch', self.olt)
            self.image_prefix = data.get('image_prefix', '')
            self.onos_image = data.get('onos_image', 'onosproject/onos:latest')
            self.docker_network = data.get('docker_network', None)
            self.server = data.get('test_server', '{}:{}'.format(CORD_TEST_HOST, CORD_TEST_PORT))
            self.iterations = data.get('iterations', None)
            self.jvm_heap_size = data.get('jvm_heap_size', None)
            self.karaf_version = data.get('karaf_version', '3.0.8')
            self.voltha_loc = data.get('voltha_loc', '')
            self.voltha_intf = data.get('voltha_intf', 'eth0')
            voltha_enable = False
            if self.voltha_loc:
                voltha_enable = True
            self.voltha_enable = data.get('voltha_enable', voltha_enable)
            self.voltha_container_mode = data.get('voltha_container_mode', True)
            self.expose_port = data.get('expose_port', False)
            if self.voltha_enable and self.voltha_container_mode:
                self.expose_port = True
