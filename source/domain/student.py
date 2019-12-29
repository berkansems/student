import json

from source.domain.user import User


class Student(User):
    def __init__(self, name="", password="", email="", address="", contactNumber="", studentId=""):
        super().__init__(name, password, email, address, contactNumber)
        self.studentId = studentId

    def setStudentId(self, studentId):
        self.studentId = studentId

    def getStudentId(self):
        return self.studentId

    def __str__(self) -> str:
        return super().__str__() + " ,StudentId = {studentId}".format(studentId=self.studentId)

    def toJson(self):
        return json.dumps(self, default=lambda student: student.__dict__, sort_keys=True)
