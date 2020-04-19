import json
from pathlib import Path

from source.domain.studentCourseMapping import StudentCourseMapping


class DataProviderJsonMappingStudentCourse:
    studentCourseList = None
    connectionString = None

    def __init__(self):
        global studentCourseList
        global connectionString
        studentCourseList = dict()
        connectionString = "{0}".format(
            Path.home().joinpath("Desktop",
                                 "studentregistrationsystem-v9",
                                 "studentregistrationsystem",
                                 "source",
                                 "data",
                                 "dataAccessJSON",
                                 "jsons",
                                 "studentCourseMapping.json"))
        if Path(connectionString).is_file():
            self.getList()
        else:
            with open(connectionString, "w") as studentCourseListFile:
                json.dump(studentCourseList, studentCourseListFile)

    def insert(self, studentCourseMapping):
        try:
            studentCourseList[studentCourseMapping.getMapId()] = studentCourseMapping.toJson()
            with open(connectionString, "w") as studentCourseListFile:
                json.dump(studentCourseList, studentCourseListFile)
                return True
        except:
            return False

    def update(self, studentCourseMapping):
        for mapId, professorCourseMappingInfo in studentCourseList.items():
            if studentCourseMapping.getMapId() == mapId:
                currentStudentCourseMapping = StudentCourseMapping()
                currentStudentCourseMapping.setStudentId(studentCourseMapping.getStudentId())
                currentStudentCourseMapping.setCourseCode(studentCourseMapping.getCourseCode())
                currentStudentCourseMapping.setMapId(studentCourseMapping.getMapId())
                studentCourseList[mapId] = currentStudentCourseMapping.toJson()
                with open(connectionString, "w") as studentCourseListFile:
                    json.dump(studentCourseList, studentCourseListFile)
                    return True
        return False

    def delete(self, mapId):
        for map_Id, studentCourseMappingInfo in studentCourseList.items():
            if mapId == map_Id:
                del studentCourseList[mapId]
                with open(connectionString, "w") as studentCourseListFile:
                    json.dump(studentCourseList, studentCourseListFile)
                    return True
        return False

    def getById(self, mapId):
        with open(connectionString, "r") as studentCourseListFile:
            studentCourseListFromFile = dict(json.load(studentCourseListFile))
            for map_Id, studentCourseMappingInfo in studentCourseListFromFile.items():
                if mapId == int(map_Id):
                    currentInsertedStudentCourseMapping = json.loads(studentCourseMappingInfo)
                    currentStudentCourseMapping = StudentCourseMapping()
                    currentStudentCourseMapping.setMapId(currentInsertedStudentCourseMapping["mapId"])
                    currentStudentCourseMapping.setCourseCode(currentInsertedStudentCourseMapping["courseCode"])
                    currentStudentCourseMapping.setStudentId(currentInsertedStudentCourseMapping["studentId"])
                    return currentStudentCourseMapping
        return False

    def getList(self):
        studentCourseList.clear()
        with open(connectionString, "r") as studentCourseListFile:
            try:
                studentCourseListFromFile = dict(json.load(studentCourseListFile))
                for mapId, studentCourseMappingInfo in studentCourseListFromFile.items():
                    currentInsertedStudentCourseMapping = json.loads(studentCourseMappingInfo)
                    currentStudentCourseMapping = StudentCourseMapping()
                    currentStudentCourseMapping.setMapId(currentInsertedStudentCourseMapping["mapId"])
                    currentStudentCourseMapping.setCourseCode(currentInsertedStudentCourseMapping["courseCode"])
                    currentStudentCourseMapping.setStudentId(currentInsertedStudentCourseMapping["studentId"])
                    studentCourseList[mapId] = currentStudentCourseMapping.toJson()
                return studentCourseList
            except Exception as ex:
                return ex
