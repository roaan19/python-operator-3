#identity operators
m="hello football"
r="hello"

if r in m :
    print("true")
if r not in m:
    print("false")

#bitwise operator
m=10
print("right shift", m >> 1)
print("left shift " , m <<1)

#grading system 
mark1=int(input("enter the marks 1 :"))
mark2=int(input("enter the marks 2 :"))
mark3=int(input("enter the marks 3 :"))
mark4=int(input("enter the marks 4 :"))

total=mark1+mark2+mark3+mark4
average=total/4

if average >=90 and average <=100 :
    print("the grade is A")
elif average >=80 and average <=90 :
    print("the grade is B")
elif average >=70 and average<=80 :
    print("the grade is C")
else :
    print("the grade is D")