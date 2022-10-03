def Sort_Tuple(tup):
     
    lst = len(tup)
    for i in range(0, lst):
         
        for j in range(0, lst-i-1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j]= tup[j + 1]
                tup[j + 1]= temp
    return tup


tup= [("Dell", 5, 60000, 60000+(4/100*60000)), ("Vivo", 4, 57000, 57000+(5/100*57000)), ("HP", 459000, 459000+(6/100*459000)), ("Samsung", 3, 45000, 45000+(3/100*45000))] 


print(Sort_Tuple(tup))




print("\n\t\tOR\t\t\n")


def product():
  prod=[('Dell', 5, 60000, 0.04), ('Vivo', 4, 57000, 0.05), ('HP',4, 59000, 0.06), ('Samsung', 3, 45000, 0.03)]
  prod.sort(key = lambda x: x[2]+(x[2]*x[3]))
  return prod
product()




def Sort_Tuple(tup):
     
    lst = len(tup)
    for i in range(0, lst):
         
        for j in range(0, lst-i-1):
            if (tup[j][1] < tup[j + 1][1]):
                temp = tup[j]
                tup[j]= tup[j + 1]
                tup[j + 1]= temp
    return tup


tup= [("Dell", 5, 60000, 60000+(4/100*60000)), ("Vivo", 4, 57000, 57000+(5/100*57000)), ("HP", 459000, 459000+(6/100*459000)), ("Samsung", 3, 45000, 45000+(3/100*45000))] 


print(Sort_Tuple(tup))



print("\n\t\tOR\t\t\n")


def product():
  prod=[('Dell', 5, 60000, 0.04), ('Vivo', 4, 57000, 0.05), ('HP',4, 459000, 0.06), ('Samsung', 3, 45000, 0.03)]
  prod.sort(key = lambda x: x[2],reverse=True)
  return prod
product()


def product(prod):
  
  prod.sort(key = lambda x: x[2]+(x[2]*x[3]))
  return prod

def product2(prod):
  
  prod.sort(key = lambda x: x[2],reverse=True)
  return prod

def discount(price,tax):
  total=price+(price*tax)
  print("Total:")
  if(total>60000):
    print("Dicount of 2% applicable")
    disc=0.02*total
    total-=disc
    return total
    
  else:
    print("No discount Applicable!")
    print("Total=",total)
    return total

prod=[('Dell', 5, 60000, 0.04), ('Vivo', 4, 57000, 0.05), ('HP',4, 59000, 0.06), ('Samsung', 3, 45000, 0.03)]
print(product(prod))
print(product2(prod))

total=discount(prod[0][2],prod[0][3])
if(total!=0):
  print("Total after discount: ",total) 
else:
  print(total)






