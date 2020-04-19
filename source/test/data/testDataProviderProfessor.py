from source.data.dataAccessJSON.dataProviderJsonProfessor import DataProviderJsonProfessor
from source.domain.professor import Professor

# Step 1 => You can get instance of DataProviderJsonProfessor() class
dataProviderJsonProfessor = DataProviderJsonProfessor()

# Step 2 => You ought to create three sample professor
# Step 2.1 => First Sample Professor
professor = Professor()
professor.setName("Ahmet Yilmaz")
professor.setEmail("ahmet.yilmaz@gmail.com")
professor.setContactNumber("+90 555 555 55 55")
professor.setAddress("142 Street")
professor.setPassword("1234567?!Aa")
professor.setSalary(7000)
professor.setStaffId(1)
professor.setDepartment("Engineering")

# Step 2.2 => Second Sample Professor
professor2 = Professor()
professor2.setName("Murat Gungor")
professor2.setEmail("murat.gungor@gmail.com")
professor2.setContactNumber("+90 555 455 33 33")
professor2.setAddress("156 Street")
professor2.setPassword("1234567?!Aa")
professor2.setSalary(9000)
professor2.setStaffId(2)
professor2.setDepartment("Engineering")

# Step 2.3 => Third Sample Professor
professor3 = Professor()
professor3.setName("Gizem Dogan")
professor3.setEmail("gizem.dogan@gmail.com")
professor3.setContactNumber("+90 555 255 44 44")
professor3.setAddress("176 Street")
professor3.setPassword("1234567?!Aa")
professor3.setSalary(5000)
professor3.setStaffId(3)
professor3.setDepartment("Engineering")

# Step 3 => Insert all of these instances to inside of professorList.json
dataProviderJsonProfessor.insert(professor)
dataProviderJsonProfessor.insert(professor2)
dataProviderJsonProfessor.insert(professor3)

# Step 4 => update specific professor by staffId
professor.setSalary(12000)
dataProviderJsonProfessor.update(professor)

# Step 5 => delete specific professor by staffId
#dataProviderJsonProfessor.delete(professor2.getStaffId())

# Step 6 => get All professors
result = dataProviderJsonProfessor.getList()
if isinstance(result, dict):
    for staffId, professorInfo in result.items():
        print(professorInfo)

# Step 7 ==> Get Specific professor by staffId
result = dataProviderJsonProfessor.getById(3)
if isinstance(result, Professor):
    print(result)
elif isinstance(result, bool):
    print(result)

