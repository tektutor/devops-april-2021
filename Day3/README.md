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
