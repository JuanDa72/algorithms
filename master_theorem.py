import math


def es_entero(number: float):
    entero = int(number)
    if (number - entero) == 0:
        return True
    else:
        return False


expression = input().split()
print(expression)

a=int(expression[2].split("f")[0])
print(a)

#Adquisición de b
intemediary_b=expression[2].split("n/")
b=int(intemediary_b[1].split(")")[0])
print(b)

#Adquisicion de c
c=int(expression[2].split("^")[1])
print(c)


k: float = math.log(a,b)
print(k)

string1=""
#aplicación del metodo maestro
if(k>c):
    string1=f"O(n^(log_({b})({a})))"
    print("String 1 es "+string1)

elif (k<c):
    string1=f"O(n^{c})"

else:
    string1=f"O(n^log_({b})({a})lg^_({int(1)})(n))"


if es_entero(k):
    #print("string 1 es "+" "+string1)
    string1=string1.replace(f"log_({b})({a})",f"{int(k)}")
    string1=string1.replace(f"lg({a})",f"{k}")
    #string1.replace(f"")
    print("string final "+string1)

string1=string1.replace("n^(0)", "1")
string1=string1.replace("n^(1)", "n")
string1=string1.replace("n^0", "1")
string1=string1.replace("n^1", "n")
string1=string1.replace("log_(2)",f"lg")
string1=string1.replace("1l","l")
string1=string1.replace("^_(1)","")


print(string1)







