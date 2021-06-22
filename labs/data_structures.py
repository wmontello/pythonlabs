grocery = ['milk','coffee','bread','eggs']
print(grocery)
grocery.remove('milk')
grocery.insert(0,'OJ')

print(grocery[0])
grocery.remove(grocery[len(grocery)-1])
print(grocery)