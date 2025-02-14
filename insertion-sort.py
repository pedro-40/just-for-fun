
a = [3 ,5 ,2 ,7 ,1 ,4 ,8 ,6 ,9 ,12 ,15 ,10 ,17 ,13 ,11 ,16 ,18 ,14 ,19 ,25 ,22 ,28 ,24 ,21 ,20 ,23 ,26 ,29 ,27 ,30 ,]

def insertion (a) :
     
    for i in range(1 , len(a)) :
          
        key = a[i]
        j = i-1


        while j>= 0 and key < a[j] :
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        print(key)
    print(a)

    
  
  



insertion(a)