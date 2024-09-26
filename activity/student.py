# add your Student class here!

class Student:
    def __init__(self, name, grade, subjects):
        self.name = name 
        self.grade = grade
        self.subjects = subjects

    def add_class(self, new_subject):
        self.subjects.append(new_subject)
        return self.subjects
    
    def get_num_classes(self):
        return len(self.subjects)
    
    def summary(self):
        pass
        #print (f"{self.name} is a {self.grade} enrolled in {self.get_num_classes()} classes")
