def a_to_b(a:list, b: list):
    if a:
        b = a
        return b
    else:
        return b

# a = [1]
# b = [3]

# b = a_to_b(a, b)
# print(b)

# b.append(2)
# print(b)

# a += [4]
# print(a)
# print(b)

old = [1,[1,2,3],3]
new = []
for i in range(len(old)):
    new.append(old[i])
 
new[0] = 3
new[1][0] = 3
print(old)
print(new)
