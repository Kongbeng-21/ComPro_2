class Score:
    def __init__(self, name: str, score: float,):
        self.name = name
        self.score = score
        self.grade = self.calculate_grade()
        
        
    def calculate_grade(self) -> str:
        if 90 <= self.score <= 100:
            grade = "A"
        elif 80 <= self.score < 90:
            grade = "B"
        elif 70 <= self.score < 80:
            grade = "C"
        elif 60 <= self.score < 70:
            grade = "D"
        else:
            grade = "F"
        return grade
            
    def get_info(self,grade) -> str:
        return f"Name: {self.name}, Score: {self.score:.2f}, Grade: {grade}"
    

name = input("Enter name: ")
try:
    score = float(input("Enter score: "))


    s = Score(name,score)
    if 0 > score or score > 100:
        print("Invalid score")


    else:
        grade = s.calculate_grade()
        print(s.get_info(grade))
except ValueError:
    print("Invalid score")
        
    