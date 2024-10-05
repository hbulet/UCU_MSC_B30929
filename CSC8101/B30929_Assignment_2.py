# Create a Python class named  University and in the university we have 3 FUNCTIONS
# 1. Students
# 2. Courses
# 3. Lecturers

class University:
    Name = "" # University name
    CourseLst = [] # Courses offered
    LecturerLst = [] # Available lectures
    StudentLst = [] # Available students
    
    def __init__(self, universityName):
        self.Name = universityName
    
    def Courses(self):
        return self.CourseLst

    def Lecturers(self):
        return self.LecturerLst
    
    def Students(self):
        return self.StudentLst

    def AddDetials(self, course, lecturer, student):
        if len(course) > 0:
            self.CourseLst.append(course)
        if len(lecturer) > 0:
            self.LecturerLst.append(lecturer)
        if len(student) > 0:
            self.StudentLst.append(student)

# Create University object   
myUniObj = University("Uganda Christian University")
myUniObj.AddDetials("CSC8101", "Lecturer 1", "B30929")
myUniObj.AddDetials("CSC8202", "Lecturer 2", "B30930")
myUniObj.AddDetials("RSM8101", "Lecturer 3", "B30931")
# Get object details
print("University: ", myUniObj.Name, ", Courses: ", myUniObj.Courses(), ", Lecturers: ", myUniObj.Lecturers(), ", Students: ", myUniObj.Students())
