import glob
import json
import os
import time

txtfiles = []
for file in glob.glob("*.txt"):
    txtfiles.append(file)


def get_state() -> list:
    state_file = open(f"{_get_state_dir()}{os.sep}state.json","r")
    state = json.loads(state_file.read())
    state_file.close()
    return state


def _write_state(state: list) -> list:
    state_file = open(f"{_get_state_dir()}{os.sep}state.json","w")
    state_file.write(json.dumps(state))
    state_file.close()


def add_entry(domain: str, update_url: str) -> None:
    state = get_state()
    state.append({"domain": domain, "updateUrl": update_url, "addedAt": time.time()})
    _write_state(state)


def _get_state_dir():
    dir_name = f'.cloudns-updater{os.sep}state'
    user_home_dir = os.path.expanduser("~")
    return os.path.join(user_home_dir, dir_name)

def _create_state_directory():
    dir_path = _get_state_dir()
    dir_name = dir_path.split(os.sep)[len(dir_path.split(os.sep)) - 1]
    state_path = dir_path.replace(dir_name, '')
    if not os.path.exists(dir_path):
        try:
            os.makedirs(dir_path)
            print(f"Directory '{dir_name}' created successfully at '{state_path}'.")
            return
        except Exception as e:
            print(f"Error creating directory '{dir_name}' at '{state_path}': {e}")
            raise e

    print(f"Directory '{dir_name}' already exists at '{state_path}'.")