FROM centos:6.7 
MAINTAINER Jeganathan Swaminathan <jegan@tektutor.org> <http://www.tektutor.org> 

RUN yum install -y openssh-server openssh-clients

# Set the password of root user to root
RUN echo 'root:root' | chpasswd

RUN usermod -aG wheel root 

RUN sed -ri 's/^session\s+required\s+pam_loginuid.so$/session optional pam_loginuid.so/' /etc/pam.d/sshd

# Disable root login &
# Disable password login, only allow public key. 
COPY sshd_config /etc/ssh/sshd_config
COPY sudoers /etc/sudoers

# Add sshd running directory.
RUN mkdir -m 700 /var/run/sshd

# Add ssh key directory.
RUN /sbin/service sshd start && /sbin/service sshd stop

EXPOSE 22
EXPOSE 80
CMD ["/usr/sbin/sshd", "-D"]
