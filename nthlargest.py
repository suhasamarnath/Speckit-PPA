l=[]
d=int(input("Enter the number of elements needed into the list: "))
for i in range(1,d+1):
   m=int(input("Ënter the numbers:"))
   l.append(m)
print(l)


def n_largest(largest):
   l.sort()
   print(f"The {largest} largest number is {l[-largest]}")



while(True):
   ch=input("Do you want to continue? y/n:")
   if ch == 'y':
      largest=int(input("Enter the nth largest number needed:"))
      n_largest(largest)
   elif ch == 'n':
      print("Thank you for visiting.")
      break  