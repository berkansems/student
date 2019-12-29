from source.dataTransferObject.studentViewModel import StudentViewModelInsertion, StudentViewModelDeletion, \
    StudentViewModelGetById
from source.service.studentService import StudentService

studentService = StudentService()

# Student 1
student1 = StudentViewModelInsertion()
student1.setStudentId(1)
student1.setName("Ali")
student1.setPassword("12345")
student1.setContactNumber("5454444444")
student1.setAddress("142 street")
student1.setEmail("ali@gmail.com")

# Student 2
student2 = StudentViewModelInsertion()
student2.setStudentId(2)
student2.setName("Mehmet")
student2.setPassword("54654756")
student2.setContactNumber("543786786556")
student2.setAddress("222 Street")
student2.setEmail("mehmet@gmail.com")

# Student 3
student3 = StudentViewModelInsertion()
student3.setStudentId(3)
student3.setName("Mesut")
student3.setPassword("543423654756")
student3.setContactNumber("1111")
student3.setAddress("2122 Street")
student3.setEmail("mesut@gmail.com")

# insertion
# first insertion
print("*************Insert**************")
result = studentService.insert(student1)
print("Insertion has been completed successfully : {0}".format(result))

# second insertion
result = studentService.insert(student2)
print("Insertion has been completed successfully : {0}".format(result))

# third insertion
result = studentService.insert(student3)
print("Insertion has been completed successfully : {0}".format(result))



print("*************After Insertion Process Student List**************")
currentStudentList = dict(studentService.getList())
for studentId,studentInfo in currentStudentList.items():
    print(currentStudentList[studentId])



# update
student1.setName("Osman")
student1.setAddress("542 Street")
result = studentService.update(student1)
student2.setName("Burak")
student2.setEmail("burak@gmail.com")
result = studentService.update(student2)
print("*************Update**************")
currentStudentList = dict(studentService.getList())
for studentId,studentInfo in currentStudentList.items():
    print(currentStudentList[studentId])
print("*********************************")



print("*************Delete**************")
studentViewModelDeletion  = StudentViewModelDeletion()
studentViewModelDeletion.setStudentId(2)
isSuccess = studentService.delete(studentViewModelDeletion)
print("Deletion has been completed successfully : {0}".format(isSuccess))


print("*************Student**************")
studentViewModelGetById = StudentViewModelGetById()
studentViewModelGetById.setStudentId(2)
currentStudent = studentService.getById(studentViewModelGetById)
print(currentStudent)

print("*************Student List**************")
currentStudentList = dict(studentService.getList())
for studentId,studentInfo in currentStudentList.items():
    print(currentStudentList[studentId])