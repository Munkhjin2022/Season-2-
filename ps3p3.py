#comment input
n = float(input("Please enter the number of book "))
cpb = float(input("Please enter cost of per book "))

#process phase 
t= n * cpb
if t<=50: 
  sh=25
else:
  sh=0

#output
print("The order total:  $",t)
print("Shipping:  $ ",sh)
