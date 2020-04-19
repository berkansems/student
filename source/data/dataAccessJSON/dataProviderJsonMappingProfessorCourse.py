import json
from json import JSONDecodeError
from pathlib import Path

from source.domain.professorCourseMapping import ProfessorCourseMapping


class DataProviderJsonMappingProfessorCourse:
    professorCourseList = None
    connectionString = None

    def __init__(self):
        global professorCourseList
        global connectionString
        professorCourseList = dict()
        connectionString = "{0}".format(
            Path.home().joinpath("Desktop",
                                 "studentregistrationsystem-v9",
                                 "studentregistrationsystem",
                                 "source",
                                 "data",
                                 "dataAccessJSON",
                                 "jsons",
                                 "professorCourseMapping.json"))

        if Path(connectionString).is_file():
            self.getList()
        else:
            with open(connectionString, "w") as professorCourseListFile:
                json.dump(professorCourseList, professorCourseListFile)

    def insert(self, professorCourseMapping):
        try:
            professorCourseList[professorCourseMapping.getMapId()] = professorCourseMapping.toJson()
            with open(connectionString, "w") as professorCourseListFile:
                json.dump(professorCourseList, professorCourseListFile)
                return True
        except:
            return False

    def update(self, professorCourseMapping):
        for mapId, professorCourseMappingInfo in professorCourseList.items():
            if professorCourseMapping.getMapId() == mapId:
                currentProfessorCourseMapping = ProfessorCourseMapping()
                currentProfessorCourseMapping.setStaffId(professorCourseMapping.getStaffId())
                currentProfessorCourseMapping.setCourseCode(professorCourseMapping.getCourseCode())
                currentProfessorCourseMapping.setMapId(professorCourseMapping.getMapId())
                professorCourseList[mapId] = currentProfessorCourseMapping.toJson()
                with open(connectionString, "w") as professorCourseListFile:
                    json.dump(professorCourseList, professorCourseListFile)
                    return True
        return False

    def delete(self, mapId):
        for map_Id, professorCourseMappingInfo in professorCourseList.items():
            if mapId == map_Id:
                del professorCourseList[mapId]
                with open(connectionString, "w") as professorCourseListFile:
                    json.dump(professorCourseList, professorCourseListFile)
                    return True
        return False

    def getById(self, mapId):
        with open(connectionString, "r") as professorCourseListFile:
            professorCourseListFromFile = dict(json.load(professorCourseListFile))
            for map_Id, professorCourseMappingInfo in professorCourseListFromFile.items():
                if mapId == int(map_Id):
                    currentInsertedProfessorCourseMapping = json.loads(professorCourseMappingInfo)
                    currentProfessorCourseMapping = ProfessorCourseMapping()
                    currentProfessorCourseMapping.setMapId(currentInsertedProfessorCourseMapping["mapId"])
                    currentProfessorCourseMapping.setCourseCode(currentInsertedProfessorCourseMapping["courseCode"])
                    currentProfessorCourseMapping.setStaffId(currentInsertedProfessorCourseMapping["staffId"])
                    return currentProfessorCourseMapping
        return False

    def getList(self):
        professorCourseList.clear()
        try:
            with open(connectionString, "r") as professorCourseListFile:
                professorCourseListFromFile = dict(json.load(professorCourseListFile))
                for mapId, professorCourseMappingInfo in professorCourseListFromFile.items():
                    currentInsertedProfessorCourseMapping = json.loads(professorCourseMappingInfo)
                    currentProfessorCourseMapping = ProfessorCourseMapping()
                    currentProfessorCourseMapping.setMapId(currentInsertedProfessorCourseMapping["mapId"])
                    currentProfessorCourseMapping.setCourseCode(currentInsertedProfessorCourseMapping["courseCode"])
                    currentProfessorCourseMapping.setStaffId(currentInsertedProfessorCourseMapping["staffId"])
                    professorCourseList[mapId] = currentProfessorCourseMapping.toJson()
                return professorCourseList
        except JSONDecodeError as jde:
            return jde
