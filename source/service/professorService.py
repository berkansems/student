import json

from source.data.dataAccessJSON.dataProviderJsonProfessor import DataProviderJsonProfessor
from source.dataTransferObject.professorViewModel import ProfessorViewModel
from source.domain.professor import Professor


# 1 - Course UnitPrice
# 2-









class ProfessorService:
    dataProviderProfessor = None
    courseService = None
    def __init__(self):
        global dataProviderProfessor
        self.dataProviderProfessor = DataProviderJsonProfessor()
        #self.courseService = CourseService()

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

    def update(self, professorViewModelUpdate):
        professor = Professor()
        professor.setStaffId(professorViewModelUpdate.getStaffId())
        professor.setName(professorViewModelUpdate.getName())
        professor.setEmail(professorViewModelUpdate.getEmail())
        professor.setContactNumber(professorViewModelUpdate.getContactNumber())
        professor.setPassword(professorViewModelUpdate.getPassword())
        professor.setAddress(professorViewModelUpdate.getAddress())
        professor.setSalary(professorViewModelUpdate.getSalary())
        professor.setDepartment(professorViewModelUpdate.getDepartment())
        return self.dataProviderProfessor.update(professor)

    def delete(self, professorViewModelDeletion):
        return self.dataProviderProfessor.delete(professorViewModelDeletion.getStaffId())

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

    def getById(self, professorViewModelGetById):
        result = self.dataProviderProfessor.getById(professorViewModelGetById.getStaffId())
        if isinstance(result, Professor):
            professorViewModel = ProfessorViewModel()
            professorViewModel.setStaffId(result.getStaffId())
            professorViewModel.setName(result.getName())
            professorViewModel.setEmail(result.getEmail())
            professorViewModel.setAddress(result.getAddress())
            professorViewModel.setContactNumber(result.getContactNumber())
            professorViewModel.setPassword(result.getPassword())
            professorViewModel.setSalary(result.getSalary())
            professorViewModel.setDepartment(result.getDepartment())
            return professorViewModel
        else:
            return result
