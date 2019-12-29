import json
from pathlib import Path

from source.domain.student import Student


class DataProviderJsonStudent:
    studentList = None
    connectionString = None

    def __init__(self):
        global studentList
        global connectionString
        studentList = dict()
        connectionString = "{0}".format(
            Path.home().joinpath("Desktop",
                                 "python",
                                 "class",
                                 "student",
                                 "source",
                                 "data",
                                 "dataAccessJSON",
                                 "jsons",
                                 "courseList.json"))

        with open(connectionString, "w") as studentListFile:
            json.dump(studentList, studentListFile)

    def insert(self, student):
        global studentList
        studentList[student.getStudentId()] = student.toJson()
        studentListFile = open(connectionString, "w")
        json.dump(studentList, studentListFile)
        return True

    def update(self, student):
        global studentList
        for studentId, studentInfo in studentList.items():
            if studentId == student.getStudentId():
                currentStudent = Student()
                currentStudent.setStudentId(student.getStudentId())
                currentStudent.setName(student.getName())
                currentStudent.setPassword(student.getPassword())
                currentStudent.setContactNumber(student.getContactNumber())
                currentStudent.setEmail(student.getEmail())
                currentStudent.setAddress(student.getAddress())
                studentList[currentStudent.getStudentId()] = currentStudent.toJson()
                with open(connectionString, "w") as studentListFile:
                    json.dump(studentList, studentListFile)
                return True
        return False

    def delete(self, id):
        global studentList
        for studentId, studentInfo in studentList.items():
            if studentId == id:
                del studentList[id]
                with open(connectionString, "w") as studentListFile:
                    json.dump(studentList, studentListFile)
                    return True
        return False

    def getList(self):
        global studentList
        studentList.clear()
        try:
            with open(connectionString, "r") as studentListFile:
                studentListFromFile = dict(json.load(studentListFile))
                for studentId, studentInfo in studentListFromFile.items():
                    currentInsertedStudent = json.loads(studentInfo)
                    currentStudent = Student()
                    currentStudent.setStudentId(currentInsertedStudent["studentId"])
                    currentStudent.setName(currentInsertedStudent["name"])
                    currentStudent.setEmail(currentInsertedStudent["email"])
                    currentStudent.setAddress(currentInsertedStudent["address"])
                    currentStudent.setContactNumber(currentInsertedStudent["contactNumber"])
                    currentStudent.setPassword(currentInsertedStudent["password"])
                    studentList[currentStudent.getStudentId()] = currentStudent.toJson()
                    #result = 1 / 0
                if studentList.items() == 0:
                    raise ValueError("Dosya içerisinde herhangi kayıt bulunamadı.")
                return studentList
        except FileNotFoundError as fileNotFoundError:
            return fileNotFoundError
        except ValueError as valueError:
            return valueError
        except ZeroDivisionError as zeroDivisionError:
            return zeroDivisionError
        except Exception as ex:
            return ex


    def getById(self, id):
        global studentList
        with open(connectionString, "r") as studentListFile:
            studentListFromFile = dict(json.load(studentListFile))
            for studentId, studentInfo in studentListFromFile.items():
                if studentId == id:
                    currentInsertedStudent = json.loads(studentInfo)
                    currentStudent = Student()
                    currentStudent.setStudentId(currentInsertedStudent["studentId"])
                    currentStudent.setName(currentInsertedStudent["name"])
                    currentStudent.setEmail(currentInsertedStudent["email"])
                    currentStudent.setAddress(currentInsertedStudent["address"])
                    currentStudent.setContactNumber(currentInsertedStudent["contactNumber"])
                    currentStudent.setPassword(currentInsertedStudent["password"])
                    return currentStudent
            return False
