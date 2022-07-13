list1 = [['Mike', 'Thomson', '9', 'M'], ['Robert', 'Bustle', '32', 'M'], ['Andria', 'Bustle', '30', 'F'], ['asdasd', 'Basdad', '5', 'F']]

list1.sort(key=lambda x:int(x[2]))
print(list1)