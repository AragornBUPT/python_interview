def test_transfer(a):
    a.append(1)
    print(a)


a = [0, 1, 2]
b = a
print(a)
print(b)
test_transfer(a)
print(a)
print(b)
