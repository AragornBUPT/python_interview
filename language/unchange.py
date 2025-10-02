# 函数
def test_no_define(age, name):
    age = 123
    name = "poloyy"
    print(age, name)


age = 1
name = "yy"
print(age, name)

test_no_define(age, name)
print(age, name)


# 函数
def test_define(dicts, sets):
    dicts["age"] = 24
    sets.pop()
    print(dicts, sets)


dicts = {"age": 123}
sets = {1, 2}
print(dicts, sets)

test_define(dicts, sets)
print(dicts, sets)
