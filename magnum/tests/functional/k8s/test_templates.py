# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from magnum.drivers.common import template_def as tdef
from magnum.tests import base


class TestTemplates(base.TestCase):
    def test_templates_list(self):
        entry_points = list(tdef.TemplateDefinition.load_entry_points())
        self.assertEqual(5, len(entry_points))

        templates = []
        for entry_point, def_class in entry_points:
            templates.append(def_class.__name__)

        self.assertEqual(['AtomicK8sTemplateDefinition',
                          'AtomicSwarmTemplateDefinition',
                          'CoreOSK8sTemplateDefinition',
                          'FedoraK8sIronicTemplateDefinition',
                          'UbuntuMesosTemplateDefinition'],
                         sorted(templates))
