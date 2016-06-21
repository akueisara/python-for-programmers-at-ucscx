#Question 1:

l = [1, 2, 3]
 
def queueadd(list,element):
    list.insert(0, element)  
 
def queueretrieve(list):
    list.pop(0)
 
queueadd(l,7)
print l
queueretrieve(l)
print l

#Question 2:

places = {'a':10,'b':5,'c':20,'d':4}
 
def closestoorigin(dictionary):
    closestkey = dictionary.keys()[0]
    closest = dictionary.values()[0]
    for x in dictionary:
        if (abs(dictionary[x]-0) < closest):
            closestkey = x
    return closestkey   
 
print "The closest place is %s" %closestoorigin(places) 