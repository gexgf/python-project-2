set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 3, 4, 5}

# def check_subset (set1, set2):
#     return set2.issubset(set1)
#
# print(check_subset(set1, set2))

def check_superset (set1, set2):
    return set2.issuperset(set1)

print(check_superset(set1, set2))

