import sys
import state_manager
import updater
import time
import system_service

version = '1.0.2'

continue_update = True


def _update_svc():
    status_tuple = system_service.get_service_status()
    if status_tuple[1]:
        if not status_tuple[0]:
            print('Starting DyDNS update system service')
            system_service.start_service()
            print(f'{system_service.get_service_status()[2]}')
        else:
            print('Restarting DyDNS update system service')
            system_service.restart_service()
            print(f'{system_service.get_service_status()[2]}')
        return

    print('Starting DyDNS update thread')
    # TODO - do this in an actual thread
    while continue_update:
        print('Updating ClouDNS domains')
        state = state_manager.get_state()
        errors = updater.update(state)
        print('Updated ClouDNS domains')
        if len(errors) > 0:
            print(f'Encountered {str(len(errors)}} errors')
            for error in errors:
                print(f'ERROR: {str(error)}')
        interval = state_manager.get_config()['updateIntervalMinutes'] * 60
        time.sleep(interval)
    print('DyDNS update thread ended')


def _application():
    if len(sys.argv) > 1 and (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        print(f'Available Commands:')
        print('----------------------------')
        print('-h (| --help) : Shows this screen')
        print('-a (| --add-hostname) <HOSTNAME/DOMAIN> <CLOUDNS_DYNAMIC_UPDATE_URL> : Add host to update list')
        print('-uim (| --update-interval-minutes) <MINUTES_BETWEEN_UPDATES> : Sets update interval minutes')
        print('(no arguments) : Start the DyDNS update service')
        return

    if len(sys.argv) == 4 and (sys.argv[1] == '-a' or sys.argv[1] == '--add-hostname'):
        print(f'Adding domain {sys.argv[2]} with update URL {sys.argv[3]}')
        state_manager.add_entry(sys.argv[2], sys.argv[3])
        print(f'Added domain {sys.argv[2]} with update URL {sys.argv[3]}')
        return

    if len(sys.argv) == 3 and (sys.argv[1] == '-uim' or sys.argv[1] == '--update-interval-minutes'):
        print(f'Setting update interval minutes to {sys.argv[2]}')
        config = state_manager.get_config()
        config['updateIntervalMinutes'] = int(sys.argv[2])
        state_manager.update_config(config)
        print(f'Set update interval minutes to {sys.argv[2]}')
        return

    if len(sys.argv) == 2 and (sys.argv[1] == '-lh' or sys.argv[1] == '--list-hostnames'):
        print(f'Listing currently active hostnames')
        state = state_manager.get_state()
        for host in state:
            printf(f'Hostname: {host["domain"]}, Added At: {host["addedAt"]}')
        return

    _update_svc()


def main():
    print(f'ClouDNS DyDNS Update Client')
    print('----------------------------')
    print(f'Version: {version}')
    print('2024 Robert Kirchner JR(rjojjr)')
    print('----------------------------')
    print()
    _application()


if __name__ == '__main__':
    main()