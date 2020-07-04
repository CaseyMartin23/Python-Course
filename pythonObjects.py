# Object naming
num = 100
num_all = 1000
sum10 = 10
# 10sum = 10  bad practise
_10sum = 10
# syn$ = 100  # bad practise

# print(num)
# print(type(num), id(num))

# Same ID's because some memory assign to both
n1 = "Jonh"
print(type(n1), id(n1))

n2 = "Jonh"
print(type(n2), id(n2))

x = 100
y = 100

print(id(x), id(y))