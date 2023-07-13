number=int(input("enter number of students:"))
sum=float(0.0)
max=0.0
for i in range(1,number+1):
  grade=float(input("please enter grade of "+str(i)+ "  of student:"))
  sum+=grade
  if grade>max:
   max=grade
   ## elif grage<min:
   ##min=grade
   ### برای محاسبه ی همزمان ماکزیمم و مینیمم از لیست (آرایه)باید استفاده کرد
average=sum/number
print("average",average)
print("max:",max)
##print("min:",min)
 



 
 