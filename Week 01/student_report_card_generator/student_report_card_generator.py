def calculate_avg(marks_dict):
    avg=(int(marks_dict["English"])+int(marks_dict["Math"])+int(marks_dict["Urdu"]))/3
    return avg


name=input("Enter name:")
age=input("Enter age:")
marks={}
marks["English"]=input("Enter marks for english:")
marks["Math"]=input("Enter marks for math:")
marks["Urdu"]=input("Enter marks for urdu:")

option=input("Add 5 bonus marks to all subjects?(yes/no):")

if option.lower()=="yes":
    marks["English"]+=5
    marks["Math"]+=5
    marks["Urdu"]+=5

avg=calculate_avg(marks)
avg=round(avg,2)
if avg>=80:
    grade="A"
elif avg>=60 and avg<80:
    grade="B"    
elif avg>=40 and avg<60:
    grade="C"
else:
    grade="F"        

with open("report.txt","w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Age: {age}\n")
    f.write(f"Math: {marks["Math"]}\n")
    f.write(f"English: {marks["English"]}\n")
    f.write(f"Urdu: {marks["Urdu"]}\n")
    f.write(f"Average: {avg}\n")
    f.write(f"Grade: {grade}\n")
    
with open("report.txt","r") as f:
    data=f.readlines()
print("Report:")
for line in data:
    print(line.strip())    