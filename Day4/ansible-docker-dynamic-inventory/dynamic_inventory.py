#!/usr/bin/python
#Author Jeganathan Swaminathan <jegan@tektutor.org> <http://www.tektutor.org>

import subprocess
import json
from os.path import expanduser

def executeDockerCommand(*args):
    return subprocess.check_output(["docker"] + list(args)).strip()

def docker_inspect(fmt, mcn):
    return executeDockerCommand("inspect", "-f", fmt, mcn)

def docker_port(machine):
    try:
       publishedPort = executeDockerCommand("port", machine, "22")
       tokens = publishedPort.split(':')
       return tokens[1]
    except:
       return "22"

def get_host_vars(m):
    home = expanduser("~")
    ip = [docker_inspect("{{.NetworkSettings.IPAddress}}", m)]

    publishedPort = docker_port(m)

    ssh_vars = {
        "ansible_port": publishedPort,
        "ansible_private_key_file": home+ "/.ssh/" + "id_rsa",
        "ansible_user": "devops",
        "ansible_become_user": "root",
        "ansible_become_password": "devops",
    }

    if ( publishedPort == "22" ):
        ssh_vars.update({"ansible_host": docker_inspect("{{.NetworkSettings.IPAddress}}", m) })
    else:
        ssh_vars.update({"ansible_host": "localhost"})

    hostConnectionDetails = {"hosts": ip, "vars": ssh_vars}
    return hostConnectionDetails

class DockerInventory():
      def __init__(self):
          self.inventory = {} # Ansible Inventory

          machines = executeDockerCommand("ps", "-q").splitlines()
          json_data = {m: get_host_vars(m) for m in machines}

          print json.dumps(json_data,indent=4,sort_keys=True)

DockerInventory()
