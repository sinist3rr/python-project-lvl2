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
    diff_store = []

    for i in file1_dict:
        if i in file2_dict:
            if file1_dict[i] == file2_dict[i]:
                diff_store.append((' ', i, file1_dict[i]))
            else:
                diff_store.append(('-', i, file1_dict[i]))
                diff_store.append(('+', i, file2_dict[i]))
        else:
            diff_store.append(('-', i, file1_dict[i]))

    for i in file2_dict:
        if i not in file1_dict:
            diff_store.append(('+', i, file2_dict[i]))

    diff_store.sort(key=lambda x: x[1])
    return print_like_json(diff_store)
