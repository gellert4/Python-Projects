A = int(input("Give a number of seconds: "))
H = (A//3600)
M = (A//60%60)
S = (A%60)

print("This corresponds to:",H ,"hours,",M ,"minutes and",S ,"seconds.")