FROM nvcr.io/nvidia/tensorflow:18.08-py3

# Install required packages
RUN apt-get update  && \
    apt-get install -y sudo apt-utils && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install libnss-ldap libpam-ldap ldap-utils nscd && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install libpam-ldapd && \
    apt-get install -y openssh-server openssh-client supervisor
RUN apt-get clean all

COPY init.sh /etc/profile.d/

# Assign slurm as admin(sudo)
RUN echo "%slurm  ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/slurm   

RUN echo "session required pam_mkhomedir.so skel=/etc/skel umask=077" >> /etc/pam.d/common-session && \
    mkdir -p /var/run/sshd

# LDAP Config
COPY ldap-auth-config /etc/auth-client-config/profile.d/ldap-auth-config
COPY ldap.conf /etc/ldap.conf
COPY ldap.secret /etc/ldap.secret
RUN chmod 600 /etc/ldap.secret

COPY pam.d /etc/pam.d
COPY nslcd.conf /etc/nslcd.conf

RUN /usr/sbin/auth-client-config -t nss -p lac_ldap

COPY entrypoint.sh /entrypoint.sh
RUN ["chmod", "+x", "/entrypoint.sh"]
#ENTRYPOINT /bin/sh /entrypoint.sh

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.5 2
RUN update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1

# install jupyter
RUN python3 -m pip install jupyter
RUN rm -fr /root/.cache
RUN jupyter notebook --generate-config --port 8888
# RUN python3 -m pip install --upgrade pip

# Install python's pip package
# RUN python -m pip --version
# RUN python -m pip install -U setuptools

# Set up our notebook config.
COPY jupyter_notebook_config.py /root/.jupyter/

# Copy sample notebooks.
COPY notebooks /workspace

# Jupyter has issues with being run directly:
#   https://github.com/ipython/ipython/issues/7062
# We just add a little wrapper script.
COPY run_jupyter.sh /
RUN ["chmod", "+x", "/run_jupyter.sh"]

WORKDIR "/workspace"
RUN chmod 0777 /workspace

EXPOSE 22
EXPOSE 8888

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf 
RUN sed -i '/#!\/usr\/bin\/python.*/c\#!/usr/bin/python2' /usr/bin/supervisord
ENTRYPOINT ["/usr/bin/supervisord"]
