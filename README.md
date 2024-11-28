# ClouDNS DDNS Client README

This is a simple python app to manage DyDNS updates for 
[ClouDNS](https://www.cloudns.net). This app currently depends on
the user manually creating and entering ClouDNS update URLs,
but I plan to integrate with the ClouDNS in the very near future.

## USAGE

### Adding Hostnames

To add a ClouDNS hostname for updates, run this app 
with the `-a`(or `--add-hostname`) flag followed by the hostname and then the
DyDNS update URL provided by the ClouDNS webapp.

EX:

```shell
python3 src/main.py -a example.com https://ipv4.cloudns.net/api/dynamicURL/?q=XyZ...
```

### Updating Hostnames

The automated updater currently runs at fixed interval of
15 minutes. To start the app in update mode, simply run the
program with no arguments:

```shell
python3 src/main.py
```