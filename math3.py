while True: 
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
    continue_program= input("(بله/خیر)ادامه میدهید؟")
    if continue_program == 'خیر' :
        print("برنامه پایان یافت،خدانگهدار")
        break