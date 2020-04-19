from source.data.dataAccessDictionary.dataProviderStudent import DataProviderStudent
from source.domain.student import Student

dataProviderStudent = DataProviderStudent()
# Student 1
student1 = Student()
student1.setStudentId(1)
student1.setName("Ali")
student1.setPassword("12345")
student1.setContactNumber("5454444444")
student1.setAddress("142 street")
student1.setEmail("ali@gmail.com")

# Student 2
student2 = Student()
student2.setStudentId(2)
student2.setName("Mehmet")
student2.setPassword("54654756")
student2.setContactNumber("543786786556")
student2.setAddress("222 Street")
student2.setEmail("mehmet@gmail.com")

# Student 3
student3 = Student()
student3.setStudentId(3)
student3.setName("Mesut")
student3.setPassword("543423654756")
student3.setContactNumber("1111")
student3.setAddress("2122 Street")
student3.setEmail("mesut@gmail.com")

# insertion
# first insertion
print("*************Insert**************")
currentStudentList = dataProviderStudent.insert(student1)
print(currentStudentList)

# second insertion
currentStudentList = dataProviderStudent.insert(student2)
print(currentStudentList)

# third insertion
currentStudentList = dataProviderStudent.insert(student3)
print(currentStudentList)

# update
student1.setName("Osman")
student1.setAddress("542 Street")
currentStudentList = dataProviderStudent.update(student1)
student2.setName("Burak")
student2.setEmail("burak@gmail.com")
currentStudentList = dataProviderStudent.update(student2)
print("*************Update**************")
print(currentStudentList)
print(currentStudentList)
print(currentStudentList)

print("*************Delete**************")
isSuccess = dataProviderStudent.delete(1)
print(isSuccess)

print("*************Student List**************")
currentStudentList = dict(dataProviderStudent.getList())
print(currentStudentList)
for studentId,studentInfo in currentStudentList.items():
    print(currentStudentList[studentId])

print("*************Student**************")
currentStudent = dataProviderStudent.getById(2)
print(currentStudent)