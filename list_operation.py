words = ["python", "java", "python", "c", "python", "java"]
set_word=set(words)
word_count=[(x.upper(),words.count(x))for x in set_word]
print(word_count)



