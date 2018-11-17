set -xe
service nscd stop
service nslcd start
/usr/sbin/sshd -D
