
student_height = input().split( )
total_height = 0 
for height in student_height:
    total_height += int(height)
print(f"total height = {total_height}")

number_of_students = 0 
for students in student_height:
    number_of_students +=1
print(f"number of students = {number_of_students}")

average_height = round(total_height/number_of_students)
print(f"average height = {average_height}")


                # OR
                
# student_height = input().split( )
# # print(student_height)
# total_height = 0
# for n in range(0,len(student_height)):
#     student_height[n] = int(student_height[n])
#     total_height  =total_height + int(student_height[n])
# print(f"total_height = {total_height}")
# print(f"number of students = {len(student_height)}")
# print(f"average height = {int(total_height/len(student_height))}")


