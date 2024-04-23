# number = [1,2,3]
# newlist = []
# for n in number:
#     add_1 = n+1
#     newlist.append(add_1)
# print(newlist)

"""newlist = [newitem for item in list]"""

# numbers = [1,2,3,4,5]
# new_list = [n+1 for n in numbers]
# print(new_list)

# name = "Subham"
# new_name = [l for l in name]
# print(new_name)


# double_num = [i+i for i in range(1,5)]
# print(double_num)

"""Conditional List Comprehension"""
"""newlist = [newitem for item in list if test]"""

names = ['subham','babulu','chiku','sipu','nikhil','ajit']
long_names = [name.upper() for name in names if len(name)>5]
short_names = [name.capitalize() for name in names if len(name)<5]
print(long_names)
print(short_names)
