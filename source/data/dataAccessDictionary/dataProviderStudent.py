

from source.domain.student import Student


class DataProviderStudent:
    studentList = None

    def __init__(self):
        global studentList
        studentList = dict()


    def insert(self, student):
        global studentList
        studentList[student.getStudentId()] = student
        return True

    def update(self, student):
        global studentList
        for studentId, studentInfo in studentList.items():
            if studentId == student.getStudentId():
                currentStudent = Student()
                currentStudent.setStudentId(student.getStudentId())
                currentStudent.setName(student.getName())
                currentStudent.setEmail(student.getEmail())
                currentStudent.setAddress(student.getAddress())
                currentStudent.setContactNumber(student.getContactNumber())
                currentStudent.setPassword(student.getPassword())
                studentList[studentId] = currentStudent
                return True
        return False

    def delete(self, id):
        global studentList
        for studentId, studentInfo in studentList.items():
            if studentId == id:
                del studentList[id]
                return True
        return False

    def getList(self) -> dict:
        global studentList
        return studentList

    def getById(self, id):
        global studentList
        for studentId, studentInfo in studentList.items():
            if studentId == id:
                currentStudent = Student()
                currentStudent.setStudentId(studentInfo.getStudentId())
                currentStudent.setName(studentInfo.getName())
                currentStudent.setEmail(studentInfo.getEmail())
                currentStudent.setAddress(studentInfo.getAddress())
                currentStudent.setContactNumber(studentInfo.getContactNumber())
                currentStudent.setPassword(studentInfo.getPassword())
                # currentStudent = studentInfo
                return currentStudent
        return False
