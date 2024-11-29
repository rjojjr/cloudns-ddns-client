# ClouDNS DDNS Update Client README

This is a simple python app to manage DyDNS updates for hostnames powered
[ClouDNS](https://www.cloudns.net)'s DNS service. This app currently depends on
the user manually creating and entering ClouDNS update URLs,
but I plan to integrate with the ClouDNS in the very near future.

## Installation

This client can currently be installed as systemd service
on most Unix distributions. 

To install this client as a system service:

```shell
curl -fsSL https://raw.githubusercontent.com/rjojjr/cloudns-ddns-client/master/scripts/linux-installer.sh | sudo bash
```

## USAGE

### Adding Hostnames

To add a ClouDNS hostname to be updated, run this app 
with the `-a`(or `--add-hostname`) flag followed by the hostname and then the
DyDNS update URL provided by the ClouDNS webapp.

EX:

```shell
python3 src/main.py -a example.com https://ipv4.cloudns.net/api/dynamicURL/?q=XyZ...
```

OR(when installed as system service a Unix-based host)

```shell
cloudns-client -a example.com https://ipv4.cloudns.net/api/dynamicURL/?q=XyZ...
```

### Updating Hostnames

The automated updater client currently runs at fixed interval of
15 minutes. To start the app in update mode, simply run the
program with no arguments:

```shell
python3 src/main.py
```

OR(when installed as system service a Unix-based host)

```shell
cloudns-client
```