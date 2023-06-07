class school:

    school_name = "Edyoda"  

    def __init__(self,rno,name):
        self.rno = rno
        self.name = name

    def display(self):
        print(f"Roll No. : {self.rno} \nName : {self.name} \nSchool Name : {school.school_name}")

    @classmethod
    def get_school_name(cls):
        return cls.school_name
    
    @classmethod
    def set_school_name(cls,s_name):
        cls.school_name = s_name

obj = school("Abi",1)
obj.display()
obj = school("Bharathi",2)
obj.display()
obj = school("shanthini",3)
obj.display()


