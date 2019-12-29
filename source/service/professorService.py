import json

from source.data.dataAccessJSON.dataProviderJsonProfessor import DataProviderJsonProfessor
from source.dataTransferObject.professorViewModel import ProfessorViewModel
from source.domain.professor import Professor


class ProfessorService:
    dataProviderProfessor = None

    def __init__(self):
        global dataProviderProfessor
        self.dataProviderProfessor = DataProviderJsonProfessor()

    def insert(self, professorViewModelInsertion):
        professor = Professor()
        professor.setStaffId(professorViewModelInsertion.getStaffId())
        professor.setName(professorViewModelInsertion.getName())
        professor.setEmail(professorViewModelInsertion.getEmail())
        professor.setContactNumber(professorViewModelInsertion.getContactNumber())
        professor.setPassword(professorViewModelInsertion.getPassword())
        professor.setAddress(professorViewModelInsertion.getAddress())
        professor.setSalary(professorViewModelInsertion.getSalary())
        professor.setDepartment(professorViewModelInsertion.getDepartment())
        return self.dataProviderProfessor.insert(professor)  # result of insert method TRUE or FALSE

    def getList(self):
        professorList = self.dataProviderProfessor.getList()
        professorViewModelList = dict()
        for staffId, professorInfo in professorList.items():
            professorViewModel = ProfessorViewModel()
            currentInsertedProfessor = json.loads(professorInfo)
            professorViewModel.setStaffId(currentInsertedProfessor["staffId"])
            professorViewModel.setName(currentInsertedProfessor["name"])
            professorViewModel.setEmail(currentInsertedProfessor["email"])
            professorViewModel.setAddress(currentInsertedProfessor["address"])
            professorViewModel.setContactNumber(currentInsertedProfessor["contactNumber"])
            professorViewModel.setPassword(currentInsertedProfessor["password"])
            professorViewModel.setSalary(currentInsertedProfessor["salary"])
            professorViewModel.setDepartment(currentInsertedProfessor["department"])
            professorViewModelList[staffId] = professorViewModel
        return professorViewModelList
