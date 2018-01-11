
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


import os
import sys

from core.models import Slice,Instance,User,Flavor,Node,Image

class XOSFlavorSelector(object):
    def __init__(self, user, mem_size=None, num_cpus=None, disk_size=None):
        self.user = user
        self.mem_size = self.get_mb(mem_size)
        self.num_cpus = int(num_cpus)
        self.disk_size = self.get_gb(disk_size)

    def get_gb(self, s):
        if "GB" in s:
            return int(s.split("GB")[0].strip())
        if "MB" in s:
            return int(s.split("MB")[0].strip())/1024
        return int(s)

    def get_mb(self, s):
        if "GB" in s:
            return int(s.split("GB")[0].strip())*1024
        if "MB" in s:
            return int(s.split("MB")[0].strip())
        return int(s)

    def get_flavor(self):
        flavor = "m1.tiny"
        if (self.mem_size>512) or (self.disk_size>1):
            flavor = "m1.small"
        if (self.mem_size>2048) or (self.disk_size>20) or (self.num_cpus>1):
            flavor = "m1.medium"
        if (self.mem_size>4096) or (self.disk_size>40) or (self.num_cpus>2):
            flavor = "m1.large"
        if (self.mem_size>8192) or (self.disk_size>80) or (self.num_cpus>4):
            flavor = "m1.xlarge"

        return Flavor.objects.get(name=flavor)

