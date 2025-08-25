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
    if num2 !=0 : 
        print(num1%num2)
    else : 
        print("تقسیم‌بر صفر امکان پذیر نیست")
elif op == '//' : 
    if num2 !=0 : 
        print(num1//num2)
    else :
        print("تقسیم بر صفر امکان پذیر نیست ")
elif op == '/' : 
    if num2 !=0 : 
        print(num1/num2)
    else :
        print("تقسیم‌بر صفر امکانپذیر نیست")
else :
    print("عملیات وارد شده معتبر نیست")
