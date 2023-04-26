class Course:

    def __init__(self,course_id,course_name,credit):
        self.course_id = course_id
        self.course_name = course_name
        self.credit = credit
    
    
    def getCourse_id(self):
        return self.course_id
    
    def getCourse_name(self):
        return self.course_name
    
    def getCredit (self):
        return self.credit