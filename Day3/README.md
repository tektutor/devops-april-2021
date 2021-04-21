### Building ubuntu ansible nod docker image
```
cd ubuntu-ansible-image
```
#### Generate ssh key pairs
```
ssh-keygen
```
You may accept all default values while generating key pairs.

```
docker build -t tektutor/ansible-ubuntu .
```

Check if the newly built image is listed
```
docker images
```
