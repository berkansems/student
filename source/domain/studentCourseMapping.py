import json


class StudentCourseMapping:

    def __init__(self, mapId=0, studentId=0, courseCode=""):
        self.mapId = mapId
        self.studentId = studentId
        self.courseCode = courseCode

    def setMapId(self, mapId):
        self.mapId = mapId

    def getMapId(self):
        return self.mapId

    def setStudentId(self, studentId):
        self.studentId = studentId

    def getStudentId(self):
        return self.studentId

    def setCourseCode(self, courseCode):
        self.courseCode = courseCode

    def getCourseCode(self):
        return self.courseCode

    def toJson(self):
        return json.dumps(self, default=lambda studentCourseMapping: studentCourseMapping.__dict__, sort_keys=True)

    def __str__(self) -> str:
        return "mapId={mapId},studentId={studentId},courseCode={courseCode}".format(
            mapId=self.mapId,
            studentId=self.studentId,
            courseCode=self.courseCode,
        )
