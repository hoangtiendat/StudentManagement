import pickle
from datetime import date, timedelta

class Class(object):
    def __init__(self):
        self.list_student=[]
    #Ham doc file
    def read_file(self, file_name):
        file=open(file_name, "rb")
        while True:
            try:
                flag=str(pickle.load(file)).split()
                id=flag[0]
                birth=timedelta(int(flag[len(flag)-1]))+date(1900,1,1) #Chuyen numberdays thanh yyyy-mm-dd
                birth=birth.strftime('%d/%m/%Y') # chuyen yyyy-mm-dd thang dd/mm/yyyy
                name=flag[1]
                for i in range(2, len(flag)-1):
                    name+=" "+flag[i]
                self.list_student.append([id, name, birth])
            except EOFError:
                break
        file.close()
    #Ham tim sinh vien theo ten
    def find_name(self, name):
        for i in range(len(self.list_student)):
            if self.list_student[i][1]==name:
                return self.list_student[i]
        return 0
    #Ham tim sinh vien theo ma so sinh vien
    def find_id(self, id):
        for i in range(len(self.list_student)):
            if self.list_student[i][0]==id:
                return self.list_student[i]
        return 0
    #Ham viet thong tin sinh vien vao file
    def write_file(self, file_name, id, name, numberdays):
        file=open(file_name, "ab")
        pickle.dump(id+" "+name+ " "+str(numberdays)+"\n",file)
        file.close()
    #Ham lay thong tin sinh vien
    def add_student(self, file_name):
        id=input("Nhap ma so sinh vien: ")
        name=input("Nhap ten sinh vien: ")
        d, m, y=input("Nhap ngay thang nam sinh(dd/mm/yyyy): ").split('/') #Tach thanh ngay thang nam
        numberdays=(date(int(y), int(m), int(d))-date(1900,1,1)).days #Chuyen dd/mm/yyyy thanh numberdays
        self.write_file(file_name,id, name, numberdays)
        print("Thong tin sinh vien "+name+" da duoc luu.\n")