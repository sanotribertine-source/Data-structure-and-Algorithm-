stack1=[] #declaration of stack
stack1.extend(["K","I","N","S","H","A","S","A"]) #adding items in the stack
print("Stack before reverse:",stack1)
stack1_reverse=[]
while stack1: # used while for reversing the stack
    next_word=stack1.pop()
    stack1_reverse.append(next_word)
print("Stck after reverse:",stack1_reverse)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#we use the list as circular queue
queue2=[]
buses =["bus-1","bus2","bus3"]
print("initial bus in queue2:",buses)

#we release the first bus (front of queue)
dispatched = buses.pop()
print("dispatched bus in queue2:",dispatched)
dispatched_buses=[0]
#when we add a bus
buses.append("bus1")
print("new bus in queue2:",buses)
#released next bus
released =buses.pop(0)
print("dispatched bus in queue2:",dispatched)
print("new bus in queue2:",buses)
#that bus also return to the end
buses.append(released)
print("bus return and added back:",buses)

#keep looping this way forever





