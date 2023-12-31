#Рядок вважається симетричним, якщо обидві половини рядка однакові.
#Перевірити, чи є рядок симетричним: 

#Input: khokho
#Output:  The entered string is symmetrical

#У випадку симетрії, якщо довжина рядка парна, тоді рядок розбивається на дві половини, і виконується цикл, перевіряючи символи обох половин. 
#Якщо символи не схожі, то цикли завершується, і рядок не є симетричним, інакше рядок є симетричним.

string = input("Введіть рядок: ")
is_sym = True
if len(string) % 2 == 0:
    mid = len(string) // 2
    for i in range(mid):
        if string[i] != string[mid + i]:
            is_sym = False
            break
else:
    is_sym = False
if is_sym:
    print("The entered string is symmetrical")
else:
    print("The entered string is not symmetrical")
