# a entero
a=1
print a
print "Id 'a' ",id(a), type(a)
print "Id '1' ",id(1), type(1)

# a real
a=2.5
print a
print "Id 'a' ",id(a), type(a)
print "Id '1' ",id(2.5), type(2.5)

# lista
lista=[1,2,3,4,5]
print lista
print "Id 'lista'",id(lista),type(lista)
lista.append(6)
print lista
print "Id 'lista'",id(lista),type(lista)
lista=["1","2","3","4","5"]
print lista
print "Id 'lista'",id(lista),type(lista)