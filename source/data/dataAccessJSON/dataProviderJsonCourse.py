import json
from pathlib import Path

from source.domain.course import Course


class DataProviderJsonCourse:
    courseList = None
    connectionString = None

    def __init__(self):
        global courseList
        global connectionString
        courseList = dict()
        connectionString = "{0}".format(
            Path.home().joinpath("Desktop",
                                 "studentregistrationsystem-v9",
                                 "studentregistrationsystem",
                                 "source",
                                 "data",
                                 "dataAccessJSON",
                                 "jsons",
                                 "courseList.json"))

        if Path(connectionString).is_file():
            self.getList()
        else:
            with open(connectionString, "w") as courseListFile:
                json.dump(courseList, courseListFile)

    def insert(self, course):
        courseList[course.getCourseCode()] = course.toJson()
        try:
            with open(connectionString, "w") as courseListFile:
                json.dump(courseList, courseListFile)
                return True
        except:
            return False

    def update(self, course):
        for courseCode, courseInfo in courseList.items():
            if course.getCourseCode() == courseCode:
                currentCourse = Course()
                currentCourse.setCourseCode(courseCode)
                currentCourse.setCourseName(course.getCourseName())
                currentCourse.setEndDate(course.getEndDate())
                currentCourse.setStartDate(course.getStartDate())
                currentCourse.setFacultyCode(course.getFacultyCode())
                courseList[currentCourse.getCourseCode()] = currentCourse.toJson()
                with open(connectionString, "w") as courseListFile:
                    json.dump(courseList, courseListFile)
                    return True
        return False

    def delete(self, code):
        for courseCode, courseInfo in courseList.items():
            if code == courseCode:
                del courseList[code]
                with open(connectionString, "w") as courseListFile:
                    json.dump(courseList, courseListFile)
                    return True
        return False

    def getList(self):
        courseList.clear()
        with open(connectionString, "r") as courseListFile:
            courseListFromFile = dict(json.load(courseListFile))
            for courseCode, courseInfo in courseListFromFile.items():
                currentInsertedCourse = json.loads(courseInfo)
                currentCourse = Course()
                currentCourse.setCourseCode(courseCode)
                currentCourse.setFacultyCode(currentInsertedCourse["facultyCode"])
                currentCourse.setStartDate(currentInsertedCourse["startDate"])
                currentCourse.setEndDate(currentInsertedCourse["endDate"])
                currentCourse.setCourseName(currentInsertedCourse["courseName"])
                courseList[currentCourse.getCourseCode()] = currentCourse.toJson()
            return courseList

    def getByCode(self, code):
        with open(connectionString, "r") as courseListFile:
            courseListFromFile = dict(json.load(courseListFile))
            for courseCode, courseInfo in courseListFromFile.items():
                if code == courseCode:
                    currentInsertedCourse = json.loads(courseInfo)
                    currentCourse = Course()
                    currentCourse.setCourseCode(courseCode)
                    currentCourse.setFacultyCode(currentInsertedCourse["facultyCode"])
                    currentCourse.setStartDate(currentInsertedCourse["startDate"])
                    currentCourse.setEndDate(currentInsertedCourse["endDate"])
                    currentCourse.setCourseName(currentInsertedCourse["courseName"])
                    return currentCourse
        return False
