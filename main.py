import pandas

df = pandas.read_csv("morse_code.csv")
new_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(new_dict)

word = input("Enter a word: ").upper()
translated_word = [str(new_dict[letter]) for letter in word]
listToStr = ' '.join([str(elem) for elem in translated_word])
print(listToStr)
