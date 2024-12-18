import subprocess
import errno
import os
from sys import platform


def stop_service():
    subprocess.run(["sudo", "systemctl", "stop", "cloudns-ddns-update-client.service"])


def start_service():
    subprocess.run(["sudo", "systemctl", "start", "cloudns-ddns-update-client.service"])


def restart_service():
    subprocess.run(["sudo", "systemctl", "restart", "cloudns-ddns-update-client.service"])


def _is_root():
    try:
        os.rename('/some/dir/that/does/not/exist', '/etc/bar')
    except IOError as e:
        if e[0] == errno.EPERM:
            return False
    return True


def is_linux():
    return platform == "linux" or platform == "linux2"


def get_service_status():
    if not _is_root():
        return (False, False, 'Must have root permission', False)
    process = subprocess.Popen("sudo systemctl status cloudns-ddns-update-client.service", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in process.stdout.readlines():
        if 'Unit cloudns-ddns-update-client.service could not be found' in line:
            return (False, False, 'DyDNS service not installed', True)
        if 'inactive' in line.lower():
            return (False, True, 'DyDNS service is not active', True)
        if 'active' in line.lower():
            return (True, True, 'DyDNS service is active', True)
    return (False, False, 'DyDNS service is not installable', True)