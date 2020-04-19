from source.data.dataAccessJSON.dataProviderJsonCourse import DataProviderJsonCourse

# Step 1 => You can get instance of DataProviderJsonCourse() class
from source.domain.course import Course

dataProviderJsonCourse = DataProviderJsonCourse()

# Step 2 => You ought to create three sample course
# Step 2.1 => First Sample Course
course1 = Course()
course1.setCourseCode("SENG101")
course1.setCourseName("Introduction to Software Engineering")
course1.setStartDate("16.09.2019")
course1.setEndDate("16.01.2020")
course1.setFacultyCode("ENGSOFT")

# Step 2.2 => Second Sample Course
course2 = Course()
course2.setCourseCode("SENG201")
course2.setCourseName("Software Construction")
course2.setStartDate("16.09.2019")
course2.setEndDate("16.01.2020")
course2.setFacultyCode("ENGSOFT")

# Step 2.3 => Third Sample Course
course3 = Course()
course3.setCourseCode("SENG301")
course3.setCourseName("Introduction to Database")
course3.setStartDate("16.09.2019")
course3.setEndDate("16.01.2020")
course3.setFacultyCode("ENGSOFT")

# Step 3 => Insert all of these instances to inside of courseList.json

dataProviderJsonCourse.insert(course1)
dataProviderJsonCourse.insert(course2)
dataProviderJsonCourse.insert(course3)

# Step 4 => update specific course by courseCode
course2.setStartDate("20.09.2019")
dataProviderJsonCourse.update(course2)

# Step 5 => delete specific course by courseCode
#dataProviderJsonCourse.delete(course3.getCourseCode())

# Step 6 => get All courses
result = dataProviderJsonCourse.getList()
if isinstance(result,dict):
    for courseCode,courseInfo in result.items():
        print(courseInfo)

# Step 7==> Get Specific course by courseCode
result = dataProviderJsonCourse.getByCode("SENG101")
if isinstance(result,Course):
    print(result)
elif isinstance(result,bool):
    print(result)