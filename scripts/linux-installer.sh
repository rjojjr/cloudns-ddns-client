#!/bin/bash

echo 'Installing ClouDNS DyDNS Update Client'

# TODO - version argument
# TODO - argument to install from local repo(no git clone)

# TODO - install deps. for other OSes
if [[ "$1" == "--install-apt-deps" ]]; then
  echo 'Installing apt dependencies'
  {
    apt install python3-pip -y && \
      apt install python3-venv -y
  } || {
    echo 'Failed to install Torch Tuner CLI apt dependencies' && \
      exit 1
  }

fi

cd /usr/local || (mkdir -p /usr/local && (cd /usr/local || (echo 'failed to create install directory at /usr/local' && exit 1)))

if [ -d ./cloudns-ddns-client  ]; then
  echo "Removing old update client install"
  {
    rm -rf ./cloudns-ddns-client
  } || {
    echo 'Failed to remove old update client install' && \
    exit 1
  }
fi

{
  git clone https://github.com/rjojjr/cloudns-ddns-client.git
} || {
  echo 'Failed to clone update client' && \
    exit 1
}

{
  cd cloudns-ddns-client
} || {
  echo 'Failed to navigate to cloudns-ddns-client directory' && \
      exit 1
}

{
  echo 'Installing update client as system wide application' && \
  cp scripts/cloudns-client /bin/cloudns-client && \
  sudo chmod +x /bin/cloudns-client
} || {
  echo 'Failed to install update client as system wide application' && \
      exit 1
}

{
  echo 'Installing update client systemd service' && \
    cp svc/cloudns-ddns-update-client.service /etc/systemd/system/ && \
    sudo systemctl enable cloudns-ddns-update-client.service && \
    sudo systemctl start cloudns-ddns-update-client.service
} || {
    echo 'Failed to install update client service' && \
    exit 1
}

echo 'ClouDNS DyDNS Update Client installed successfully!'