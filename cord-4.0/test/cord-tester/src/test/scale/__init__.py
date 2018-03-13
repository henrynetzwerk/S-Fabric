
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
import os,sys
##add the python path to lookup the utils
working_dir = os.path.dirname(os.path.realpath(sys.argv[-1]))
utils_dir = os.path.join(working_dir, '../utils')
fsm_dir = os.path.join(working_dir, '../fsm')
subscriber_dir = os.path.join(working_dir, '../subscriber')
tls_dir = os.path.join(working_dir, '../tls')
vrouter_dir = os.path.join(working_dir, '../vrouter')
vsg_dir = os.path.join(working_dir, '../vsg')
__path__.append(utils_dir)
__path__.append(fsm_dir)
__path__.append(subscriber_dir)
cli_dir = os.path.join(working_dir, '../cli')
__path__.append(cli_dir)
__path__.append(tls_dir)
__path__.append(vrouter_dir)
__path__.append(vsg_dir)
