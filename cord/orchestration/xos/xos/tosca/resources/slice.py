
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


from xosresource import XOSResource
from core.models import Slice,User,Site,Network,NetworkSlice,SliceRole,SlicePrivilege,Service,Image,Flavor,Node

class XOSSlice(XOSResource):
    provides = "tosca.nodes.Slice"
    xos_model = Slice
    copyin_props = ["enabled", "description", "slice_url", "max_instances", "default_isolation", "default_flavor", "network", "exposed_ports"]

    def get_xos_args(self):
        args = super(XOSSlice, self).get_xos_args()

        site_name = self.get_requirement("tosca.relationships.MemberOfSite", throw_exception=True)
        site = self.get_xos_object(Site, login_base=site_name)
        args["site"] = site

        serviceName = self.get_requirement("tosca.relationships.MemberOfService", throw_exception=False)
        if serviceName:
            service = self.get_xos_object(Service, name=serviceName)
            args["service"] = service

        default_image_name = self.get_requirement("tosca.relationships.DefaultImage", throw_exception=False)
        if default_image_name:
            default_image = self.get_xos_object(Image, name=default_image_name, throw_exception=True)
            args["default_image"] = default_image

        default_flavor_name = self.get_requirement("tosca.relationships.DefaultFlavor", throw_exception=False)
        if default_flavor_name:
            default_flavor = self.get_xos_object(Flavor, name=default_flavor_name, throw_exception=True)
            args["default_flavor"] = default_flavor

        default_node_name = self.get_property_default("default_node", None)
        if default_node_name:
            default_node = self.get_xos_object(Node, name=default_node_name, throw_exception=True)
            args["default_node"] = default_node

        return args

    def postprocess(self, obj):
        for net_name in self.get_requirements("tosca.relationships.ConnectsToNetwork"):
            net = self.get_xos_object(Network, name=net_name)
            if not NetworkSlice.objects.filter(network=net, slice=obj):
                ns = NetworkSlice(network=net, slice=obj)
                ns.save()
                self.info("Added network connection from '%s' to '%s'" % (str(obj), str(net)))

        rolemap = ( ("tosca.relationships.AdminPrivilege", "admin"), ("tosca.relationships.AccessPrivilege", "access"),
                    ("tosca.relationships.PIPrivilege", "pi"), ("tosca.relationships.TechPrivilege", "tech") )
        self.postprocess_privileges(SliceRole, 'Slice', rolemap, obj)

    def delete(self, obj):
        if obj.instances.exists():
            self.info("Slice %s has active instances; skipping delete" % obj.name)
            return
        super(XOSSlice, self).delete(obj)



