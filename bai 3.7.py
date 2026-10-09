a = float(input())
b = float(input())
c = float(input())
if a==b and a==c:
    print("deu")
elif a==b or a==c or b==c:
    print("can")
elif a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a:
    print("vuong")
else:
    print("thuong")
        

    



    

