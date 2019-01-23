def word_counter(str1):

    return len(str1.split(" "))


tr = open("11-0.txt")
tr1 = tr.read()

# print(word_counter(tr1))





def hard_word_counter(str2):
    wordcount = {}
    lmao = str2.split(" ")


    for word in (lmao):
        word = word.lower()

        if "\r" in word:
            word = word.replace("\r", "")
        if "\xe2\x80\x98" in word:
            word = word.replace("\xe2\x80\x98", "'")

        if "\n" in word:
            word = word.replace("\n", "")

        if "," in word:
            word = word.replace(",", "")

        if "?" in word:
            word = word.replace("?", "")

        if "." in word:
            word = word.replace(".", "")

        if "'s" in word:
            word = word.replace("'s", "")

        if word not in wordcount:
            wordcount[word] = 1

        else:
            wordcount[word] = wordcount[word] + 1


    del wordcount['']

    return wordcount




print(hard_word_counter(tr1))


def many_dict10(dict):
    big= 0
    ind = ""
    big_list= []
    for b in range(10):
        for key in dict:
            if dict[key] > big:
                ind = key
                big = dict[ind]

        del dict[ind]
        big_list.append(ind)
        big = 0
        ind = 0



    return big_list


print(many_dict10(hard_word_counter(tr1)))