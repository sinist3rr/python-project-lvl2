import json
import yaml


def bool_transform(item):
    if item is True:
        return 'true'
    if item is False:
        return 'false'
    return item


def print_like_json(item):
    result = '{\n'
    for i in item:
        result += '\t{} {}: {}\n'.format(i[0], i[1], bool_transform(i[2]))
    result += '}\n'
    return result


def parse_file(filename):
    if filename.endswith('.json'):
        with open(filename, 'r') as jsonfile:
            return json.load(jsonfile)
    if filename.endswith('.yml'):
        with open(filename) as ymlfile:
            return yaml.load(ymlfile, Loader=yaml.FullLoader)
    return 'unknown file type'


def generate_diff(file1, file2):
    file1_dict = parse_file(file1)
    file2_dict = parse_file(file2)
    file1_keys = set(file1_dict)
    file2_keys = set(file2_dict)
    shared_keys = file1_keys.intersection(file2_keys)
    added_keys = file2_keys.difference(file1_keys)
    removed_keys = file1_keys.difference(file2_keys)
    diff_store = []

    for i in added_keys:
        diff_store.append(('+', i, file2_dict[i]))
    for i in removed_keys:
        diff_store.append(('-', i, file1_dict[i]))
    for i in shared_keys:
        if file1_dict[i] == file2_dict[i]:
            diff_store.append((' ', i, file1_dict[i]))
        else:
            diff_store.append(('-', i, file1_dict[i]))
            diff_store.append(('+', i, file2_dict[i]))

    diff_store.sort(key=lambda x: x[1])
    return print_like_json(diff_store)
