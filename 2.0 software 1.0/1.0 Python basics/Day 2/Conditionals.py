# # # age=input("please what is your age?")
# # # if age > 18:
# # #     print("You can vote")
# # # else:
# # #     print("please wait for next elections")

# # Age=int(input("what is your age"))
# # if Age > 16:
# #     print("you can join the basketball team")
# # else:
# #     print("you are too young to play basketball")

# command=input("Enter 'exit' to end the program and 'continue' to keep going")
# if command=="exit":
#     print("exiting cmd")
# elif command=="continue":
#     print("continue enjoying...")
# else:
#     print("wrong command")
print("___"*50)
mark=float(input("enter your mark"))
if mark >=80:
    print("A grade")
elif mark >= 70:
    print("B+ grade")
elif mark >= 60:
    print("B grade")
elif mark >= 50:
    print("C grade")
elif mark >=40:
    print("D grade")
elif mark < 39:
    print("see you next year")
else:
    print("very poor")