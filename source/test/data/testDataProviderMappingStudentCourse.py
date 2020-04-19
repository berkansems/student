# Örneğin bir tablo oluşturalım.Öğrencilerin hangi dersi aldıkları hakkında
# Student Ali  => SENG 101   StudentId 1
# Student Mehmet => SENG101,SENG 201 StudentId 2
# Student Mesut => SENG 301,SENG201  StudentId 3


# Step 1
# 1.1 You can get instance of DataProviderJsonMappingStudentCourse() class
# 1.2 You can get instance of DataProviderJsonStudent() class
# 1.3 You can get instance of DataProviderJsonCourse() class
from source.data.dataAccessJSON.dataProviderJsonCourse import DataProviderJsonCourse
from source.data.dataAccessJSON.dataProviderJsonMappingStudentCourse import DataProviderJsonMappingStudentCourse
from source.data.dataAccessJSON.dataProviderJsonStudent import DataProviderJsonStudent
from source.domain.studentCourseMapping import StudentCourseMapping

dataProviderJsonMappingStudentCourse = DataProviderJsonMappingStudentCourse()
dataProviderJsonStudent = DataProviderJsonStudent()
dataProviderJsonCourse = DataProviderJsonCourse()

# Step 2 => You ought to create three sample StudentCourseMapping class

# Step 2.1 => First Sample StudentCourseMapping
studentCourseMapping1 = StudentCourseMapping()
studentCourseMapping1.setMapId(1)
studentCourseMapping1.setStudentId(1)
studentCourseMapping1.setCourseCode("SENG101")

# Step 2.2 => Second Sample StudentCourseMapping
studentCourseMapping2 = StudentCourseMapping()
studentCourseMapping2.setMapId(2)
studentCourseMapping2.setStudentId(2)
studentCourseMapping2.setCourseCode("SENG101")

studentCourseMapping3 = StudentCourseMapping()
studentCourseMapping3.setMapId(3)
studentCourseMapping3.setStudentId(2)
studentCourseMapping3.setCourseCode("SENG201")

# Step 2.3 => Third Sample ProfessorCourseMapping
studentCourseMapping4 = StudentCourseMapping()
studentCourseMapping4.setMapId(4)
studentCourseMapping4.setStudentId(3)
studentCourseMapping4.setCourseCode("SENG201")

studentCourseMapping5 = StudentCourseMapping()
studentCourseMapping5.setMapId(5)
studentCourseMapping5.setStudentId(3)
studentCourseMapping5.setCourseCode("SENG301")

# Step 3 => Insert all of these instances to inside of studentCourseMapping.json
dataProviderJsonMappingStudentCourse.insert(studentCourseMapping1)
dataProviderJsonMappingStudentCourse.insert(studentCourseMapping2)
dataProviderJsonMappingStudentCourse.insert(studentCourseMapping3)
dataProviderJsonMappingStudentCourse.insert(studentCourseMapping4)
dataProviderJsonMappingStudentCourse.insert(studentCourseMapping5)

# Step 4 => update specific studentCourseMapping by mapId
# studentCourseMapping5.setCourseCode("SENG101")
# dataProviderJsonMappingStudentCourse.update(studentCourseMapping5)

# Step 5 => delete specific studentCourseMapping by mapId
# dataProviderJsonMappingStudentCourse.delete(studentCourseMapping5.getMapId())

# Step 6 => get All studentCourseMappings
result = dataProviderJsonMappingStudentCourse.getList()
if isinstance(result, dict):
    for mapId, studentCourseMappingInfo in result.items():
        print(studentCourseMappingInfo)
elif isinstance(result, bool):
    print(result)

# Step 7 ==> Get Specific studentCourseMappings by mapId
result = dataProviderJsonMappingStudentCourse.getById(5)
if isinstance(result, StudentCourseMapping):
    print(result)
elif isinstance(result, bool):
    print(result)
