#comment input 
name = str(input("Please enter name "))
d = float(input("Enter number of dependents "))
inc = float(input("Enter the gross income" ))

#process phase 
ainc = (inc - d)* 12000.00
if ainc>50000: 
  tx=ainc*0.2
else:
  tx=ainc*0.1

if tx<0:
  tx=100

#output
print("Last name: ", name)
print("The gross income: ",inc)
print("The number of dependents: ", d)
print("The adjusted gross income: ", ainc)
print("The income tax: ", tx)