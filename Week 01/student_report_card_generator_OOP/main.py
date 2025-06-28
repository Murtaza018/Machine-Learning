class students:
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.grades={}
    def add_grade(self,subject,marks):
        self.grades[subject]=marks
    def calculate_average(self):
        avg=0
        for subject in self.grades:
            avg+=self.grades[subject]
        return avg/len(self.grades)
    def assign_grade(self):
        avg=self.calculate_average()
        if avg>=80:
            return "A"
        elif avg>=60 and avg<80:
            return "B"    
        elif avg>=40 and avg<60:
            return "C"
        else:
            return "F"    
    def generate_report(self):
        report=""
        report+=f"Name:{self.name}\n"
        report+=f"Age:{self.age}\n"
        report+=f"Marks:\n"
        for key in self.grades:
            report+=f"{key}:{self.grades[key]}"
        report+=f"Average:{self.calculate_average()}"    
        report+=f"Grade:{self.assign_grade()}" 
        return report   
    def save_to_tile(self,filename):  
        self.generate_report()      
    def load_from_tile(filename):        