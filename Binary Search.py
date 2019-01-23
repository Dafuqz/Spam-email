import random


def binary_search(the_list, char):
    '''
    Input:
        the_list (list of str)
        half (char)

    Output:
        (int): Returns the index of the char, and False if it isn't in the list.
    '''

    front = 0
    back = len(the_list) - 1
    while True:
        if back < front:
            return "False"
        half = (front + back) // 2
        if the_list[half] < char:
            front = half + 1
        elif the_list[half] > char:
            back = half - 1
        else:
            return half



    



# main code for testing.

list1 = ["a", "b", "c", "d", "e", "f"]

print binary_search(list1, "f")
