import json


def get_entries():
    entries = dict()
    with open('data/entries.json', mode='r') as f:
        data = json.load(f)
    for i in data:
        entries[i['word']] = list(i['translations'])
    entries = dict(sorted(entries.items()))
    return entries


def create_entry(ang, fra):
    error = 0
    msg = ""
    try:
        with open('data/entries.json', mode='r') as f:
            data = json.load(f)
        data.append({'word': str(ang), 'translations': fra.split(',')})
        with open('data/entries.json', mode='w') as f:
            f.write(json.dumps(data))
    except Exception as e:
        error = -1
        msg = e
    return error, msg


def set_entry(ang, fra):
    error = 0
    msg = ""
    try:
        with open('data/entries.json', mode='r') as f:
            data = json.load(f)
        for i in data:
            if i['word'] == ang:
                i['translations'] = fra.split(',')
        with open('data/entries.json', mode='w') as f:
            f.write(json.dumps(data))
    except Exception as e:
        error = -1
        msg = e
    return error, msg