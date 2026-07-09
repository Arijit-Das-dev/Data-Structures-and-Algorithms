# Grade calculator.

# ----------- Creating grade calculator class blueprint ----------- 
class GradeCalculator:

    def __init__(self, sub1 : int, sub2 : int, sub3 : int, sub4 : int, sub5 : int):
        
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.sub4 = sub4
        self.sub5 = sub5
    
    def show_percentage(self) -> int:
        
        summ = self.sub1 + self.sub2 + self.sub3 + self.sub4 + self.sub5
        total = 500

        percentage = (summ / total) * 100

        return percentage
    
    def show_total_marks(self) -> int:

        total = self.sub1 + self.sub2 + self.sub3 + self.sub4 + self.sub5
        return total
    
    def show_grade(self):

        percentage = self.show_percentage()

        if percentage >= 90 and percentage <= 100:
            return "A+"

        elif percentage >= 80:
            return "A"

        elif percentage >= 70:
            return "B"
        
        elif percentage >= 60:
           return "C"
        
        elif percentage >= 50:
            return "D"
        
        else:
            return "F"


# ----------- Taking user input ----------- 
sub1 = int(input("Enter marks of English : "))
sub2 = int(input("Enter marks of Bengali : "))
sub3 = int(input("Enter marks of Math : "))
sub4 = int(input("Enter marks of Science : "))
sub5 = int(input("Enter marks of Computer : "))


# ----------- Creating grade calculator class object ----------- 
grade = GradeCalculator(sub1, sub2, sub3, sub4, sub5)

# ----------- Output -----------
print()
print(f"Here is your total marks : {grade.show_total_marks()}")
print(f"Here is your percentage : {grade.show_percentage()}")
print(f"Here is your grade : {grade.show_grade()}")