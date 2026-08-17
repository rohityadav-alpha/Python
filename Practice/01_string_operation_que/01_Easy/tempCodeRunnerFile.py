# 14. Find the Longest Word in a Sentence
sen="dear! rohit yadav your selected for it trichi thanks!"
# solution 1
def largest_sen(sentence):
    final=0
    wd=""
    for word in sentence.split():
        current=0
        for ch in word:
            current+=1
        if current>final:
            final=current
            wd=word
    return wd,final
print(largest_sen(sen))
# solution 2
words = sen.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest) # programming


# 15. Reverse the Order of Words in a Sentence
# solution 1 -- without using [::-1] indexing method
def rev_word(sentence):
    final_list=[]
    for word in sentence.split():
        current_word=""
        for ch in range(len(word)-1,-1,-1):
            current_word+=word[ch]
        final_list.append(current_word)
    return (" ".join(final_list))
print(rev_word(sen))
# solution 2 with [::-1] indexing method
def rev_words(sentence):
    final_list=[]
    for word in sentence.split():
        final_list.append(word[::-1])
    return (" ".join(final_list))
print(rev_words(sen))

