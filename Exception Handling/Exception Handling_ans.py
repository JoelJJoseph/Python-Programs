def validate(dob):
  l = dob.split("/")
  d = int(l[0])
  m = int(l[1])
  y = int(l[2])
  if d == 0 or m > 12 or m ==0 : 
    return 0   #invalid date case
  elif m == 2:  #invalid cases for a debruary date
    if y % 100 == 0 and y % 400 != 0 and d > 29: 
      return 0  #leap year rule exceptions
    elif y%4 == 0 and d > 29:
      return 0  #leap year
    elif d > 28 and d != 29: 
      return 0
  elif (m == 4 or m == 6 or m == 9 or m ==11) and (d > 30): 
    return 0 #months with dates limited to 30
  else: 
    return 1


z = { 1:"positiveAries", 
     2:"positiveTaurus",
     3:"positiveGemini",
     4:"positiveCancer",
     5:"positiveLeo",
     6:"positiveVirgo",
     7:"positiveLibra",
     8:"positiveScorpius",
     9:"positiveSagittarius",
     10:"positiveCapricorn",
     11:"positiveAquarius",
     12:"positivePisces"
}
def zodiac(dob):
  ds = dob.split("/")
  dl = [int(x) for x in ds]
  if (dl[1] == 3 and dl[2]>=21) or (dl[1] == 4 and dl[2]<=19):
    print(z[1])
  elif (dl[1] == 4 and dl[2]>=20) or (dl[1] == 5 and dl[2]<=20):
    print(z[2])
  elif (dl[1] == 5 and dl[2]>=21) or (dl[1] == 6 and dl[2]<=21):
    print(z[3])
  elif (dl[1] == 6 and dl[2]>=22) or (dl[1] == 7 and dl[2]<=22):
    print(z[4])
  elif (dl[1] == 7 and dl[2]>=23) or (dl[1] == 8 and dl[2]<=22):
    print(z[5])
  elif (dl[1] == 8 and dl[2]>=23) or (dl[1] == 9 and dl[2]<=22):
    print(z[6])
  elif (dl[1] == 9 and dl[2]>=23) or (dl[1] == 10 and dl[2]<=23):
    print(z[7])
  elif (dl[1] == 10 and dl[2]>=24) or (dl[1] == 11 and dl[2]<=21):
    print(z[8])
  elif (dl[1] == 11 and dl[2]>=22) or (dl[1] == 12 and dl[2]<=21):
    print(z[9])
  elif (dl[1] == 12 and dl[2]>=22) or (dl[1] == 1 and dl[2]<=19):
    print(z[10])
  elif (dl[1] == 1 and dl[2]>=20) or (dl[1] == 2 and dl[2]<=18):
    print(z[11])
  elif (dl[1] == 2 and dl[2]>=19) or (dl[1] == 3 and dl[2]<=20):
    print(z[12])



i=1
while(i):
  dob = input("Input: ")
  if dob == '?':
    print("Input should be (dd/mm/yyyy) format or q/Q to quit")
  elif dob == '':
    print("A positive quality")
  elif dob == 'q' or dob == 'Q':
    raise TypeError("Bye! Hope you run this program again")
  else:
    try:
      if validate(dob):
        zodiac(dob)
      else:
        raise NameError
    except: print("Invalid input. run again")