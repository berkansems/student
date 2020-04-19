# Professor => Course
# Student  => Course
# courseProfessorList
# activeCourseList
import json
from json import JSONDecodeError

from source.data.dataAccessJSON.dataProviderJsonCourse import DataProviderJsonCourse
from source.data.dataAccessJSON.dataProviderJsonMappingProfessorCourse import DataProviderJsonMappingProfessorCourse
from source.data.dataAccessJSON.dataProviderJsonMappingStudentCourse import DataProviderJsonMappingStudentCourse
from source.dataTransferObject.courseViewModel import CourseViewModel, CourseViewModelCode
from source.dataTransferObject.professorViewModel import ProfessorViewModelGetById
from source.domain.course import Course
from source.domain.professorCourseMapping import ProfessorCourseMapping
from source.domain.studentCourseMapping import StudentCourseMapping
from source.service.professorService import ProfessorService
from source.service.studentService import StudentService


class CourseService:
    dataProviderCourse = None
    studentService = None
    professorService = None
    dataProviderProfessorCourseMapping = None
    dataProviderStudentCourseMapping = None

    def __init__(self):
        self.dataProviderCourse = DataProviderJsonCourse()
        self.studentService = StudentService()
        self.professorService = ProfessorService()
        self.dataProviderProfessorCourseMapping = DataProviderJsonMappingProfessorCourse()
        self.dataProviderStudentCourseMapping = DataProviderJsonMappingStudentCourse()

    def insert(self, courseViewModelInsertion):
        course = Course()
        course.setCourseName(courseViewModelInsertion.getCourseName())
        course.setCourseCode(courseViewModelInsertion.getCourseCode())
        course.setEndDate(courseViewModelInsertion.getEndDate())
        course.setStartDate(courseViewModelInsertion.getStartDate())
        course.setFacultyCode(courseViewModelInsertion.getFacultyCode())
        course.setUnitPrice(courseViewModelInsertion.getUnitPrice())
        course.setTotalHour(courseViewModelInsertion.getTotalHour())
        result = self.dataProviderCourse.insert(course)
        if result == True:
            professorCourseMapping = ProfessorCourseMapping()
            professorCourseMapping.setMapId(self.createUniqueMapId(self.dataProviderProfessorCourseMapping.getList()))
            professorCourseMapping.setStaffId(courseViewModelInsertion.getStaffId())
            professorCourseMapping.setCourseCode(courseViewModelInsertion.getCourseCode())
            result = self.dataProviderProfessorCourseMapping.insert(professorCourseMapping)
            if result:
                # UnitPrice,TotalHours
                professorViewModelGetById = ProfessorViewModelGetById()
                professorViewModelGetById.setStaffId(courseViewModelInsertion.getStaffId())
                professor = self.professorService.getById(professorViewModelGetById)
                currentSalary = professor.getSalary() + (
                        courseViewModelInsertion.getUnitPrice() * courseViewModelInsertion.getTotalHour())
                professor.setSalary(currentSalary)
                return self.professorService.update(professor)
        else:
            return False

    def update(self, courseViewModelUpdate):
        course = Course()
        course.setCourseName(courseViewModelUpdate.getCourseName())
        course.setCourseCode(courseViewModelUpdate.getCourseCode())
        course.setEndDate(courseViewModelUpdate.getEndDate())
        course.setStartDate(courseViewModelUpdate.getStartDate())
        # course.setStaffId(courseViewModelUpdate.getStaffId())
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
            courseViewModel.setStartDate(currentInsertedCourse["startDate"])
            courseViewModel.setEndDate(currentInsertedCourse["endDate"])
            professorList = list()
            for mapId, professorCourseMappingInfo in self.dataProviderProfessorCourseMapping.getList().items():
                insertedMappingInfo = json.loads(professorCourseMappingInfo)
                if insertedMappingInfo["courseCode"] == courseCode:
                    professorViewModelGetById = ProfessorViewModelGetById()
                    professorViewModelGetById.setStaffId(insertedMappingInfo["staffId"])
                    professorViewModel = self.professorService.getById(professorViewModelGetById)
                    professorList.append(professorViewModel)
            courseViewModel.setProfessorList(professorList)
            courseViewModelList[courseCode] = courseViewModel

        return courseViewModelList

    def getByCode(self, courseViewModelCode):
        result = self.dataProviderCourse.getByCode(courseViewModelCode.getCourseCode())
        if isinstance(result, Course):
            courseViewModel = CourseViewModel()
            courseViewModel.setCourseCode(result.getCourseCode())
            courseViewModel.setCourseName(result.getCourseName())
            courseViewModel.setFacultyCode(result.getFacultyCode())
            courseViewModel.setStartDate(result.getStartDate())
            courseViewModel.setEndDate(result.getEndDate())
            professorList = list()
            for mapId, professorCourseMappingInfo in self.dataProviderProfessorCourseMapping.getList().items():
                insertedMappingInfo = json.loads(professorCourseMappingInfo)
                if insertedMappingInfo["courseCode"] == result.getCourseCode():
                    professorViewModelGetById = ProfessorViewModelGetById()
                    professorViewModelGetById.setStaffId(insertedMappingInfo["staffId"])
                    professorViewModel = self.professorService.getById(professorViewModelGetById)
                    professorList.append(professorViewModel)
            courseViewModel.setProfessorList(professorList)
            return courseViewModel
        return result

    def insertStudentToActiveCourse(self, courseViewModelStudentInsertion):
        studentCourseMapping = StudentCourseMapping()
        studentCourseMapping.setMapId(self.createUniqueMapId(self.dataProviderStudentCourseMapping.getList()))
        studentCourseMapping.setStudentId(courseViewModelStudentInsertion.getStudentId())
        studentCourseMapping.setCourseCode(courseViewModelStudentInsertion.getCourseCode())
        return self.dataProviderStudentCourseMapping.insert(studentCourseMapping)

    def getEnrolledCoursesOfStudentByStudentId(self, courseViewModelEnrollmentCourseByStudentId):
        result = self.dataProviderStudentCourseMapping.getList()
        insertedCourseCodeList = list()
        insertedCourseViewList = list()
        if isinstance(result, dict):
            for mapId, mapInfo in result.items():
                currentMapInfo = json.loads(mapInfo)
                if str(currentMapInfo["studentId"]) == str(courseViewModelEnrollmentCourseByStudentId.getStudentId()):
                    insertedCourseCodeList.append(currentMapInfo["courseCode"])
            for courseCode in insertedCourseCodeList:
                courseViewModelCode = CourseViewModelCode()
                courseViewModelCode.setCourseCode(courseCode)
                courseViewModel = self.getByCode(courseViewModelCode)
                insertedCourseViewList.append(courseViewModel)
            return insertedCourseViewList
        elif isinstance(result, Exception):
            return False

    def getEnrolledCoursesOfProfessorByStaffId(self, courseViewModelEnrollmentProfessorByStaffId):
        result = self.dataProviderProfessorCourseMapping.getList()
        insertedCourseCodeList = list()
        insertedCourseViewList = list()
        if isinstance(result, dict):
            for mapId, mapInfo in result.items():
                currentMapInfo = json.loads(mapInfo)
                if str(currentMapInfo["staffId"]) == str(courseViewModelEnrollmentProfessorByStaffId.getStaffId()):
                    insertedCourseCodeList.append(currentMapInfo["courseCode"])
            for courseCode in insertedCourseCodeList:
                courseViewModelCode = CourseViewModelCode()
                courseViewModelCode.setCourseCode(courseCode)
                courseViewModel = self.getByCode(courseViewModelCode)
                insertedCourseViewList.append(courseViewModel)
            return insertedCourseViewList
        elif isinstance(result, Exception):
            return False

    def dropCourseByStudent(self, courseViewModelDropCourse):
        result = self.dataProviderStudentCourseMapping.getList()
        if isinstance(result, dict):
            for mapId, mapInfo in result.items():
                currentMapInfo = json.loads(mapInfo)
                if courseViewModelDropCourse.getCourseCode() == currentMapInfo["courseCode"]:
                    if str(courseViewModelDropCourse.getStudentId()) == str(currentMapInfo["studentId"]):
                        return self.dataProviderStudentCourseMapping.delete(mapId)
        elif isinstance(result, bool):
            return False

    def createUniqueMapId(self, result):
        maxId = 0
        if not isinstance(result, JSONDecodeError):
            for mapId in result.keys():
                if maxId < int(mapId):
                    maxId = int(mapId)
            maxId += 1
            return maxId
        maxId += 1
        return maxId
