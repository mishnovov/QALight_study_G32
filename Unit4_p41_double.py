#Використовуючи словник, видалити всі дублі слів з даного речення: 
#Python is great and Java is also great
#Потрібно отримати: Python is great and Java also

sentence = "Python is great and Java is also great"
words = sentence.split()  # Розбиваємо речення на слова

# Створюємо словник
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# нове речення
new_sentence = " ".join([word for word in words if word_count[word] == 1])

print(new_sentence)





