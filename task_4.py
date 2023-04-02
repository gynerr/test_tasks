import json
from datetime import datetime


def recursive_change(data, key):
    if key in data:
        data[key] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    for k, v in data.items():
        if isinstance(v, dict):
            recursive_change(v, key)


def main(file_name):
    with open(file_name, 'r', encoding='Utf-8') as file:
        data = json.load(file)
        recursive_change(data, 'updated')

    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    main('test_json.json')
