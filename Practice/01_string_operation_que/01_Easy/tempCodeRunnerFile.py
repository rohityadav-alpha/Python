sen="dear! rohit yadav your selected for nit trichi thanks!"
def largest_sen(sentence):
    final=0
    wd=""
    for word in sentence.split():
        current=0
        for j in word:
            current+=1
        if current>final:
            final=current
            wd=word
    return wd,final
print(largest_sen(sen))
print(sen.split())