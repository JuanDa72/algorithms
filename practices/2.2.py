array=list(map(int, input().split()))
result=[0]*len(array)
for i in range(len(array)):
    if array[i] != 1:
        result[i] += 1
    for j in range(2, int((array[i]**0.5)+1)):

        if array[i]%j==0:
            result[i]+=j
            k = array[i] // j
            if k != j and k != array[i]:
                result[i] += k


for q in range(0, len(result)):
    if result[q]>array[q]:
        result[q]=1

    elif result[q]<array[q]:
        result[q]=-1

    else:
        result[q]=0


string=list(map(str, result))
print("\t".join(string))
