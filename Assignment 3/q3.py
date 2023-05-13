import re
files = int(input("Enter number of files: "))

for i in range(1,files+1):
    print("FILE no.",i)
    file_name = "q3FILE" + str(i) + ".txt"
    
    word_freq = {} #reset to empty dict for each iteration
    #shows indiv count of each word in file-but contains punctuations also!!
   
    with open(file_name, "r") as f:
        s = f.readlines()
        for i in range(s.count('\n')):
            s.remove('\n')
        lines = len(s)
    ctr = 0
    # f3sentencectr = 0  #counts no. of sentences w >35 words or < 5 words
    # for i in s:
    #     sentences = i.split('.') 
    #     # print(sentences[0])
    #     if len(sentences[0]) > 35 or len(sentences[0]) < 5:
    #         f3sentencectr += 1
    # print('Total Number of sentences with >35 words or < 5 words :',
    #     f3sentencectr)   
        
    print("TOtal sentences =", lines) #total sentences count


    def count_sentences(file_name): #func to calc indiv long & short sentences, & also replacing
        #multiple punctuations. using re librarhy
        with open(file_name, 'r') as f:
            r = f.read()
            # replace multiple punctuation with a single '.'
            r = re.sub(r'[.!?]+', '.', r) 
            sentences = r.split('.') # split the r by sentences
            long_sentences = 0
            short_sentences = 0
            for sentence in sentences:
                sentence = sentence.strip()
                words = sentence.split()
                if len(words) > 35:
                    long_sentences += 1
                elif len(words) < 5 and len(words)>0:
                    short_sentences += 1
            return long_sentences, short_sentences

    long_sentences, short_sentences = count_sentences(file_name)
    print("Number of long sentences:", long_sentences)
    print("Number of short sentences:", short_sentences)
    f3sentencectr=long_sentences+short_sentences

    print('Total Number of sentences with >35 words or < 5 words :',f3sentencectr)

    
    for i in s:
        words = i.split()
        for word in words:
            ctr += 1
            if word.lower() in word_freq:
                word_freq[word.lower()] += 1     
            else:
                word_freq[word.lower()] = 1
            
    # count the number of consecutive punctuations
    with open(file_name, "r") as f:
        r = f.read()
    comma_count = len(re.findall(",{2,}", r))# no. of consecutive comma occurrences (min of 2) in r.

    fullstop_count = len(re.findall("\.{2,}", r))# no. of consecutive fullstop occurr (min of 2) in r.
    colon_count = len(re.findall(":{2,}", r))# no. of consecutive colon occ(min of 2) in r.
    semicolon_count = len(re.findall(";{2,}", r))# no. of consecutive semicolon occ (min of 2) in r.
  
    print()
    print("Number of consecutive commas:", comma_count)
    print("Number of consecutive full stops:", fullstop_count)
    print("Number of consecutive colons:", colon_count)
    print("Number of consecutive semicolons:", semicolon_count)
    print()


    with open(file_name, "r") as input_file:
        contents = input_file.read()

    # Remove all extra commas and full stops
    correct_punct = re.sub(r"[,.]+", "", contents)

    with open("output.txt", "w") as output_file:
        output_file.write(correct_punct)

    with open("output.txt", 'r') as file:
        # s_new=file.readlines()
        import string
        contents = file.read()
        # Remove punctuation
        #removes all punctuation from string contents using translate() method. str.maketrans("", "", string.punctuation) 
        # creates a translation table that maps every punct character in string.punctuation to None.
        contents = contents.translate(str.maketrans("", "", string.punctuation))
        words = contents.lower().split()
        # print(words)
        word_count = {}  # dict to store word freq
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        print()

        print("Word count =",word_count)
        # for word, frequency in word_count.items():
        #     print(f"{word}: {frequency}")
        print()

    print("Here punctuation HAS NOT been removed=",word_freq)
    print()

    print("Here punctuation HAS been removed=",word_count)
    print()

    unique_words=[]
    for i in word_count.keys():
        if word_count[i]==1:
            unique_words.append(i)
    print("LIST OF UNIQUE WORDS =",unique_words)
    a=len(unique_words)
    print()
    print("No. of unique_words =",a)
    print("Total words =",ctr)
    print()

    l = sorted(word_count.items(), key=lambda item: item[1],reverse=True)
    print("SORTED LIST OF TUPLES WITH WORD AND ITS COUNT =",l)
    occ_top5=0 #total occurrences the top 5 most occurring words
    for i in range(5):
        occ_top5 +=l[i][1]
    print()
    print("total occurrences the top 5 most occurring words =",occ_top5)

    F1 = (a/ctr)  #ctr=total no. of words, a=no of unique words
    F2 = (occ_top5/ctr) 
    F3= f3sentencectr/(lines)
    F4= (comma_count+fullstop_count+colon_count+semicolon_count)/ctr
    if ctr>750:
        F5=1
    else:
        F5=0
    netscore= 4 + F1*6 + F2*6 -F3 - F4 - F5
    print()

    print("Net score =",netscore)
    print("\n")


    #output
    import random
    with open("scores.txt", "a") as f:
        f.write(file_name+"\n")  # write the filename
        f.write("score: {}\n".format(netscore))  # write the score
        f.write("Five most used words: ")
        for i in range(5):
            f.write("{} ".format(l[i][0]))
        f.write("\n")
        f.write("Five randomly selected words: ")
        random_words = random.sample(words, 5)
        for word in random_words:
            f.write("{} ".format(word))
        f.write("\n")


