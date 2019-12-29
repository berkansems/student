# Professor => Course
# Student  => Course
# courseProfessorList
# activeCourseList
import json

from source.data.dataAccessJSON.dataProviderJsonCourse import DataProviderJsonCourse
from source.dataTransferObject.courseViewModel import CourseViewModel
from source.domain.course import Course
from source.service.professorService import ProfessorService
from source.service.studentService import StudentService


class CourseService:
    dataProviderCourse = None
    studentService = None
    professorService = None

    def __init__(self):
        self.dataProviderCourse = DataProviderJsonCourse()
        self.studentService = StudentService()
        self.professorService = ProfessorService()

    def insert(self, courseViewModelInsertion):
        course = Course()
        course.setCourseName(courseViewModelInsertion.getCourseName())
        course.setCourseCode(courseViewModelInsertion.getCourseCode())
        course.setEndDate(courseViewModelInsertion.getEndDate())
        course.setStartDate(courseViewModelInsertion.getStartDate())
        course.setStaffId(courseViewModelInsertion.getStaffId())
        course.setFacultyCode(courseViewModelInsertion.getFacultyCode())
        return self.dataProviderCourse.insert(course)

    def update(self, courseViewModelUpdate):
        course = Course()
        course.setCourseName(courseViewModelUpdate.getCourseName())
        course.setCourseCode(courseViewModelUpdate.getCourseCode())
        course.setEndDate(courseViewModelUpdate.getEndDate())
        course.setStartDate(courseViewModelUpdate.getStartDate())
        course.setStaffId(courseViewModelUpdate.getStaffId())
        course.setFacultyCode(courseViewModelUpdate.getFacultyCode())
        return self.dataProviderCourse.update(course)

    def delete(self, courseViewModelDeletion):
        return self.dataProviderCourse.delete(courseViewModelDeletion.getCourseCode())

    def getList(self):
        courseList = self.dataProviderCourse.getList()
        courseViewModelList = dict()
        for courseCode, courseInfo in courseList.items():
            courseViewModel = CourseViewModel()
            currentInsertedCourse = json.loads(courseInfo)
            courseViewModel.setCourseCode(courseCode)
            courseViewModel.setCourseName(currentInsertedCourse["courseName"])
            courseViewModel.setFacultyCode(currentInsertedCourse["facultyCode"])
            courseViewModel.setStaffId(currentInsertedCourse["staffId"])
            courseViewModel.setStartDate(currentInsertedCourse["startDate"])
            courseViewModel.setEndDate(currentInsertedCourse["endDate"])
            courseViewModelList[courseCode] = courseViewModel
        return courseViewModelList

    def getByCode(self, courseViewModelCode):
        result = self.dataProviderCourse.getByCode(courseViewModelCode.getCourseCode())
        if result != False:
            courseViewModel = CourseViewModel()
            courseViewModel.setCourseCode(result.getCourseCode())
            courseViewModel.setCourseName(result.getCourseName())
            courseViewModel.setFacultyCode(result.getFacultyCode())
            courseViewModel.setStaffId(result.getStaffId())
            courseViewModel.setStartDate(result.getStartDate())
            courseViewModel.setEndDate(result.getEndDate())
            return courseViewModel
        return result

    def insertStudentToActiveCourse(self, courseViewModelStudentInsertion):

        return None
