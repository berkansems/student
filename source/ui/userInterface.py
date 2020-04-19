from source.dataTransferObject.courseViewModel import CourseViewModelStudentInsertion, CourseViewModel, \
    CourseViewModelCode, CourseViewModelEnrollmentCourseByStudentId, CourseViewModelDropCourse, \
    CourseViewModelEnrollmentProfessorByStaffId, CourseViewModelInsertion, CourseViewModelUpdate
from source.dataTransferObject.professorViewModel import ProfessorViewModelGetById, ProfessorViewModel
from source.dataTransferObject.studentViewModel import StudentViewModel, StudentViewModelGetById
from source.service.courseService import CourseService
from source.service.professorService import ProfessorService
from source.service.studentService import StudentService

studentService = StudentService()
courseService = CourseService()
professorService = ProfessorService()
while True:
    print("Student Registration System")
    # print("**********Menu*************")
    print("Lütfen Giriş Yapınız")
    print("      1-Öğrenci Girişi")
    print("      2-Öğretmen Girişi")
    chose = int(input("Seçiminiz : "))
    if chose == 1:
        print("Öğrenci Giriş Sayfasına Hoş Geldiniz.")
        wrongCounter = 0
        while True:
            studentId = input("Öğrenci Numaranızı Giriniz : ")
            password = input("Parolanızı Giriniz          : ")
            studentViewModelGetById = StudentViewModelGetById()
            studentViewModelGetById.setStudentId(studentId)
            result = studentService.getById(studentViewModelGetById)
            if isinstance(result, StudentViewModel):
                if password == result.getPassword():
                    print("Öğrenci Yönetim Paneli")
                    while True:
                        print("1-Aktif Kursları Listele ve Ders Seçme")
                        print("2-Kayıtlı Olduğum Kurslar")
                        print("3-Aktif Kurs Arama")
                        print("4-Çıkış")
                        choseStudent = int(input("Seçimizisi Giriniz : "))
                        if choseStudent == 1:
                            courseList = courseService.getList()
                            i = 1
                            for courseCode, courseInfo in courseList.items():
                                # print("{0} {1}".format(i, courseInfo))
                                print(
                                    "{0}- | Kurs Kodu : {1} | Kurs Adı : {2} | Başlangıç Tarihi : {3} | Bitiş Tarihi : {4} | Fakülte Kodu : {5} |".format(
                                        i, courseInfo.getCourseCode(), courseInfo.getCourseName(),
                                        courseInfo.getStartDate(), courseInfo.getEndDate(),
                                        courseInfo.getFacultyCode()))
                                print(" Eğitmen ve Eğitmentler")
                                for professor in courseInfo.getProfessorList():
                                    print("     {0}.Professor : {1}".format(i, professor.getName()))
                                i += 1
                            yesNo = None
                            studentId = result.getStudentId()
                            while yesNo != "no":
                                print("Seçim İşlemi Menüsü")
                                print("1-Kurs Kodu ile Ders Seçmek")
                                print("2-Öğrenci Yönetim Paneline Geri Dön")
                                nestedChose = int(input("Seçiminizi Giriniz : "))
                                if nestedChose == 1:
                                    chosenCourseCode = input("Lütfen Kurs Kodunu Giriniz : ")
                                    courseViewModelStudentInsertion = CourseViewModelStudentInsertion()
                                    courseViewModelStudentInsertion.setStudentId(studentId)
                                    courseViewModelStudentInsertion.setCourseCode(chosenCourseCode)
                                    courseServiceResult = courseService.insertStudentToActiveCourse(
                                        courseViewModelStudentInsertion)
                                    if courseServiceResult == True:
                                        print("{0} kurs koduna sahip derse kaydoldunuz.".format(chosenCourseCode))
                                        yesNo = input("Başka bir derse kaydolmak istiyor musun ?(yes/no)")
                                        if yesNo == "yes":
                                            continue
                                elif nestedChose == 2:
                                    break
                        elif choseStudent == 2:
                            print("Kayıtlı Olduğum Kurslar")
                            print("Kurs Kodu  |  Kurs Adı")
                            courseViewModelEnrollmentCourseByStudentId = CourseViewModelEnrollmentCourseByStudentId()
                            courseViewModelEnrollmentCourseByStudentId.setStudentId(studentId)
                            courseServiceViewModelList = courseService.getEnrolledCoursesOfStudentByStudentId(
                                courseViewModelEnrollmentCourseByStudentId)
                            for course in courseServiceViewModelList:
                                print("{0}        {1}".format(course.getCourseCode(), course.getCourseName()))
                            while True:
                                print("Kurs İşlemleri")
                                print("1-Dersi Bırak")
                                print("2-Ana Menüye Geri Git")
                                answer = input("Seçiminizi Giriniz : ")
                                if int(answer) == 1:
                                    enterCourseCode = input("Lütfen bırakmak istediğiniz dersin kodunu giriniz : ")
                                    courseViewModelDropCourse = CourseViewModelDropCourse()
                                    courseViewModelDropCourse.setCourseCode(enterCourseCode)
                                    courseViewModelDropCourse.setStudentId(studentId)
                                    dropProcessResult = courseService.dropCourseByStudent(courseViewModelDropCourse)
                                    if dropProcessResult == True:
                                        print("{0} koduna sahip dersten başarılı bir şekilde çekildiniz.".format(
                                            enterCourseCode))
                                        yesNo = input("Başka bir işlem yapmak istiyor musun ?(yes/no)")
                                        if yesNo == "yes":
                                            continue
                                        elif yesNo == "no":
                                            break
                                    elif dropProcessResult == False:
                                        print("Kurstan çekilme işlemi yapılamadı.")

                                elif int(answer) == 2:
                                    break
                        elif choseStudent == 3:
                            courseCode = input("Kurs kodunu giriniz : ")
                            courseViewModelCode = CourseViewModelCode()
                            courseViewModelCode.setCourseCode(courseCode)
                            result = courseService.getByCode(courseViewModelCode)
                            if isinstance(result, CourseViewModel):
                                print(
                                    " | Kurs Kodu : {0} | Kurs Adı : {1} | Başlangıç Tarihi : {2} | Bitiş Tarihi : {3} | Fakülte Kodu : {4} |".format(
                                        result.getCourseCode(), result.getCourseName(),
                                        result.getStartDate(), result.getEndDate(),
                                        result.getFacultyCode()))
                                print(" Eğitmen ve Eğitmentler")
                                i = 1
                                for professor in result.getProfessorList():
                                    print("     {0}.Professor : {1}".format(i, professor.getName()))
                                    i += 1

                            elif isinstance(result, bool):
                                print("Girmiş olduğunuz ders koduna ait bir kayıt bulunmamaktadır.")
                        elif choseStudent == 4:
                            exit()

                else:
                    wrongCounter += 1
                    if wrongCounter == 3:
                        print("Öğrenci hesabı şifrenizi 3 defa yanlış girmenizden dolayı hesabınız kapatılmıştır.")
                        break
            elif isinstance(result, bool):
                print("Sistemde kayıtlı olmayan bir öğrenci numarası girdiniz.")
                continue
    elif chose == 2:
        print("Eğitmen Giriş Sayfasına Hoş Geldiniz.")
        while True:
            staffId = input("Eğitmen Numaranızı Giriniz   : ")
            password = input("Parolanızı Giriniz          : ")
            professorViewModelGetById = ProfessorViewModelGetById()
            professorViewModelGetById.setStaffId(staffId)
            result = professorService.getById(professorViewModelGetById)
            if isinstance(result, ProfessorViewModel):
                if result.getPassword() == password:
                    print("Eğitmen Yönetim Paneli")
                    while True:
                        print("1-Aktif Kurslarım")
                        print("2-Kurs Arama")
                        print("3-Yeni Kurs Oluştur")
                        print("4-Kurs Güncelleme")
                        print("5-Çıkış")
                        chose = int(input("Seçiminizi Giriniz : "))
                        if chose == 1:

                            print("Kayıtlı Olduğum Kurslar")
                            print("Kurs Kodu  |  Kurs Adı")

                            courseViewModelEnrollmentProfessorByStaffId = CourseViewModelEnrollmentProfessorByStaffId()
                            courseViewModelEnrollmentProfessorByStaffId.setStaffId(staffId)
                            courseServiceViewModelList = courseService.getEnrolledCoursesOfProfessorByStaffId(
                                courseViewModelEnrollmentProfessorByStaffId)
                            for course in courseServiceViewModelList:
                                print("{0}        {1}".format(course.getCourseCode(), course.getCourseName()))
                            print("**********Kurs Listesi Sonu***********\n")
                        elif chose == 2:
                            while True:
                                courseCode = input("Kurs kodunu giriniz : ")
                                courseViewModelCode = CourseViewModelCode()
                                courseViewModelCode.setCourseCode(courseCode)
                                result = courseService.getByCode(courseViewModelCode)
                                if isinstance(result, CourseViewModel):
                                    print(
                                        " | Kurs Kodu : {0} | Kurs Adı : {1} | Başlangıç Tarihi : {2} | Bitiş Tarihi : {3} | Fakülte Kodu : {4} |".format(
                                            result.getCourseCode(), result.getCourseName(),
                                            result.getStartDate(), result.getEndDate(),
                                            result.getFacultyCode()))
                                    print(" Eğitmen ve Eğitmentler")
                                    i = 1
                                    for professor in result.getProfessorList():
                                        print("     {0}.Professor : {1}".format(i, professor.getName()))
                                        i += 1
                                    break
                                elif isinstance(result, bool):
                                    print("Girmiş olduğunuz ders koduna ait bir kayıt bulunmamaktadır.")
                        elif chose == 3:
                            print("*********Yeni Kurs Oluşturma***********")
                            courseCode = input("Kurs Kodu Giriniz               :")
                            courseName = input("Kurs Adı Giriniz                :")
                            facultyCode = input("Fakülte Kodunu Giriniz         :")
                            startDate = input("Başlangıç Tarihini Giriniz       :")
                            endDate = input("Bitiş Tarihini Giriniz             : ")
                            staffId = input("Eğitmen Numaranızı Giriniz         :")
                            unitPrice = int(input("Birim Ücreti Giriniz         :"))
                            totalHour = int(input("Toplam Ders Saatini Giriniz  :"))
                            courseViewModelInsertion = CourseViewModelInsertion()
                            courseViewModelInsertion.setStaffId(staffId)
                            courseViewModelInsertion.setCourseCode(courseCode)
                            courseViewModelInsertion.setCourseName(courseName)
                            courseViewModelInsertion.setFacultyCode(facultyCode)
                            courseViewModelInsertion.setStartDate(startDate)
                            courseViewModelInsertion.setEndDate(endDate)
                            courseViewModelInsertion.setUnitPrice(unitPrice)
                            courseViewModelInsertion.setTotalHour(totalHour)
                            result = courseService.insert(courseViewModelInsertion)
                            if result == True:
                                print("Yeni Kurs başarılı bir şekilde oluşturuldu")
                        elif chose == 4:
                            print("Kurs Bilgilerini Güncelleme")
                            courseCode = input("Güncelleme yapmak istediğiniz kursun kodunu giriniz : ")
                            courseViewModelCode = CourseViewModelCode()
                            courseViewModelCode.setCourseCode(courseCode)
                            result = courseService.getByCode(courseViewModelCode)
                            if isinstance(result, CourseViewModel):
                                print("{0} Kurs koduna ait dersin bilgilerini güncelleme ekranı".format(courseCode))
                                print("1-Kurs Adı : {0}".format(result.getCourseName()))
                                print("2-Başlangıç Tarihi : {0}".format(result.getStartDate()))
                                print("3-Bitiş Tarihi : {0}".format(result.getEndDate()))
                                print("4-Fakülte Kodu : {0}".format(result.getFacultyCode()))
                                print("5-Ana Menüye Dön")
                                chose = int(input("Seçinizi Giriniz : "))
                                if chose != 5:
                                    courseViewModelUpdate = CourseViewModelUpdate()
                                    courseViewModelUpdate.setCourseName(result.getCourseName())
                                    courseViewModelUpdate.setCourseCode(result.getCourseCode())
                                    courseViewModelUpdate.setStartDate(result.getStartDate())
                                    courseViewModelUpdate.setEndDate(result.getEndDate())
                                    courseViewModelUpdate.setFacultyCode(result.getFacultyCode())
                                    if chose == 1:
                                        courseName = input("Yeni Kurs Adını Giriniz : ")
                                        courseViewModelUpdate.setCourseName(courseName)
                                    elif chose == 2:
                                        startDate = input("Yeni Balangıç Tarihi Belirleyiniz : ")
                                        courseViewModelUpdate.setStartDate(startDate)
                                    elif chose == 3:
                                        endDate = input("Yeni Bitiş Tarihi Belirleyiniz : ")
                                        courseViewModelUpdate.setEndDate(endDate)
                                    elif chose == 4:
                                        facultyCode = input("Yeni Fakülte Kodunu Giriniz :")
                                        courseViewModelUpdate.setFacultyCode(facultyCode)
                                    result = courseService.update(courseViewModelUpdate)
                                    if result == True:
                                        print("Kurs Bilgileri Başarılı bir şekilde güncellendi.")
                                        courseViewModelCode = CourseViewModelCode()
                                        courseViewModelCode.setCourseCode(courseCode)
                                        result = courseService.getByCode(courseViewModelCode)
                                        if isinstance(result, CourseViewModel):
                                            print(
                                                " | Kurs Kodu : {0} | Kurs Adı : {1} | Başlangıç Tarihi : {2} | Bitiş Tarihi : {3} | Fakülte Kodu : {4} |".format(
                                                    result.getCourseCode(), result.getCourseName(),
                                                    result.getStartDate(), result.getEndDate(),
                                                    result.getFacultyCode()))
                                            print(" Eğitmen ve Eğitmentler")
                                            i = 1
                                            for professor in result.getProfessorList():
                                                print("     {0}.Professor : {1}".format(i, professor.getName()))
                                                i += 1

                            else:
                                print("{0} kurs koduna ait herhangi bir kurs bulunamamıştır.".format(courseCode))
                        elif chose == 5:
                            exit()
