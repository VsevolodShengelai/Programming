# Принимает вес в килограммах и рост в метрах. Возвращает индекс массы тела. 
def bmi(weight: float, height: float): 

    BMI = weight/((height/100) ** 2)
    return BMI

# Принимает численное значение ИМТ и печатает на экран соответствующую категорию
def print_bmi(bmi: float):
    
    if bmi < 18.5:
        print('Underweight')
    if 18.5 <= bmi < 25.0:  
        print('Normal weight')
    if 25.0 <= bmi < 30.0:
        print('Overweight')
    if 30.0 <= bmi:
        print('Obesity')


print('Индекс массы тела')
print('Введите значение массы тела (в кг) и роста (в см)')
W, L = input().split()
W = float(W)
L = float(L)
BMI = bmi(W, L)

print_bmi(BMI)
