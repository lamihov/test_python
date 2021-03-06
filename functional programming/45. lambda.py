''' При создании функции def она привязывается к переменной автоматически, другие объекты (строки, числа) создаются по ходу работы без присвоения переменной.
Аналогично создаются лямбда -функции, известные как анонимные. Используются для присвоения простой функции в качестве аргумента другой функции.'''
def my_func (f, arg):
    return f(arg)
my_func(lambda x: 2*x*x, 5)

''' Функциональность лямбда - функции ограничивается одной строкой кода'''
def polynomial(x): #стандартная функция
    return x**2 + 5*x + 4
print(polynomial(-4))
print((lambda x: x**2 + 5*x + 4) (-4)) #лямбда - функция

#пример
a = (lambda x: x*x)(8)

''' Лямбда - функциям можно присваивать переменные и они могут использоваться как обычные функции.'''
double = lambda x: x * 2
print(double(7))

#пример
triple = lambda x: x*3
add = lambda x,y: x + y
print(add(triple(3),4))