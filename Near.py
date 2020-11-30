def near(word1, word2):
    wordOne = list(word1)
    wordTwo = list(word2)
    isTrue = False

    # Checks if the length of the first word is bigger than the second word
    if len(wordOne) > len(wordTwo):
    
    # For each letter in 'word1' take it out and see if the words are equal
        for i in range(0,len(wordOne)):
            word1Temp = list(word1)
            word1Temp.pop(i)
            if word1Temp == wordTwo:
                isTrue = True
                break
            else:
                isTrue = False
            
    else:
        isTrue = False
    
    print(isTrue)

near("reset", "rest")
near("dragoon", "dragon")
near("eave", "leave")
near("sleet", "lets")