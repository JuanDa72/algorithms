def insertion_sort_3(array:list):
    l=len(array)
    comparations=0
    for i in range(1,l):
        counter=0
        insert_index=i
        insert_value=array[i]
        flag = True

        while insert_index>0 and insert_value<array[insert_index-1]:
            flag=False
            counter+=1
            array[insert_index]=array[insert_index-1]
            insert_index-=1

        array[insert_index]=insert_value
        #Sumamos todas las comparaciones que se hacen dentro del while, no suma ni la inicial ni tampoco
        #la final en la que se sale del bucle
        comparations+=counter

        #Nos aseguramos de sumar la comparación final que se realiza cuando se sale del bucle
        if(insert_index!=0 and not(flag)):
            comparations+=1

        #Suma la única comparación para cuando no se entra en el while ya que se encunetran ordenado
        if(flag):
            comparations+=1



    return comparations

print(insertion_sort_3([12,3,7,9,14,6,11,2]))
