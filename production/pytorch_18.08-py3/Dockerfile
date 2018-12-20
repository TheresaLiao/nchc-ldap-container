FROM nvcr.io/nvidia/pytorch:18.08-py3

# Install required packages
RUN apt-get update  && \
    apt-get install -y sudo && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install libnss-ldap libpam-ldap ldap-utils nscd && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install libpam-ldapd && \
    apt-get install -y openssh-server openssh-client supervisor

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

# Install python3's pip package
RUN apt-get install -y libsqlite3-dev \
        libzmq3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.5 2

# install jupyter
RUN python -m pip install --upgrade IPython
RUN python -m pip install --upgrade pip
RUN python -m pip install jupyter
RUN rm -fr /root/.cache
RUN jupyter notebook --generate-config --port 8888

# Set up our notebook config.
COPY jupyter_notebook_config.py /root/.jupyter/

# Jupyter has issues with being run directly:
#   https://github.com/ipython/ipython/issues/7062
# We just add a little wrapper script.
COPY run_jupyter.sh /
RUN ["chmod", "+x", "/run_jupyter.sh"]

# Copy sample notebooks.
COPY notebooks /workspace
RUN ["chown", "-R", "11899:11899", "/workspace"]
RUN ["chmod", "0777", "/workspace"]
WORKDIR "/workspace"

EXPOSE 22

# IPython
EXPOSE 8888


ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN sed -i '/#!\/usr\/bin\/python/c\#!/usr/bin/python2' /usr/bin/supervisord
ENTRYPOINT ["/usr/bin/supervisord"]
