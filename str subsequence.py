
def str_subsequence(str1):
    most1 = 1
    most = 0



    while 5==5:
        if len(str1) < 2:
            if most1 > most:
                most = most1
                most1 = 1
            break

        if str1[0] == str1[1]:
            most1 = most1 + 1
        if str1[0] != str1[1]:
            if most1 > most:
                most = most1
                most1 = 1
        str1 = str1[1:]


    return most

str3 = "fabbcccccddddeeeeeffffffffff"

print(str_subsequence(str3))