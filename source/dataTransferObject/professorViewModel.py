class ProfessorViewModel:
    def __init__(self, name="",
                 password="",
                 email="",
                 address="",
                 contactNumber="",
                 staffId="",
                 salary="",
                 department=""):
        self.name = name
        self.password = password
        self.email = email
        self.address = address
        self.contactNumber = contactNumber
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

    def setName(self, name):
        self.name = name

    def setPassword(self, password):
        self.password = password

    def setEmail(self, email):
        self.email = email

    def setAddress(self, address):
        self.address = address

    def setContactNumber(self, contactNumber):
        self.contactNumber = contactNumber

    def getName(self):
        return self.name

    def getPassword(self):
        return self.password

    def getEmail(self):
        return self.email

    def getAddress(self):
        return self.address

    def getContactNumber(self):
        return self.contactNumber

    def __str__(self) -> str:
        return "Name = {name},Password= {password},Email={email},Address={address},ContactNumber={contactNumber},StudentId={staffId},Salary={salary},Department={department}" \
            .format(
            name=self.getName(),
            password=self.getPassword(),
            email=self.getEmail(),
            address=self.getAddress(),
            contactNumber=self.getContactNumber(),
            staffId=self.getStaffId(),
            salary=self.getSalary(),
            department=self.getDepartment()
        )


class ProfessorViewModelInsertion:
    def __init__(self, name="",
                 password="",
                 email="",
                 address="",
                 contactNumber="",
                 staffId="",
                 salary="",
                 department=""):
        self.name = name
        self.password = password
        self.email = email
        self.address = address
        self.contactNumber = contactNumber
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

    def setName(self, name):
        self.name = name

    def setPassword(self, password):
        self.password = password

    def setEmail(self, email):
        self.email = email

    def setAddress(self, address):
        self.address = address

    def setContactNumber(self, contactNumber):
        self.contactNumber = contactNumber

    def getName(self):
        return self.name

    def getPassword(self):
        return self.password

    def getEmail(self):
        return self.email

    def getAddress(self):
        return self.address

    def getContactNumber(self):
        return self.contactNumber

    def __str__(self) -> str:
        return "Name = {name},Password= {password},Email={email},Address={address},ContactNumber={contactNumber},StudentId={staffId},Salary={salary},Department={department}" \
            .format(
            name=self.getName(),
            password=self.getPassword(),
            email=self.getEmail(),
            address=self.getAddress(),
            contactNumber=self.getContactNumber(),
            staffId=self.getStaffId(),
            salary=self.getSalary(),
            department=self.getDepartment()
        )