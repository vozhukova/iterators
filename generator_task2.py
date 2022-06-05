nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


def flat_generator(list_cons):
    new_list = []
    for list in list_cons:
        new_list.extend(list)
    for item in new_list:
        yield item


for item in flat_generator(nested_list):
    print(item)
