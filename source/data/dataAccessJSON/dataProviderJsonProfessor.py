import json
from pathlib import Path

from source.domain.professor import Professor



class DataProviderJsonProfessor:
    professorList = None
    connectionString = None

    def __init__(self):
        global professorList
        global connectionString
        professorList = dict()
        connectionString = "{0}".format(
            Path.home().joinpath("Desktop",
                                 "studentregistrationsystem-v9",
                                 "studentregistrationsystem",
                                 "source",
                                 "data",
                                 "dataAccessJSON",
                                 "jsons",
                                 "professorList.json"))


        if Path(connectionString).is_file():
            self.getList()
        else:
            with open(connectionString, "w") as professorListFile:
                json.dump(professorList, professorListFile)

    def insert(self, professor):
        global professorList
        professorList[professor.getStaffId()] = professor.toJson()
        professorListFile = open(connectionString, "w")
        json.dump(professorList, professorListFile)
        return True

    def update(self, professor):
        global professorList
        for staffId, studentInfo in professorList.items():
            if staffId == professor.getStaffId():
                currentProfessor = Professor()
                currentProfessor.setStaffId(professor.getStaffId())
                currentProfessor.setName(professor.getName())
                currentProfessor.setPassword(professor.getPassword())
                currentProfessor.setContactNumber(professor.getContactNumber())
                currentProfessor.setEmail(professor.getEmail())
                currentProfessor.setAddress(professor.getAddress())
                currentProfessor.setSalary(professor.getSalary())
                professorList[currentProfessor.getStaffId()] = currentProfessor.toJson()
                with open(connectionString, "w") as professorListFile:
                    json.dump(professorList, professorListFile)
                return True
        return False

    def delete(self, id):
        global professorList
        for staffId, professorInfo in professorList.items():
            if staffId == id:
                del professorList[id]
                with open(connectionString, "w") as professorListFile:
                    json.dump(professorList, professorListFile)
                    return True
        return False

    def getList(self):
        global professorList
        professorList.clear()
        try:
            with open(connectionString, "r") as professorListFile:
                professorListFromFile = dict(json.load(professorListFile))
                for staffId, professorInfo in professorListFromFile.items():
                    currentInsertedProfessor = json.loads(professorInfo)
                    currentProfessor = Professor()
                    currentProfessor.setStaffId(currentInsertedProfessor["staffId"])
                    currentProfessor.setName(currentInsertedProfessor["name"])
                    currentProfessor.setEmail(currentInsertedProfessor["email"])
                    currentProfessor.setAddress(currentInsertedProfessor["address"])
                    currentProfessor.setContactNumber(currentInsertedProfessor["contactNumber"])
                    currentProfessor.setPassword(currentInsertedProfessor["password"])
                    currentProfessor.setSalary(currentInsertedProfessor["salary"])
                    currentProfessor.setDepartment(currentInsertedProfessor["department"])
                    professorList[currentProfessor.getStaffId()] = currentProfessor.toJson()
                if professorList.items() == 0:
                    raise ValueError("Dosya içerisinde herhangi kayıt bulunamadı.")
                return professorList
        except FileNotFoundError as fileNotFoundError:
            return fileNotFoundError
        except ValueError as valueError:
            return valueError
        except Exception as ex:
            return ex

    def getById(self, id):
        global professorList
        with open(connectionString, "r") as professorListFile:
            professorListFromFile = dict(json.load(professorListFile))
            for staffId, professorInfo in professorListFromFile.items():
                if int(staffId) == int(id):
                    currentInsertedProfessor = json.loads(professorInfo)
                    currentProfessor = Professor()
                    currentProfessor.setStaffId(currentInsertedProfessor["staffId"])
                    currentProfessor.setName(currentInsertedProfessor["name"])
                    currentProfessor.setEmail(currentInsertedProfessor["email"])
                    currentProfessor.setAddress(currentInsertedProfessor["address"])
                    currentProfessor.setContactNumber(currentInsertedProfessor["contactNumber"])
                    currentProfessor.setPassword(currentInsertedProfessor["password"])
                    currentProfessor.setSalary(currentInsertedProfessor["salary"])
                    currentProfessor.setDepartment(currentInsertedProfessor["department"])
                    return currentProfessor
            return False