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
