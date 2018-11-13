# ldap-container

##Test by docker
```shell=
ex. sthost01 / PWDhostst01
docker build -t ubuntu:ldap .
docker run -d -P --name test_ldap ubuntu:ldap
docker port test_ldap 22
docker ps |grep test_ldap

docker exec -ti test_ldap bash
getent passwd slurmuser
su ${ldapuser}
exit

ssh ${ldapuser}@localhost -p ${22forword_port}

docker stop test_ldap && docker rm test_ldap 
```

##Test by kubernetes
```shell=
kubectl create -f ldap-ssh.yaml
```
