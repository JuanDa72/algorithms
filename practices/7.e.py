import math

def master_theorem(a,b,d):
    "a,b,d tienen que ser enteros"
    b_d=b**d
    print(a,b,d,b_d)
    if a<b_d:
        print("Primer caso")
        if d==0:
            string=f"O(1)"

        elif d==1:
            string=f"O(n)"

        else:
            string=f"O(n^{d})"

    elif a==b_d:
        print("Segundo caso")
        nd=""
        if d==0:
            nd=f""

        elif d==1:
            nd=f"n"

        else:
            nd=f"n^({d})"

        string=f"O({nd}lg(n))"

    else:
        print("Tercer caso")
        first_part=""
        value=math.log(a, b)
        if value.is_integer():
            if value==1:
                first_part="n"
                return f"O(n)"
            
            else:
                first_part=f"n^({int(value)})"
                return f"O({first_part})"

        else:
            if b==2:
                first_part=f"(lg({a}))"
            
            else:
                first_part=f"(log_({b})({a}))"

        string=f"O(n^{first_part})"

    return string


entrada=input().split("=")[1][1::]
f=entrada.find("f")
a=entrada[0:f]
slash=entrada.find("/")+1
pare=entrada.find(")")
b=entrada[slash:pare]
c=entrada[entrada.find("^")+1:len(entrada)]

print(master_theorem(int(a),int(b),int(c)))