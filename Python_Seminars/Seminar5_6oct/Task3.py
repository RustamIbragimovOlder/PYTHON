# Напишите программу, удаляющую из текста все слова, содержащие "абв".

# 1. Мой вариант 1

text = 'Абвгде-йка, абвгде-йка! Это учеба или игра?'
print(text)

def remove_words_text(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

print(remove_words_text(text))

# 2. Мой вариант 2

text = 'qwerty абв рабв нет да, 12345 АБВ хватит неабв'
print(text)
print(" ".join(list(filter(lambda x: 'абв' not in x, text.split()))))

