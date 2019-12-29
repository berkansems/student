class StudentViewModelInsertion:
    def __init__(self, name="", password="", email="", address="", contactNumber="", studentId=""):
        self.name = name
        self.password = password
        self.email = email
        self.address = address
        self.contactNumber = contactNumber
        self.studentId = studentId

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

    def setStudentId(self, studentId):
        self.studentId = studentId

    def getStudentId(self):
        return self.studentId
class StudentViewModelUpdate:
    def __init__(self, name="", password="", email="", address="", contactNumber="", studentId=""):
        self.name = name
        self.password = password
        self.email = email
        self.address = address
        self.contactNumber = contactNumber
        self.studentId = studentId

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

    def setStudentId(self, studentId):
        self.studentId = studentId

    def getStudentId(self):
        return self.studentId
class StudentViewModelDeletion:

    def __init__(self, id="") -> None:
        self.studentId = id

    def setStudentId(self, studentId):
        self.studentId = studentId

    def getStudentId(self):
        return self.studentId
class StudentViewModel:
    def __init__(self, name="", password="", email="", address="", contactNumber="", studentId=""):
        self.name = name
        self.password = password
        self.email = email
        self.address = address
        self.contactNumber = contactNumber
        self.studentId = studentId

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

    def setStudentId(self, studentId):
        self.studentId = studentId

    def getStudentId(self):
        return self.studentId

    def __str__(self) -> str:
        return "Name = {name},Password= {password},Email={email},Address={address},ContactNumber={contactNumber},StudentId={studentId}" \
            .format(
            name=self.getName(),
            password=self.getPassword(),
            email=self.getEmail(),
            address=self.getAddress(),
            contactNumber=self.getContactNumber(),
            studentId = self.getStudentId()
        )
class StudentViewModelGetById:
    def __init__(self, id="") -> None:
        self.studentId = id

    def setStudentId(self, studentId):
        self.studentId = studentId

    def getStudentId(self):
        return self.studentId
