import random


def remove_duplicates(lis):

    # order doesn't matter here
    lis1 = set(lis)
    return list(lis1)


my_list = ["b", "c",5,"c", 4, 5, 4, 1]
#print(remove_duplicates(my_list))

def remove_d(lis):

    # order does matter
    re = []
    for i in range(len(lis)):
        boy = lis[i]
        if boy not in re:
            re.append(boy)

    return re


b = remove_d(my_list)

print b



def random_search(lis,item):
    randomint = random.randint(0,len(lis)-1)

    if lis[randomint] == item:
        return randomint
    else:
        random_search(lis,item)



print random_search(b, 1)