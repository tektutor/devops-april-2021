#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def sayHello(name):
   return "Hello " + name + " !"

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str')
        )
    )

    name = module.params['name']

    result = sayHello( name )

    module.exit_json(output = result, changed=False)
    #module.fail_json(msg = "##### Something bad happened #####", changed=False)

main()
