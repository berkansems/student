class CourseViewModelInsertion:
    def __init__(self, courseCode=None, courseName=None, facultyCode=None, startDate=None, endDate=None, staffId=None,
                 unitPrice=None, totalHour=None
                 ):
        self.courseCode = courseCode
        self.courseName = courseName
        self.facultyCode = facultyCode
        self.startDate = startDate
        self.endDate = endDate
        self.staffId = staffId
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


class CourseViewModelUpdate:
    def __init__(self, courseCode=None, courseName=None, facultyCode=None, startDate=None, endDate=None):
        self.courseCode = courseCode
        self.courseName = courseName
        self.facultyCode = facultyCode
        self.startDate = startDate
        self.endDate = endDate

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
            endDate=self.endDate,
        )


class CourseViewModelDeletion:
    def __init__(self, courseCode):
        self.courseCode = courseCode

    def setCourseCode(self, courseCode):
        self.courseCode = courseCode

    def getCourseCode(self):
        return self.courseCode


class CourseViewModel:
    def __init__(self, courseCode=None, courseName=None, facultyCode=None, startDate=None, endDate=None,
                 professorList=None):
        self.courseCode = courseCode
        self.courseName = courseName
        self.facultyCode = facultyCode
        self.startDate = startDate
        self.endDate = endDate
        self.professorList = professorList

    def setProfessorList(self, professorList):
        self.professorList = professorList

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

    def getProfessorList(self):
        return self.professorList

    def __str__(self) -> str:
        return "courseCode={courseCode},courseName={courseName},facultyCode={facultyCode},startDate={startDate},endDate={endDate},professorList={professorList}".format(
            courseCode=self.courseCode,
            courseName=self.courseName,
            facultyCode=self.facultyCode,
            startDate=self.startDate,
            endDate=self.endDate,
            professorList=self.professorList
        )


class CourseViewModelCode:
    def __init__(self, courseCode=None):
        self.courseCode = courseCode

    def setCourseCode(self, courseCode):
        self.courseCode = courseCode

    def getCourseCode(self):
        return self.courseCode


class CourseViewModelStudentInsertion:

    def __init__(self, studentId=None, courseCode=None):
        self.studentId = studentId
        self.courseCode = courseCode

    def setStudentId(self, studentId):
        self.studentId = studentId

    def getStudentId(self):
        return self.studentId

    def setCourseCode(self, courseCode):
        self.courseCode = courseCode

    def getCourseCode(self):
        return self.courseCode


class CourseViewModelEnrollmentCourseByStudentId:

    def __init__(self, studentId=None):
        self.studentId = studentId

    def setStudentId(self, studentId):
        self.studentId = studentId

    def getStudentId(self):
        return self.studentId


class CourseViewModelEnrollmentProfessorByStaffId:

    def __init__(self, staffId=None):
        self.staffId = staffId

    def setStaffId(self, staffId):
        self.staffId = staffId

    def getStaffId(self):
        return self.staffId


class CourseViewModelDropCourse:

    def __init__(self, courseCode=None, studentId=None):
        self.courseCode = courseCode
        self.studenId = studentId

    def setStudentId(self, studentId):
        self.studenId = studentId

    def getStudentId(self):
        return self.studenId

    def setCourseCode(self, courseCode):
        self.courseCode = courseCode

    def getCourseCode(self):
        return self.courseCode
