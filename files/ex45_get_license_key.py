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

import sys
from _restobject import RestObject

def ex45_get_license_key(restobj):
    sys.stdout.write("\nEXAMPLE 45: Get iLO License Key\n")
    instances = restobj.search_for_type("HpiLOLicense.")
    license_result = dict()
    licenseproperties = ["License", "LicenseKey", "LicenseType"]
    
    for instance in instances:
        response = restobj.rest_get(instance["href"])
        license_result["License"] = response.dict["License"]
        
        for licenseproperty in licenseproperties:
            sys.stdout.write("\t" + licenseproperty + ": " + \
                                  str(response.dict[licenseproperty]) + "\n")
    restobj.error_handler(response)
    return (license_result)

if __name__ == "__main__":
    # When running on the server locally use the following commented values
    # iLO_https_url = "blobstore://."
    # iLO_account = "None"
    # iLO_password = "None"

    # When running remotely connect using the iLO secured (https://) address, 
    # iLO account name, and password to send https requests
    # iLO_https_url acceptable examples:
    # "https://10.0.0.100"
    # "https://f250asha.americas.hpqcorp.net"
    try:
        iLO_https_url = "https://" + str(sys.argv[1])
        iLO_account = str(sys.argv[2])
        iLO_password = str(sys.argv[3])
    
        #Create a REST object
        REST_OBJ = RestObject(iLO_https_url, iLO_account, iLO_password)
		ex45_get_license_key(REST_OBJ)
		
    except Exception:
        sys.stderr.write("Credentials Error \n")
