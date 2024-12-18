import json
import os
import time


def add_entry(domain: str, update_url: str) -> None:
    state = get_state()
    state.append({"domain": domain, "updateUrl": update_url, "addedAt": time.time(), "active": True})
    _write_state(state)


def get_state() -> list:
    file_path = f"{_get_state_dir()}{os.sep}state.json"
    if not os.path.exists(file_path):
        return []
    state_file = open(file_path,"r")
    state = json.loads(state_file.read())
    state_file.close()
    return state


def get_config() -> dict:
    file_path = f"{_get_state_dir()}{os.sep}config.json"
    if not os.path.exists(file_path):
        return {"updateIntervalMinutes": 15}
    config_file = open(file_path,"r")
    config = json.loads(config_file.read())
    config_file.close()
    return config


def update_config(config: dict) -> None:
    _write_config(config)

def _write_state(state: list) -> None:
    _create_state_directory()
    state_file = open(f"{_get_state_dir()}{os.sep}state.json","w+")
    state_file.write(json.dumps(state))
    state_file.close()


def _write_config(config: dict) -> None:
    _create_state_directory()
    config_file = open(f"{_get_state_dir()}{os.sep}config.json","w+")
    config_file.write(json.dumps(config))
    config_file.close()


def _get_state_dir():
    dir_name = f'.cloudns-updater{os.sep}state' if os.name == 'nt' else f'{os.sep}usr{os.sep}local{os.sep}cloudns-ddns-client{os.sep}state'
    return os.path.join(os.path.expanduser("~"), dir_name) if os.name == 'nt' else dir_name

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