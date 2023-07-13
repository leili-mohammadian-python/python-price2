number=int(input("enter number of students:"))
sum=float(0.0)
average=float(0.0)
list=[]
for i in range(1,number+1):
  grade=float(input("please enter grade of "+str(i)+ "  of student:"))
  list.append(grade)
  sum+=grade
average=sum/i
print("average:",average)
print("max:",max(list))
print("min:",min(list))
  