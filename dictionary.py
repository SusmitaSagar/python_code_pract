"""
built in mapping type,maps keys to values
keys = name,work,32
values= susm,student,id
no indexing in dictionary,we call from key
"""

d = {"name":'susm',"work":'student', 'online':True, 32:"id" }
for i in (d.keys()):
    print(d[i])

print(d)
print(type(d))

print(d.keys())
print(d.values())
print(d["online"])
print(d[32])
d['sports'] = 'football' # add new key and value
print(d)

#if there are repeting value of key in dictionary
d = {"name": ['susm','juhi'],"work":'student', 'online':True, 32:"id","name":'susm', 34:{"age": 55}} #new dict age
print(d.values())
#it prints line by line, pgle susm assign hoga name me , fir lily, qki variable h ye
print(type(d["name"]))
print(d[34]["age"]) # for accessing the dictionar within dictionary


d = {"name": ['susm','juhi'],"work":'student', 'online':True, 32:"id" }
print(d["name"][0]+"hi")

d.update({"hobby":"paint"})
print(d)

del d[32]
print(d)






