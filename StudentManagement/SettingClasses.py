import pickle
from datetime import date, timedelta

class Student(object):
    def __init__(self, id, full_name, birthday):
        self.__id=id
        self.__full_name=full_name
        self.__birthday=birthday
    def __str__(self):
        return str(str(self.__id).ljust(10)+str(self.__full_name).ljust(30)+self.convert_days_into_birthday(self.__birthday).ljust(15))
    def get_id(self):
        return self.__id
    def get_full_name(self):
        return self.__full_name
    def get_birthday(self):
        return self.__birthday
    #Ham chuyen so ngay thanh ngay thang nam (tinh tu 1/1/1900)
    def convert_days_into_birthday(self, days):
        birthday=timedelta(self.__birthday)+date(1900, 1, 1)
        return str(birthday.strftime('%d/%m/%Y'))

class Class(object):
    def __init__(self):
        self.list_student=[]
    #Ham doc file
    def read_file(self, file_name):
        file=open(file_name, "rb")
        while True:
            try:
                self.list_student.append(pickle.load(file))
            except EOFError:
                break
        file.close()
    #Ham tim sinh vien theo ten
    def find_name(self, name):
        for i in range(len(self.list_student)):
            if self.list_student[i].get_full_name() == name:
                return self.list_student[i]
        return 0
    #Ham tim sinh vien theo ma so sinh vien
    def find_id(self, id):
        for i in range(len(self.list_student)):
            if self.list_student[i].get_id() == id:
                return self.list_student[i]
        return 0
    #Ham viet thong tin sinh vien vao file
    def write_file(self, file_name, id, name, numberdays):
        file=open(file_name, "ab")
        pickle.dump(Student(id, name, numberdays),file)
        file.close()
    #Ham lay thong tin sinh vien
    def add_student(self, file_name):
        id=input("Nhap ma so sinh vien: ")
        name=input("Nhap ten sinh vien: ")
        birthday=input("Nhap ngay thang nam sinh(dd/mm/yyyy): ")
        self.write_file(file_name,id, name, self.convert_birthday_into_days(birthday))
        print("Thong tin sinh vien "+name+" da duoc luu.\n")
    #Ham chuyen ngay/thang/nam thanh so ngay
    def convert_birthday_into_days(self, birthday):
        d, m, y=birthday.split('/')
        return int((date(int(y), int(m), int(d))-date(1900,1,1)).days)
