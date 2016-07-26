import re
import time
start_time = time.time()

def get_words(text):
    return re.compile('\w+').findall(text.lower())

def edit_distance(str1, str2):
    str1 = ' ' + str1
    str2 = ' ' + str2
    d = {}
    x = len(str1)
    y = len(str2)

    for i in range (x):
        d[i,0] = i
    for j in range (y):
        d[0,j] = j
    for j in range(1,y):
        for i in range(1,x):
            if str1[i] == str2[j]:
                d[i, j] = d[i-1, j-1]
            else:
                d[i, j] = min(d[i-1, j], d[i, j-1], d[i-1, j-1]) + 1;
    return d[x-1, y-1]

words = file('words.txt').read()
words_list = get_words(words)

def min_edit_distance(query):
    query = query.lower()
    my_dict = {}
    for i in range (len(words_list)):
        result = edit_distance(query, words_list[i])
        my_dict[words_list[i]] = result
    return min(my_dict, key=my_dict.get)

if __name__ =='__main__':
    result = min_edit_distance('Masal')
    print(result)
    print("--- %s seconds ---" % (time.time() - start_time))
