docker build -t ubuntu:ldap .
docker stop test_ldap && docker rm test_ldap 
docker run -d --name test_ldap ubuntu:ldap
docker port test_ldap 22
docker exec -ti test_ldap bash
