#Рядок називається паліндромом, якщо одна половина рядка є зворотною стороною іншої половини або якщо рядок виглядає однаковим при читанні вперед або назад.

#Перевірити, чи є рядок паліндромом: 

#Input:amaama
#Output: The entered string is palindrome

#У випадку паліндрому цикл виконується до середини рядка.
#Перший і останній символи мають збігатись. 
#Якщо символи не збігаються, то цикл завершується, і рядок не є паліндромом, інакше рядок є паліндромом.

string = input("Введіть рядок: ")
is_symm = True
for i in range(len(string) // 2):
    if string[i] != string[-i - 1]:
        is_symm = False
        break
if is_symm:
    print("The entered string is palindrome")
else:
    print("The entered string is not palindrome")