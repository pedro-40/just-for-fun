s=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

sezar = s * 2


password=input("enter your password  ") 

key = int (input("key ?"))

def sezar_password():
    for i in password :

        if i ==' ' :
            print('' ,end='')
        else:
        
            u = sezar.index(i) +key
            print(sezar[u] , end='')

sezar_password()
