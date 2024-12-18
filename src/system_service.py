import subprocess


def stop_service():
    subprocess.run(["sudo", "systemctl", "stop", "cloudns-ddns-update-client.service"])


def start_service():
    subprocess.run(["sudo", "systemctl", "start", "cloudns-ddns-update-client.service"])


def restart_service():
    subprocess.run(["sudo", "systemctl", "restart", "cloudns-ddns-update-client.service"])


def get_service_status():
    process = subprocess.Popen("sudo systemctl status cloudns-ddns-update-client.service", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in process.stdout.readlines():
        if 'could not be found' in line:
            return (False, False, 'DyDNS service not installed')
        if 'inactive' in line.lower():
            return (False, True, 'DyDNS service is not active')
        if 'active' in line.lower():
            return (True, True, 'DyDNS service is active')
    return (False, False, 'DyDNS service is not installable')