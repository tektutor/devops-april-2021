#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import os

def extractIPAddress():
   stream = os.popen('hostname -i')
   ip = stream.read()
   return ip

def main():
    module = AnsibleModule(
        argument_spec=dict()
    )

    ipAddress = extractIPAddress( )

    module.exit_json(ip_address = ipAddress, changed=False)
    #module.fail_json(msg = "##### Something bad happened #####", changed=False)

main()
