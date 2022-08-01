# use Ubuntu jammy release
FROM ubuntu:jammy

# installs
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y python3 \
    python3-pip \
    sudo

# update
RUN apt-get update && apt-get -y upgrade

# create new dev user
RUN useradd --user-group --create-home --shell /bin/bash dev ;\
    echo "dev ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER dev
