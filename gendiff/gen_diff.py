import json


def bool_transform(item):
    if item is True:
        return 'true'
    if item is False:
        return 'false'
    return item


def print_like_json(item):
    result = '{\n'
    for i in item:
        result += '\t{} {}: {}\n'.format(i[1], i[0], i[2])
    result += '}\n'
    return result


def generate_diff(file1, file2):
    with open(file1, 'r') as openfile:
        file1_dict = json.load(openfile)
    with open(file2, 'r') as openfile:
        file2_dict = json.load(openfile)
    diff_store = []

    for i in file1_dict:
        if i in file2_dict:
            if file1_dict[i] == file2_dict[i]:
                diff_store.append((i, ' ', bool_transform(file1_dict[i])))
            else:
                diff_store.append((i, '-', bool_transform(file1_dict[i])))
                diff_store.append((i, '+', bool_transform(file2_dict[i])))
        else:
            diff_store.append((i, '-', bool_transform(file1_dict[i])))

    for i in file2_dict:
        if i not in file1_dict:
            diff_store.append((i, '+', bool_transform(file2_dict[i])))

    diff_store.sort(key=lambda x: x[0])
    return print_like_json(diff_store)
