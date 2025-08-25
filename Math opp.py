num1 = float(input("عدد اول را وارد کنید:"))
num2 = float(input("عدد دوم را وارد کنید:"))
op = input("(+,-,*,%,//,/)عملیات")
if op == '+' : 
    print(num1 + num2)
elif op == '-' : 
    print(num1-num2)
elif op == '*' : 
    print(num1*num2)
elif op == '%' : 
    print(num1%num2)
elif op == '//' : 
    print(num1//num2)
elif op == '/' : 
    print(num1/num2)
else :
    print("عملیات وارد شده معتبر نیست")
