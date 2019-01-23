from string import punctuation

import os
import random



'''

Spam email detection:

Input:
    an email that is either spam or ham
    
Output:
    determine if the email is spam or ham

'''

# change keyword_num to use more or less keywords to test the program
keyword_num = 30
spam_words = {}
ham_words = {}
ham_counter = 0
spam_counter = 0
spam_list20 = {}
ham_list20 = {}
list_of_words = []
list_of_hwords = []

def naive_bayes(spam,ham):

    for key in spam:
        b = 0
        try:
            b = ham[key]
        except KeyError:
            b = 0
        pro = float(spam[key])/(spam[key] + b)
        spam[key] = pro

    return spam

def word_counter(str1):

    return len(str1.split(" "))


def many_dict20ham(dict):
    global ham_counter, ham_list20, keyword_num
    big= 0
    ind = ""
    big_list= []
    for b in range(keyword_num):
        for key in dict:
            if dict[key] > big:
                ind = key
                big = dict[ind]


        #print dict[ind], ind
        ham_counter += dict[ind]
        ham_list20[ind] = dict[ind]
        del dict[ind]
        big_list.append(ind)
        big = 0
        ind = 0



    return big_list

def many_dict20spam(dict):
    global spam_counter, ham_list20, keyword_num
    big= 0
    ind = ""
    big_list= []
    for b in range(keyword_num):
        for key in dict:
            if dict[key] > big:
                ind = key
                big = dict[ind]


        #print dict[ind], ind
        spam_counter += dict[ind]
        spam_list20[ind] = dict[ind]
        del dict[ind]
        big_list.append(ind)
        big = 0
        ind = 0



    return big_list

def remove_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

def read_ham():

    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    ham_words = {}
    path = 'ham'
    listing = os.listdir(path)
    for infile in listing:
        email = open(path + "/" + infile)
        #print "current file is: " + infile
        real_email = email.read()
        real_email = real_email.splitlines()






        for i in range(len(real_email)):



            boy = real_email[i].split(" ")
            for word in boy:
                if word in num and "num" not in ham_words:
                    ham_words["num"] = 1

                elif word not in ham_words:
                    ham_words[word] = 1

                elif word in num and "num" not in ham_words:
                    ham_words["num"] += 1
                else:
                    ham_words[word] += 1


    return ham_words

    


def read_spam():

    num = ["1","2","3","4","5","6","7","8","9","0"]
    path = 'spam'
    listing = os.listdir(path)
    spam_words = {}
    for infile in listing:
        #print "current file is: " + infile
        email = open(path + '/' + infile)
        real_email = email.read()

        real_email = real_email.splitlines()



        for i in range(len(real_email)):

            boy = real_email[i].split(" ")

            for word in boy:
                if word in num and "num" not in spam_words:
                    spam_words["num"] = 1

                elif word not in spam_words:
                    spam_words[word] = 1


                elif word in num and "num" in spam_words:
                    spam_words["num"] += 1

                else:
                    spam_words[word] += 1

    return spam_words





'''
email = open("spam_ham.txt")
real_email = email.read()
real_email = real_email.splitlines()
print(real_email)



for i in range(len(real_email)):
    if real_email[i][:2] == "No":
        boy = real_email[i][4:].split(" ")
        for word in boy:
            if word not in ham_words:
                ham_words[word] = 1

            else:
                ham_words[word] = ham_words[word] + 1

    elif real_email[i][:3] == "Yes":
        boy = real_email[i][5:].split(" ")
        for word in boy:
            if word not in spam_words:
                spam_words[word] = 1

            else:
                spam_words[word] = spam_words[word] + 1




print spam_words, ham_words
'''

def delete_spam(dic):

    del dic["."], dic[","], dic["-"], dic["the"], dic["to"], dic["/"], dic["and"], dic[":"], dic["of"], dic["a"], dic["in"], dic["="]
    del dic["!"], dic["for"], dic["is"], dic["you"], dic["?"], dic["your"], dic["("], dic[")"], dic["|"], dic["that"], dic["Subject:"]
    del dic["be"], dic["or"], dic["_"], dic["this"], dic["'"], dic["with"], dic["s"], dic["on"], dic["are"], dic[";"], dic["i"], dic["as"]
    del dic["not"], dic["it"]

    return dic


def delete_ham(dic):

    del dic["."], dic[","], dic["-"], dic["the"], dic["to"], dic["/"], dic["and"], dic[":"], dic["of"], dic["a"], dic["in"], dic["="]
    del dic["for"], dic[">"], dic["you"], dic["i"], dic[")"], dic["("], dic["Subject:"], dic["that"], dic["is"], dic["<"], dic["are"]
    del dic['"'], dic["from"], dic["subject"], dic["be"], dic["?"], dic["'"], dic["am"]


    return dic


spam1 = read_spam()
ham1 = read_ham()
#print ham1
spam1 = delete_spam(spam1)
ham1 = delete_ham(ham1)

#print spam1
#print ham1["e"]

many_dict20spam(spam1)

many_dict20ham(ham1)

#print ham_counter
#print spam_counter

#print spam_list20
#print ham_list20
final_spam = naive_bayes(spam_list20, ham1)
final_ham = naive_bayes(ham_list20, spam1)

for key in spam_list20:
    list_of_words.append(key)

#print(list_of_words)

for key in ham_list20:
    list_of_hwords.append(key)

#print list_of_hwords
def main1():
    global list_of_words, final_spam, final_ham

    lps = []



    path = 'Testing Data2'
    listing = os.listdir(path)
    for infile in listing:
        probs = 1
        email = open(path + "/" + infile)
        #print "current file is: " + infile
        email = email.read()
        email = email.splitlines()
        for i in range(len(email)):
            boy = email[i].split(" ")
            for word in boy:
                if word in list_of_words:
                    index = list_of_words.index(word)
                    probs = probs * final_spam[list_of_words[index]]

        lps.append(probs)
        #print lps
    return lps

def main2():
    global list_of_hwords, final_spam, final_ham

    lph = []



    path = 'Testing Data2'
    listing = os.listdir(path)
    for infile in listing:
        probs = 1
        email = open(path + "/" + infile)
        #print "current file is: " + infile
        email = email.read()
        email = email.splitlines()
        for i in range(len(email)):
            boy = email[i].split(" ")
            for word in boy:
                if word in list_of_hwords:
                    index = list_of_hwords.index(word)
                    probs = probs * final_ham[list_of_hwords[index]]

        lph.append(probs)
        #print lph
    return lph


#print main1()
#print main2()
list_of_sprobs = main1()
list_of_hprobs = main2()
mark = 0
choice = []
accuracy = []
#print list_of_hprobs
#print list_of_sprobs

for i in range(len(list_of_hprobs)):
    print list_of_hprobs[i], " vs", list_of_sprobs[i]
    if list_of_hprobs[i] > list_of_sprobs[i]:
        choice.append(1)
    elif list_of_hprobs[i] < list_of_sprobs[i]:
        choice.append(0)
    else:
        choice.append(0)

print choice
for i in range(len(choice)):
    if choice[i] == 1 and i <= 19:
        accuracy.append(1)
        print " ham -----> correct"
    elif choice[i] == 0 and i > 19:
        accuracy.append(1)
        print "spam ----->  correct"
    else:
        if choice[i] == 0:
            print "spam ------> wrong"

        else:
            print "ham ------> wrong"

        accuracy.append(0)

#print accuracy

for item in accuracy:
    mark += item

mark1 = mark/float(len(accuracy))



print "The accuracy is:", mark, "/", len(accuracy),  "which is about---->", round (mark1*100, 1), "%"