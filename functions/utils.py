from json import load, dump


NoneType = type(None)


def get_settings(target:str):
    with open(f"./settings/{target}.json", "r") as f:
        return load(f)


def edit_settings(target:str, key:str, value:str):
    settings = get_settings(target)
    settings[key] = value
    with open(f"./settings/{target}.json", "w") as f:
        dump(settings, f)