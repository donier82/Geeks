print('Test questions about Python')
a=int(input('Enter questions counts: '))
listt=[]
for i in range(a):
    print(f'Enter {i+1} - question: ')
    b=input()
    listt.append(b)
    for i in range(3):
         print(f'Enter {i+1} - ask: ')
         c=input()
         listt.append(c)
print(listt)  
 
#    print('Enter {i}-question: ')
#b=(input('Enter n question: '))
