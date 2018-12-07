# ldap-container


## Image status
|Repo name|Tag|Nvidia Driver|update date|Production use|
|:--------|:-:|:-----------:|:---------:|:------------:|
|caffe|18.08-py2|384.xx|2018/11/07|✔|
|caffe|18.10-py2|---.--|----/--/--|✖|
|caffe2|18.08-py2|384.xx|2018/11/07|✔|
|cntk|18.08-py3|384.xx|2018/11/07|✔|
|cuda|9.0-cudnn7.1-devel-ubuntu16.04|384.xx|2018/11/07|✔|
|digits|18.08|384.xx|2018/11/07|✔|
|digits|18.10|---.--|----/--/--|✖|
|mxnet|18.08|384.xx|2018/11/07|✔|
|mxnet|18.10|---.--|----/--/--|✖|
|pytorch|18.08-py2|384.xx|2018/11/07|✔|
|pytorch|18.10-py2|---.--|----/--/--|✖|
|tensorrt|18.08-py3|384.xx|2018/11/07|✔|
|tensorrt|18.10-py3|---.--|----/--/--|✖|
|tensorrtserver|18.08-py2|384.xx|2018/11/07|✔|
|tensorrtserver|18.10-py3|---.--|----/--/--|✖|
|theano|18.08-py2|384.xx|2018/11/07|✔|
|torch|18.08-py2|384.xx|2018/11/07|✔|

## Test 
### By docker
```shell=
ex. sthost01 / PWDhostst01
// Create contaiber
docker build -t ubuntu:ldap .
docker run -d -P --name test ubuntu:ldap
docker exec -ti test bash

// Check connect ldap server
getent passwd slurmuser
su ${ldapuser}
exit

// ssh by ldap user
ssh ${ldapuser}@localhost -p ${22forword_port}

// delete container
docker stop test && docker rm test
```

### Test by kubernetes
```shell=
kubectl create -f ldap-ssh.yaml
```
