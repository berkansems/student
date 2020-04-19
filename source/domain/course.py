import json


# unitPrice,totalHour
class Course:
    def __init__(self, courseCode=None, courseName=None, facultyCode=None, startDate=None, endDate=None, unitPrice=None,
                 totalHour=None):
        self.courseCode = courseCode
        self.courseName = courseName
        self.facultyCode = facultyCode
        self.startDate = startDate
        self.endDate = endDate
        self.unitPrice = unitPrice
        self.totalHour = totalHour

    def setUnitPrice(self, unitPrice):
        self.unitPrice = unitPrice

    def getUnitPrice(self):
        return self.unitPrice

    def setTotalHour(self, totalHour):
        self.totalHour = totalHour

    def getTotalHour(self):
        return self.totalHour

    def setCourseCode(self, courseCode):
        self.courseCode = courseCode

    def setCourseName(self, courseName):
        self.courseName = courseName

    def setFacultyCode(self, facultyCode):
        self.facultyCode = facultyCode

    def setStartDate(self, startDate):
        self.startDate = startDate

    def setEndDate(self, endDate):
        self.endDate = endDate

    def getCourseCode(self):
        return self.courseCode

    def getCourseName(self):
        return self.courseName

    def getFacultyCode(self):
        return self.facultyCode

    def getStartDate(self):
        return self.startDate

    def getEndDate(self):
        return self.endDate

    def __str__(self) -> str:
        return "courseCode={courseCode},courseName={courseName},facultyCode={facultyCode},startDate={startDate},endDate={endDate}".format(
            courseCode=self.courseCode,
            courseName=self.courseName,
            facultyCode=self.facultyCode,
            startDate=self.startDate,
            endDate=self.endDate)

    def toJson(self):
        return json.dumps(self, default=lambda course: course.__dict__, sort_keys=True)
