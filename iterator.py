iterator = iter('abc')
print(next(iterator))
print(next(iterator))
print(next(iterator))

# using object oriented programming
class Iterator(object):
    def __init__(self, step):
        self.step = step

    def __next__(self):
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        return self

if __name__ == "__main__":
    itera = Iterator(5)
    [print(value) for value in itera]
