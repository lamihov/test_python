'''объект none предназначен для указания отсутствия значений. В языках программирования ипользуется null. 
Как и другие пустые значение (0; []; пустые строки) объеки None возвращает False при преобразовании в логическую переменную'''
None == None
print(None)
#объект None возвращается функцией которая не запрограммирована что-либо возвращать
def some_func():
    print("Hi!")
var = some_func()
print(var)
#пример
foo = print()
if foo == None:
    print(1)
else:
    print(2)