#comment input 
q=float(input("Please enter a quantity of an item "))

#process phase
if q>=1000:
  up = 3.00
else: up = 5.00

ep = q * up 
tax = (ep/100) * 7
total = ep + tax 

#output 
print("Compute extended price is ", ep)
print("The tax to be 7% is ", tax)
print("The total is computed as extended price plus the tax is ", total)