mydict = {"hello" : "world", "speckbit" : "self-learning", "life" : "meaning"}

n = input("Enter the value:")

for i,j in enumerate(mydict):
	if mydict[j]==n:
		print("Key =",j)
  
