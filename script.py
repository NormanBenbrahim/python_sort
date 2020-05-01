# sort

# we will sort different lists with python
a = [7,3,9,44,76,78]

fruits = ['bananas', 'apples', 'oranges', 'kiwis', 'dragonfruits', 'pears']

#fruits.sort()
#print(fruits)

def sorter_func(x):
    return len(x)


fruits.sort(key=sorter_func)
print(fruits)

my_big_list = [
    {'kitchen': 'table', 'year': 2019},
    {'kitchen': 'stove', 'year': 1999},
    {'living_room': 'couch', 'year': 2018},
    {'living_room': 'tv', 'year': 2020}    
]

def new_sorter_func(x):
    return x['year']

my_big_list.sort(key=new_sorter_func)
print(my_big_list)