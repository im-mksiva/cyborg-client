# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from cyborg.accelerator.drivers.nic.base import NICDriver
from cyborg.accelerator.drivers.nic.intel.driver import IntelNICDriver  # noqa

from cyborg.tests import base


class TestNICDriver(base.TestCase):
    def test_create(self):
        NICDriver.create("intel")
        self.assertRaises(LookupError, NICDriver.create, "other")

    def test_discover(self):
        d = NICDriver()
        self.assertRaises(NotImplementedError, d.discover)

    def test_discover_vendors(self):
        d = NICDriver()
        self.assertRaises(NotImplementedError, d.discover_vendors)
