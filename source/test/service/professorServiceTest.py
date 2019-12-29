from source.dataTransferObject.professorViewModel import ProfessorViewModelInsertion
from source.service.professorService import ProfessorService

professorService = ProfessorService()


# Professor 1
professor1 = ProfessorViewModelInsertion()
professor1.setStaffId(1)
professor1.setName("Ali")
professor1.setPassword("12345")
professor1.setContactNumber("5454444444")
professor1.setAddress("142 street")
professor1.setEmail("ali@gmail.com")
professor1.setSalary(5000)
professor1.setDepartment("Software")

# Professor 2
professor2 = ProfessorViewModelInsertion()
professor2.setStaffId(2)
professor2.setName("Mehmet")
professor2.setPassword("54654756")
professor2.setContactNumber("543786786556")
professor2.setAddress("222 Street")
professor2.setEmail("mehmet@gmail.com")
professor2.setSalary(7000)
professor2.setDepartment("Electric-Electronic")

# Professor 3
professor3 = ProfessorViewModelInsertion()
professor3.setStaffId(3)
professor3.setName("Mesut")
professor3.setPassword("543423654756")
professor3.setContactNumber("1111")
professor3.setAddress("2122 Street")
professor3.setEmail("mesut@gmail.com")
professor2.setSalary(9000)
professor2.setDepartment("Industrial")


# insertion
# first insertion
print("*************Insert**************")
result = professorService.insert(professor1)
print("Insertion has been completed successfully : {0}".format(result))

# second insertion
result = professorService.insert(professor2)
print("Insertion has been completed successfully : {0}".format(result))

# third insertion
result = professorService.insert(professor3)
print("Insertion has been completed successfully : {0}".format(result))



print("*************After Insertion Process Student List**************")
currentStudentList = dict(professorService.getList())
for studentId,studentInfo in currentStudentList.items():
    print(currentStudentList[studentId])
