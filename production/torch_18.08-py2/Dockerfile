FROM nvcr.io/nvidia/torch:18.08-py2 
RUN set -xe; \
    apt-get update; \
    apt-get install -y sudo; \
    DEBIAN_FRONTEND=noninteractive apt-get -y install libnss-ldap libpam-ldap ldap-utils nscd ;\
    DEBIAN_FRONTEND=noninteractive apt-get install -y libpam-ldapd ;\
    apt-get -y install openssh-server openssh-client

RUN echo "%slurm  ALL=(ALL:ALL) ALL" >> /etc/sudoers    

RUN set -xe; \
    echo "session required pam_mkhomedir.so skel=/etc/skel umask=077" >> /etc/pam.d/common-session; \
    mkdir -p /var/run/sshd
COPY ldap-auth-config /etc/auth-client-config/profile.d/ldap-auth-config
COPY ldap.conf /etc/ldap.conf
COPY ldap.secret /etc/ldap.secret
RUN chmod 600 /etc/ldap.secret

COPY pam.d /etc/pam.d
COPY nslcd.conf /etc/nslcd.conf

RUN /usr/sbin/auth-client-config -t nss -p lac_ldap

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT /bin/sh /entrypoint.sh

EXPOSE 22
