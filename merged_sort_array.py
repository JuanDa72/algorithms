def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    counter = 0
    while (counter < m):
        print("Volvimos aquí")
        flag=False
        position=0
        if(n>0):
            for i in range(n):
                #print("el valor de n2 es " + str(nums2[i]))
                #print("El valor de n1 es"+ str(nums1[counter]))

                if(nums1[counter]<=nums2[i]):

                    if not(flag):
                        print("Primero menor")
                        counter += 1
                        break

                    else:
                        register=nums1[counter]
                        nums1[counter]=nums2[position]
                        nums2.pop(position)
                        nums2.insert(i-1, register)
                        counter+=1
                        print("Counter cambio a "+str(counter))
                        print("Nums 1 es " + str(nums1))
                        print("Nums 2 es " + str(nums2))
                        break



                else:
                    if not(flag):
                        position=i
                        flag=True



        if(flag and counter<m):
            print("Entro aquí xd")
            register=nums1[counter]
            nums1[counter]=nums2[position]
            nums2.pop(position)
            nums2.append(register)
            counter+=1
            print("Nums 1 es " + str(nums1))
            print("Nums 2 es " + str(nums2))

        else:
             break

    nums1[m:]=nums2[:]
    print(nums1)




merge([0,0,3,0,0,0,0,0,0],3, [-1,1,1,1,2,3], 6)