class Foo:
    def __init__(self) -> None:
        pass

    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]


foo = Foo()
for i in foo:
    print(i)
