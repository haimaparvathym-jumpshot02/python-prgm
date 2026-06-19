# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         return f"Name:{self.name},Age:{self.age}"
    

# obj1=person("Alice", 25)
# print(obj1.display())

# class hod:
#     def __init__(self,name,dept):
#         self.name=name
#         self.dept=dept
#     def display(self):
#         return f"Name:{self.name},dept:{self.dept}"
    


# class teacher(hod):
#     def __init__(self,name1,sub,name,dept):
#         super().__init__(name,dept)
#         self.name1=name1
#         self.sub=sub
#     def teacher_display(self):
#         super().display()
#         return f"Name:{self.name},sub:{self.sub}"
    
# teacher1=teacher("Bob","Math","Alice","CS")
# print(teacher1.display())
# print(teacher1.teacher_display())




# class student:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
#     def display(self):
#         return f"Name:{self.name},roll:{self.roll}"


class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        return f"Name:{self.name},roll:{self.roll}"
class marks(student):
    def __init__(self,marks,name,roll):
        super().__init__(name,roll)
        self.marks=marks
    def marks_display(self):
        super().display()
        return f"Name:{self.name},roll:{self.roll},marks:{self.marks}"











