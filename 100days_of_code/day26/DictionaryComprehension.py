"""new_dict ={new_key:new_value for item in list}
    new_dict ={new_key:new_value for (key,value) in dict.item()}
    new_dict ={new_key:new_value for (key,value) in dict.item() if test}
    """
    

import random


names = ['subham','babulu','chiku','sipu','nikhil','ajit']
student_score={student:random.randint(1,100) for student in names}
print(student_score)

pass_student = {student:score for (student,score) in student_score.items() if score>60}
print(f"pass_student:{pass_student}")

