amu = raw_input()
words = amu.split(" ") 
newWords = [word[::-1] for word in words] 
newSentence = " ".join(newWords)
print(newSentence) 
