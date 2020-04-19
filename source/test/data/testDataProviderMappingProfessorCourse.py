from source.data.dataAccessJSON.dataProviderJsonCourse import DataProviderJsonCourse
from source.data.dataAccessJSON.dataProviderJsonMappingProfessorCourse import DataProviderJsonMappingProfessorCourse
from source.data.dataAccessJSON.dataProviderJsonProfessor import DataProviderJsonProfessor
from source.domain.course import Course
from source.domain.professorCourseMapping import ProfessorCourseMapping

# Örneğin bir tablo oluşturalım.Hangi eğitmen hangi dersi vermesi hakkında
# Professor Ahmet Yılmaz => SENG 101 StaffId 1
# Professor Murat Gungor => SENG 201 StaffId 2
# Professor Gizem Dogan => SENG 301  StaffId 3


# Step 1
# 1.1 You can get instance of DataProviderJsonMappingProfessorCourse() class
# 1.2 You can get instance of DataProviderJsonProfessor() class
# 1.3 You can get instance of DataProviderJsonCourse() class


dataProviderJsonMappingProfessorCourse = DataProviderJsonMappingProfessorCourse()
dataProviderJsonProfessor = DataProviderJsonProfessor()
dataProviderJsonCourse = DataProviderJsonCourse()

# Step 2 => You ought to create three sample ProfessorCourseMapping class
# Step 2.1 => First Sample ProfessorCourseMapping
professorCourseMapping1 = ProfessorCourseMapping()
professorCourseMapping1.setMapId(1)
result = dataProviderJsonCourse.getByCode("SENG101")
if isinstance(result, Course):
    professorCourseMapping1.setCourseCode(result.getCourseCode())
professorCourseMapping1.setStaffId(dataProviderJsonProfessor.getById(1).getStaffId())

# Step 2.2 => Second Sample ProfessorCourseMapping
professorCourseMapping2 = ProfessorCourseMapping()
professorCourseMapping2.setMapId(2)
professorCourseMapping2.setCourseCode(dataProviderJsonCourse.getByCode("SENG201").getCourseCode())
professorCourseMapping2.setStaffId(dataProviderJsonProfessor.getById(2).getStaffId())

# Step 2.3 => Third Sample ProfessorCourseMapping
professorCourseMapping3 = ProfessorCourseMapping()
professorCourseMapping3.setMapId(3)
professorCourseMapping3.setCourseCode(dataProviderJsonCourse.getByCode("SENG301").getCourseCode())
professorCourseMapping3.setStaffId(dataProviderJsonProfessor.getById(3).getStaffId())

# Step 3 => Insert all of these instances to inside of professorCourseMapping.json
dataProviderJsonMappingProfessorCourse.insert(professorCourseMapping1)
dataProviderJsonMappingProfessorCourse.insert(professorCourseMapping2)
dataProviderJsonMappingProfessorCourse.insert(professorCourseMapping3)

# Step 4 => update specific professorCourseMapping by mapId
professorCourseMapping2.setStaffId(3)
dataProviderJsonMappingProfessorCourse.update(professorCourseMapping2)

# Step 5 => delete specific professorCourseMapping by mapId
# dataProviderJsonMappingProfessorCourse.delete(professorCourseMapping2.getMapId())

# Step 6 => get All professorCourseMappings
result = dataProviderJsonMappingProfessorCourse.getList()
if isinstance(result, dict):
    for mapId, professorCourseMappingInfo in result.items():
        print(professorCourseMappingInfo)
elif isinstance(result, bool):
    print(result)

# Step 7 ==> Get Specific professorCourseMapping by mapId
result = dataProviderJsonMappingProfessorCourse.getById(2)
if isinstance(result, ProfessorCourseMapping):
    print(result)
elif isinstance(result, bool):
    print(result)


