import math
def func(a,b,c):
    delta=b*b-4*a*c
    if a==0:
        if b==0:
            if c==0:
                print(5)
            else:
                print(4)
        else:
            print(6)
            print(f"{(-c/b):.2f}")
    else:
        if delta==0:
            print(2)
            print(f"{(-b/(2*a)):.2f}")
        elif delta>0:
            print(1)
            print(f"{(-b-math.sqrt(b*b-4*a*c))/(2*a):.2f}"," ",f"{(-b+math.sqrt(b*b-4*a*c))/(2*a):.2f}")
        else:
            print(3)
    print('\n')

a,b,c=list(input().split())
func(float(a),float(b),float(c))