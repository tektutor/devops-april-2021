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
ssh -p 2002 root@localhost
```

You need type 'yes' when it prompts for 'docker run -d --name ubuntu1 --hostname ubuntu1 -p 2001:22 tektutor/ansible-ubuntu
' question.

The expectation here is, ssh shouldn't prompt for password as we are using key-pair for login authentication.
