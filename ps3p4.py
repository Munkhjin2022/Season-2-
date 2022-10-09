#comment input 
name=input("Please enter name\n")
ca = float(input("Please enter cost of the appliance\n "))

#process phase 
if ca<=1000:
  wa=ca*0.05
else: 
  wa=ca*0.1

t = ca + wa

#output
print("Name:  ", name)
print("The cost of an appliance is:  $", ca)
print("The cost of warranty is:  $", wa)
print("Total:  $", t)

