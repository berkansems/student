import json

from source.domain.user import User


class Professor(User):
    def __init__(self, name="",
                 password="",
                 email="",
                 address="",
                 contactNumber="",
                 staffId="",
                 salary="",
                 department=""):
        super().__init__(name, password, email, address, contactNumber)
        self.staffId = staffId
        self.salary = salary
        self.department = department

    def setStaffId(self, staffId):
        self.staffId = staffId

    def setSalary(self, salary):
        self.salary = salary

    def setDepartment(self, department):
        self.department = department

    def getStaffId(self):
        return self.staffId

    def getSalary(self):
        return self.salary

    def getDepartment(self):
        return self.department

    def __str__(self) -> str:
        return super().__str__() + "StaffId = {staffId}, Salary= {salary},Department={department}".format(
            staffId= self.staffId, salary=self.salary,department= self.department
        )
    def toJson(self):
        return json.dumps(self, default=lambda student: student.__dict__, sort_keys=True)
