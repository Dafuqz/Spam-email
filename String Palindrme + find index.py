def palindrome(str):
    return str == "".join(reversed(str))



print(palindrome("dad"))



def Hardpalindrom(str):
    '''
        Input:
            a string


        Output:
            return true if the string is a palindrome



        '''
    for i in range(len(str) // 2):
        if str[i] != str[-i - 1]:
            return False


    return True





# print(Hardpalindrom("doggod"))


def findIndex(list, char):
    for i in range(len(list)):
        if list[i] == char:
            return i


myList = [0,"!23", 4, "b"]

print (findIndex(myList, 4))

def easyFindIndex(list, char):
    return list.index(char)



print(easyFindIndex(myList,"b"))