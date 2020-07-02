def file_to_list(path):
    #completeName = r"C:\Users\josef\Desktop\exjobb-NLP\\" + filename + ".txt"
    completeName = path
    f = open(completeName, "r")
    vocab_list = []
    while True:
        word = f.readline()
        vocab_list.append(word.rstrip())
        if not word:
            break
    f.close()
    return vocab_list


#read_file("bad-words")
#read_file("google-10000-english-usa")
#read_file("vocab") #this contains 3000 english words plus 1300 bad words
#dict_to_list()
#print(lst)

#big_vocab = file_to_list(r"C:\Users\josef\Desktop\exjobb-NLP\big_vocab.txt")
#big_vocab.sort(key=len)
#print(big_vocab[10000:15000])
