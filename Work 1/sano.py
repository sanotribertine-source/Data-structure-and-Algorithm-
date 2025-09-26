#integer
quantities=[200,10,30,90,130,140]
total_quantities=round(sum(quantities))
avg_quantities=round(total_quantities/len(quantities))
max_quantities=round(max(quantities))
min_quantities=round(min(quantities))
print("The quantities are:",quantities)
print("total quantities are:",total_quantities)
print("average quantities are:",avg_quantities)
print("max quantity is:",max_quantities)
print("min quantity is:",min_quantities)

#string
quantities=[200,10,30,90,130,140]
total_quantities=round(sum(quantities))
avg_quantities=round(total_quantities/len(quantities))
print("The number of quantities are:",len(quantities))
print("total quantities are:",total_quantities)
print("average quantities are:",avg_quantities)

#boolean
quantities=[200,10,30,90,130,140]
threshold=100
c=1
for c in quantities :
    if c >= threshold:
        print(f"the quantities{c} is: Above Standard")
    else:
        print(f"the quantities{c} is: Below Standard")

#list
quantities=[200,10,90,130,30,140]
print("This is the list before any operation:",quantities)
quantities.append(55)
quantities.append(43)
c=1
for c in quantities:
    if c >=101:
        quantities.remove(c)
print("This is the list after any operation:",quantities)
quantities.sort()
print("The final list after sorting:",quantities)

#arrays
quantities=[200,10,90,130,30,140]
arrr=(10,200,140)
print("array data:",arrr)
array_sum=sum(arrr)
list_sum=sum(quantities)
print(f"array sum is {array_sum}")
print(f"list_sum is {list_sum}")
if array_sum==list_sum:
    print("array sum equals list_sum")
else:
    print("array sum does not equal list_sum")

#dictionary
records=[{"id": 1, "name": "Claim1", "value": 120},
         {"id": 2, "name": "Claim2", "value": 90},
         {"id": 3, "name": "Claim3", "value": 80},]

records[1]["value"]=100 #update record
records.pop(0) #remove record
total_value=sum(r["value"] for r in records)
print("Total value across records:",total_value)
avg_value=total_value/len(records)
if avg_value>120 and len(records)>=2:
    print("the average value is Above Standard")
else:
    print("the average value is Below Standard")