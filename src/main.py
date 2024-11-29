import sys
import state_manager
import updater
import time

interval = state_manager.get_config()['updateIntervalMinutes'] * 60 * 60

def main():
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

    print('Starting DyDNS update thread')
    while True:
        print('Updating ClouDNS domains')
        state = state_manager.get_state()
        updater.update(state)
        print('Updated ClouDNS domains')
        interval = state_manager.get_config()['updateIntervalMinutes'] * 60
        time.sleep(interval)


if __name__ == '__main__':
    main()