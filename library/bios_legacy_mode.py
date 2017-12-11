#!/usr/bin/python

# Copyright 2016 Hewlett Packard Enterprise Development, LP.
#
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
 
 
DOCUMENTATION = '''
---
module: bios_legacy_mode
short_description: This module reverts the bios to default settings
'''

EXAMPLES = '''
- name: Bios revert Default
  bios_legacy_mode:
    ilo_https_url: "https://{{ ilo_ip }}"
'''

import sys
from ansible.module_utils._restobject import RestObject

def bios_legacy_mode(restobj):
    instances = restobj.search_for_type("Bios.")

    for instance in instances:
        body = {"BootMode": "LegacyBios"}
        response = restobj.rest_put(instance["href"], body)
        restobj.error_handler(response)

#Instantiating module class        
from ansible.module_utils.basic import *
    
def main():
    module = AnsibleModule(
        argument_spec = dict(
            state     = dict(default='present', choices=['present', 'absent']),
            ilo_https_url    = dict(required=True, type='str'),
            ilo_pass  = dict(required=True, type='str'),
            ilo_user  = dict(required=True, type='str')
        )
    )

    # When running on the server locally use the following commented values
    # While this example can be run remotely, it is used locally to locate the
    # iLO IP address
    iLO_https_url = module.params['ilo_https_url']
    iLO_account = module.params['ilo_user']
    iLO_password = module.params['ilo_pass']

    #Create a REST object
    try:
        REST_OBJ = RestObject(iLO_https_url, iLO_account, iLO_password)
    except excp:
        sys.stderr.write("ERROR: server not reachable or doesn't support " \
                                                                "RedFish.\n")
        sys.exit()
    except Exception, excp:
        raise excp
    bios_legacy_mode(REST_OBJ)
    module.exit_json(changed=True)

if __name__ == "__main__":
    main()
