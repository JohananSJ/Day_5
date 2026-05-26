sentence = input("Enter a sentence: ")
words = sentence.split()
print("\nNumber of words:", len(words))
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("\nWord Frequency:")
print(word_count)