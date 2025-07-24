# # # # # # # # # # #loops
# # # # # # # # # # #•For loop
# # # # # # # # # # 1. starting
# # # # # # # # # # 2. condition
# # # # # # # # # # 3. increment or decrement
# # # # # # # # # names=["will","Leo", "kate", "killian", "mimbom", "nimbom" ]
# # # # # # # # # count=1
# # # # # # # # # for name in names:
# # # # # # # # #     print(f"{count}. {name}")
# # # # # # # # #     count +=1

# # # # # # # # #     # else:
# # # # # # # # #     #     print(f"Welcome to the Party: {name}")
# # # # # # # # # #Range loop
# # # # # # # # for i in range(5):
# # # # # # # #     print(i)
# # # # # # # # for i in range(2, 7):
# # # # # # # #     print(i)
# # # # # # # for i in range(0, 10, 2):
# # # # # # #     print(i)
# # # # # # for i in range(10, 0, -1):
# # # # # #     print(f"countdown: {i}")
# # # # # # print("Blast off🚀🚀")
# # # # # count = 1
# # # # # while count <= 5:
# # # # #     print(f"count is: {count}")
# # # # #     count +=1 
# # # # user_input = ""
# # # # while user_input!="quite":
# # # #     user_input= input("Enter 'quite' to exit:")
# # # #     if user_input!="quite":
# # # #         print(f"you entered: {user_input}")
# # # # print("Goodbye!")
# # # print("Finding the first even number:")
# # # for number in range(1, 10):
# # #     if number%2 ==0:
# # #         print(f"Found even number: {number}")
# # #         break
# # #     print(f"{number} is odd")
# # print("printing only odd numbers:")
# # for number in range(1, 10):
# #     if number % 2 ==0:
# #         continue
# #     print(f"Odd number: {number}")
# print("Multiplication table")
# for i in range(1, 4):
#     for j in range(1, 4):
#         result = i*j
#         print(f"{i} X {j} = {result}")

#     print()

print("Triangle pattern")
for row in range(1, 6):
    for star in range(row):
        print("*", end="")
    print()