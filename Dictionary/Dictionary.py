def MyPassion(x):
  freq = {}
  
  for i in x:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
  return freq

def maximum(freq):
  numbs=list(freq.values())
  mx=max(numbs)
  if numbs.count(mx)==len(numbs):
    return 1
  else:
    return mx

string=input("Enter a string: ")
res=string.split()
final=dict()

for i in range(len(res)):
  mod=list()
  wrd=MyPassion(res[i])
  mx=maximum(wrd)

  if(mx!=1):
    for j in wrd:
      if(wrd[j]==mx):
        mod.append(j)
  
  final[res[i]]=mod
print(final)

