import json


class ProfessorCourseMapping:

    def __init__(self, mapId=0, staffId=0, courseCode=""):
        self.mapId = mapId
        self.staffId = staffId
        self.courseCode = courseCode

    def setMapId(self, mapId):
        self.mapId = mapId

    def getMapId(self):
        return self.mapId

    def setStaffId(self, staffId):
        self.staffId = staffId

    def getStaffId(self):
        return self.staffId

    def setCourseCode(self, courseCode):
        self.courseCode = courseCode

    def getCourseCode(self):
        return self.courseCode

    def toJson(self):
        return json.dumps(self, default=lambda professorCourseMapping: professorCourseMapping.__dict__, sort_keys=True)