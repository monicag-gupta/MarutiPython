# Iterating through a list
print("\nFruits:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print("\nFor : range(1,6): ")
# Using range() to generate a sequence of numbers
for i in range(1, 6):
    print(i)
print("\nFor : range(6,0,-1): ")
for i in range(6,0,-1):
    print(i)

print("\nWhile count=1 to 5: ")
# Counting using a while loop
count = 1
while count <= 5:
    print(count)
    count += 1
print("\nWhile Loop with break and continue: ")

count=0
while(count<=31):
    count = count+1
    if(count==12):
        print("12th is a holiday")
        continue;
    if(count % 7 == 1 or count % 7 == 6):
        print(count,"weekend");
    else:
        print(count,"Weekday");
    if(count==20):
        print("20th is the last working day for this month")
        break;

print("Happy Working")
    
name=""
while (True):
    print("\n\n******Menu********")
    print("1. Enter Name")
    print("2. Display Name")
    print("3. Exit")
    ans=int(input("Enter choice:"))
    if ans == 1:
        name=input("Enter Name:")
    elif ans == 2:
        print("The name is ",name)
    elif ans == 3:
        break
    else:
        print("Incorrect choice!!")
print("Menu Ends")
  
    


