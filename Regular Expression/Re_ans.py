import re

def LoveForIcecreams(s):
  words=re.findall('Butterscotch', s)
  return len(words)

def MyScottishAccent(s):
  return re.sub("o","u", s)

def LinkConsonants(s):
  searchobj = re.search( '[b-df-hj-np-tv-z] [b-df-hj-np-tv-z]',s,re.I)
  if searchobj:
    return True
  else:
    return False

def LonelyLetter(s):
  s=s.lower()
  matcher=re.compile(r'(.)\1*')
  l = [match.group() for match in matcher.finditer(s)]
  return l.count('o')


print(LoveForIcecreams('Butterscotch'))
print(LoveForIcecreams('Butterscotch Butterscotch'))


print(MyScottishAccent('hello python coders'))
print(MyScottishAccent('computer geek'))

print(LinkConsonants('Fairy Tales'))
print(LinkConsonants('Funny Faces'))
print(LinkConsonants('Thèse are crazy'))

print(LonelyLetter('Google'))
print(LonelyLetter('Robins'))
print(LonelyLetter('Smoothie'))
print(LonelyLetter('Ozone'))
