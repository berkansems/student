import json


class Course:
    def __init__(self, courseCode, courseName, facultyCode, startDate, endDate, staffId):
        self.courseCode = courseCode
        self.courseName = courseName
        self.facultyCode = facultyCode
        self.startDate = startDate
        self.endDate = endDate
        self.staffId = staffId

    def setStaffId(self, staffId):
        self.staffId = staffId

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

    def getStaffId(self):
        return self.staffId

    def __str__(self) -> str:
        return "courseCode={courseCode},courseName={courseName},facultyCode={facultyCode},startDate={startDate},endDate={endDate},staffId={staffId}".format(
            courseCode=self.courseCode,
            courseName=self.courseName,
            facultyCode=self.facultyCode,
            startDate=self.startDate,
            endDate=self.endDate,
            staffId=self.staffId)

    def toJson(self):
        return json.dumps(self, default=lambda course: course.__dict__, sort_keys=True)
