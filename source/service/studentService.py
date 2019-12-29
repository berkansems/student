import json

from source.data.dataAccessDictionary.dataProviderStudent import DataProviderStudent
from source.data.dataAccessJSON.dataProviderJsonStudent import DataProviderJsonStudent
from source.dataTransferObject.studentViewModel import StudentViewModel
from source.domain.student import Student


class StudentService:
    dataProviderStudent = None

    def __init__(self):
        global dataProviderStudent
        #self.dataProviderStudent = DataProviderStudent() # for dictionary
        self.dataProviderStudent = DataProviderJsonStudent() # for Json
    def insert(self, studentViewModelInsertion):
        student = Student()
        student.setStudentId(studentViewModelInsertion.getStudentId())
        student.setName(studentViewModelInsertion.getName())
        student.setEmail(studentViewModelInsertion.getEmail())
        student.setContactNumber(studentViewModelInsertion.getContactNumber())
        student.setPassword(studentViewModelInsertion.getPassword())
        student.setAddress(studentViewModelInsertion.getAddress())
        return self.dataProviderStudent.insert(student)  # result of insert method TRUE or FALSE

    def update(self, studentViewModelUpdate):
        student = Student()
        student.setStudentId(studentViewModelUpdate.getStudentId())
        student.setName(studentViewModelUpdate.getName())
        student.setEmail(studentViewModelUpdate.getEmail())
        student.setContactNumber(studentViewModelUpdate.getContactNumber())
        student.setPassword(studentViewModelUpdate.getPassword())
        student.setAddress(studentViewModelUpdate.getAddress())
        return self.dataProviderStudent.update(student)

    def delete(self, studentViewModelDeletion):
        return self.dataProviderStudent.delete(studentViewModelDeletion.getStudentId())

    def getList(self):
        studentList = self.dataProviderStudent.getList()
        if not isinstance(studentList,ZeroDivisionError):
            studentViewModelList = dict()
            for studentId, studentInfo in studentList.items():
                studentViewModel = StudentViewModel()
                currentInsertedStudent = json.loads(studentInfo)
                studentViewModel.setStudentId(currentInsertedStudent["studentId"])
                studentViewModel.setName(currentInsertedStudent["name"])
                studentViewModel.setEmail(currentInsertedStudent["email"])
                studentViewModel.setAddress(currentInsertedStudent["address"])
                studentViewModel.setContactNumber(currentInsertedStudent["contactNumber"])
                studentViewModel.setPassword(currentInsertedStudent["password"])
                studentViewModelList[studentId] = studentViewModel
            return studentViewModelList
        else:
            return studentList

    def getById(self, studentViewModelGetById):
        result = self.dataProviderStudent.getById(studentViewModelGetById.getStudentId())
        if result != False:
            studentViewModel = StudentViewModel()
            studentViewModel.setStudentId(result.getStudentId())
            studentViewModel.setName(result.getName())
            studentViewModel.setEmail(result.getEmail())
            studentViewModel.setAddress(result.getAddress())
            studentViewModel.setContactNumber(result.getContactNumber())
            studentViewModel.setPassword(result.getPassword())
            return studentViewModel
        return result
