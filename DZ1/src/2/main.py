from json import loads, dumps
from csv import DictReader

with open('books.csv', 'r') as f:
    reader = DictReader(f)
    l = list(reader)

with open('users.json', 'r') as f:
    j = f.read()
    n = loads(j)

o=[]
for i in range(0, len(n)):
    d={}
    d['name']=n[i]['name']
    d['gender']=n[i]['gender']
    d['address']=n[i]['address']
    if i>=len(l):
        title=''
        author=''
        height=''
    else:
        title=l[i]['Title']
        author=l[i]['Author']
        height=l[i]['Height']
    d['books']={'title': title, 'author': author, 'height': height}
    o.append(d)

with open('out.json', 'w') as f:
    s = dumps(o, indent=4)
    f.write(s)

