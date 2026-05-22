import json

def save_memory(data):

    with open("data.json", "w") as file:
        json.dump(data, file)

def load_memory():

    try:
        with open("data.json", "r") as file:
            return json.load(file)

    except:
        return {}