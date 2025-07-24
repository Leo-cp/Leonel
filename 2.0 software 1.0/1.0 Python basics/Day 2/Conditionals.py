# # # # # age=input("please what is your age?")
# # # # # if age > 18:
# # # # #     print("You can vote")
# # # # # else:
# # # # #     print("please wait for next elections")

# # # # Age=int(input("what is your age"))
# # # # if Age > 16:
# # # #     print("you can join the basketball team")
# # # # else:
# # # #     print("you are too young to play basketball")

# # # command=input("Enter 'exit' to end the program and 'continue' to keep going")
# # # if command=="exit":
# # #     print("exiting cmd")
# # # elif command=="continue":
# # #     print("continue enjoying...")
# # # else:
# # #     print("wrong command")
# # print("___"*50)
# # mark=float(input("enter your mark"))
# # if mark >=80:
# #     print("A grade👌")
# # elif mark >= 70:
# #     print("B+ grade")
# # elif mark >= 60:
# #     print("B grade")
# # elif mark >= 50:
# #     print("C grade")
# # elif mark >=40:
# #     print("D grade")
# # else:
# #     print("very poor")
# #simple calculator
# first_number=float(input("Enter first number: "))
# second_number=float(input("enter second number: "))
# operator=input("enter operator")
# result=0
# if operator=="+":
#     result=first_number + second_number
#     print(f"results is: {result}")
# elif operator=="-":
#     result=first_number - second_number
#     print(f"results is: {result}")
# elif operator== "*":
#     result=first_number * second_number
#     print(f"results is: {result}")
# elif operator=="/":
#     if second_number!=0:
#     result=first_number / second_number
#     print(f"results is: {result}")
#     else:
#        print("error")
# else:
#     print("Synthax error")
year=int(input("enter the year"))
if year%4==0:
    print(f"{year}  is a leap year")
elif year%100==0:
    print(f"{year} is not a leap year")
elif year%400==0:
    print(f"{year} is a leap year")
else:
    print("it is not a leap year")