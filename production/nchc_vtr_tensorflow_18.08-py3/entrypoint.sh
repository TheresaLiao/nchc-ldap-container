set -xe
service nscd stop
service nslcd start
/root/try.py &
/usr/sbin/sshd -D
