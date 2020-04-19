from source.dataTransferObject.courseViewModel import CourseViewModelInsertion, CourseViewModelStudentInsertion
from source.service.courseService import CourseService

# Step 1 => You can get instance of CourseService() class
courseService = CourseService()


# Step 2 => You ought to create three sample course
# Step 2.1 => First Sample Professor
courseViewModelInsertion1 = CourseViewModelInsertion()
courseViewModelInsertion1.setMapId(4)
courseViewModelInsertion1.setStaffId(3)
courseViewModelInsertion1.setCourseCode("SENG401")
courseViewModelInsertion1.setStartDate("20.01.2020")
courseViewModelInsertion1.setEndDate("20.06.2020")
courseViewModelInsertion1.setCourseName("Advanced Software Constructions")
courseViewModelInsertion1.setFacultyCode("ENGSENG")

courseService.insert(courseViewModelInsertion1)

result = courseService.getList()
print("ghjk")

courseService.createUniqueMapId()
courseViewModelStudentInsertion = CourseViewModelStudentInsertion()
courseViewModelStudentInsertion.setCourseCode("SENG101")
courseViewModelStudentInsertion.setStudentId(3)
courseService.insertStudentToActiveCourse(courseViewModelStudentInsertion)