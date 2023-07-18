#Напишіть програму для створення нового рядка, що складається з першого, середнього та останнього символів вхідного рядка.

#Дано: str1 = "James"
#Очікуваний результат: Jms

str1 = "James"
first_char = str1[0] # перший смивол
last_char = str1[-1] # Оостанній символ
middle_char = str1[len(str1)//2] # середній символ

new_s = first_char + middle_char + last_char

print(new_s) 
