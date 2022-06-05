nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, list):
        self.list = list
        self.index = 0
        self.index_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.list):
            index = self.index
            while self.index_item < len(self.list[index]):
                index_item = self.index_item
                self.index_item += 1
                return self.list[index][index_item]
            self.index += 1
            self.index_item = 0
        raise StopIteration


for item in FlatIterator(nested_list):
    print(item)


flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

