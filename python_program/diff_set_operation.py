# Python Program to Illustrate Different Set Operations  ????

# define three sets
E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}

# set union
print("Union of E and N is",E | N)

# set intersection
print("Intersection of E and N is",E & N)

# set difference
print("Difference of E and N is",E - N)

# set symmetric difference
print("Symmetric difference of E and N is",E ^ N)


'''
E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}

output ==
Union of E and N is {0, 1, 2, 3, 4, 5, 6, 8}
Intersection of E and N is {2, 4}
Difference of E and N is {0, 8, 6}
Symmetric difference of E and N is {0, 1, 3, 5, 6, 8}

'''