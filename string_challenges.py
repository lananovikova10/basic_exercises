# Вывести последнюю букву в слове
word = 'Архангельск'
list_of_letters = list(word)
print(list_of_letters[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
list_of_letters = list(word)
print(list_of_letters.count('а'))

# Вывести количество гласных букв в слове
word = 'Архангёльск'
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
number_vowels=0
for letter in word:
    if letter.lower() in vowels:
        number_vowels = number_vowels+1
print(number_vowels)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()
print(words)
for word in words:
    print(word[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
one_big_word = ''
for word in words:
    one_big_word += word

average_length = sum(len(word) for word in words) / len(one_big_word)
print(average_length)