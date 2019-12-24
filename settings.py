import json
def GetSettings(settings_file):
    with open(settings_file, 'r') as fp:
        file = json.load(fp)
        return file["settings"]