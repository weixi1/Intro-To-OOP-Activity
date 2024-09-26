# add your get_student_with_more_classes function here!
from activity.student import Student

def get_student_with_more_classes(student1, student2): 

    if student1.get_num_classes() > student2.get_num_classes():
        print (student1.name)
    else:
        print (student2.name)