from json import load, dump


def get_settings():
    f = open("./settings/client.json", "r")
    settings = load(f)
    f.close()
    return settings


def edit_settings(key: str, value: str):
    settings = get_settings()
    settings[key] = value
    f = open("./settings/client.json", "w")
    dump(settings, f)
    f.close()  