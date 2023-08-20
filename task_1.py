__all__ = ["traverse_directory", "save_as_json", "save_as_csv", "save_as_pickle"]

import os
import json
import csv
import pickle


def traverse_directory(directory):
    result = []

    for root, dirs, files in os.walk(directory):
        print(root, dirs, files)
        current_dir = {
            'name': os.path.basename(root),
            'type': 'directory',
            'size': 0,
            'parent_directory': os.path.dirname(root)
        }

        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            current_dir['size'] += file_size

            result.append({
                'name': file,
                'type': 'file',
                'size': file_size,
                'parent_directory': os.path.basename(root)
            })

        result.append(current_dir)

    return result


def save_as_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def save_as_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


def save_as_pickle(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


result = traverse_directory("c:\\JavaScript")

save_as_json(result, 'result.json')
save_as_csv(result, 'result.csv')
save_as_pickle(result, 'result.pickle')
