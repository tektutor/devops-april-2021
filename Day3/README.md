Assumptions is you have logged in as root user in the terminal
```
sudo su -
```

### Building ubuntu ansible nod docker image
```
cd ubuntu-ansible-image
```
#### Generate ssh key pairs
```
ssh-keygen
```
You may accept all default values while generating key pairs.

Copy the public key generated in the previous step
```
cp /root/.ssh/id_rsa.pub authorized_keys
```

```
docker build -t tektutor/ansible-ubuntu .
```

Check if the newly built image is listed
```
docker images
```

### Creating containers using our new ubuntu ansible image
```
docker run -d --name ubuntu1 --hostname ubuntu1 -p 2001:22 tektutor/ansible-ubuntu
docker run -d --name ubuntu2 --hostname ubuntu2 -p 2002:22 tektutor/ansible-ubuntu
```

### Check if the ubuntu1 and ubuntu2 containers are running
```
docker ps
```

### Test if you can do ssh to those new containers
```
ssh -p 2001 root@localhost
```
You need type 'yes' when it prompts for "Are you sure you want to continue connecting (yes/no)?" question.

You may type exit to come of the ubuntu1 container.

```
ssh -p 2002 root@localhost
```
You need type 'yes' when it prompts for "Are you sure you want to continue connecting (yes/no)?" question.

You may type exit to come of the ubuntu2 container.


The expectation here is, ssh shouldn't prompt for password as we are using key-pair for login authentication.

### Inventory file (Filename - hosts)
```
cd ..
```
Assumption is, you are in Day3 folder.
You need to create a file called hosts and type below contents

```
[all]
ubuntu1 ansible_host=localhost ansible_port=2001 ansible_user=root ansible_private_key_file=/root/.ssh/id_rsa
ubuntu2 ansible_host=localhost ansible_port=2002 ansible_user=root ansible_private_key_file=/root/.ssh/id_rsa
```

### Running ansible adhoc command
```
ansible -i hosts all -m ping
ansible -i hosts ubuntu1 -m ping
ansible -i hosts ubuntu2 -m ping
ansible -i hosts all -m shell -a "hostname -i"
```

### Writing a simple ansible playbook

You need to create file called ping.yml. The name of the file is user-defined.

```
- name: Simple ping playbook
  hosts:  all
  tasks:
    - name: Ping the ansible node
      ping:
 ```
 
 You may now execute the ansible playbook as shown below
 ```
 ansible-playbook -i hosts ping.yml
 ```

### Writing a decent complex ansible playbook
Create a file named install-nginx.yml with the below code

```
- name: Install nginx in ansible nodes
  hosts: all
  tasks:
    - name: Install nginx
      apt: name=nginx state=latest update_cache=yes
      
 #  - name: Start nginx web server
 #    service: name=nginx state=started enabled=yes
 # service module has a bug related to service when ansible nodes are docker container, hence using shell module instead.
 
    - name: Start nginx web server
      shell:  service nginx start 
```

Execute the playbook with the below command
```
ansible-playbook -i hosts install-nginx.yml
```

You may test if you are able to access the web pages using the IP address of the containers
```
curl http://172.17.0.2:80
curl http://172.17.0.3
curl http://172.17.0.4
curl http://172.17.0.5
```
You may have to find the IP Addresses of your containers and modify the above IP Addresses accordingly.  In my case,
```
ubuntu1 container's IP is 172.17.0.2
ubuntu2 container's IP is 172.17.0.3
ubuntu3 container's IP is 172.17.0.4
ubuntu4 container's IP is 172.17.0.5
```

In case you forgot the command to. find IP address of docker containers, please check below
```
docker inspect ubuntu1 | grep IPA
docker inspect -f {{.NetworkSettings.IPAddress}} ubuntu1
```
You may use any one of the above docker commands.

In case, if wish to find container IP using ansible adhoc command, please check below.
```
ansible -i hosts ubuntu1 -m shell -a "hostname -i"
ansible -i hosts ubuntu2 -m shell -a "hostname -i"
ansible -i hosts ubuntu3 -m shell -a "hostname -i"
ansible -i hosts ubuntu4 -m shell -a "hostname -i"
```
