from SettingClasses import Class
import os

if __name__ == '__main__':
    my_class=Class()
    def print_student(result): #In ra thong tin sinh vien thanh mot dong
        if result == 0:
            print("Khong tim thay.")
        else:
            print("\n")
            print("Thong tin sinh vien ban can tim.".center(55))
            print("_"*55)
            print("MSSV".ljust(15)+"Ho ten".ljust(30)+"Ngay sinh".ljust(10))
            print("_"*55)
            print(result[0].ljust(15)+result[1].ljust(30)+result[2].ljust(10))
            print("\n")
    while True:
        os.system('cls')
        print("\t\tTuy Chon.")
        print("1. Tim sinh vien theo ten.")
        print("2. Tim sinh vien theo ma so sinh vien.")
        print("3. Them sinh vien.")
        print("0. Thoat!")
        n=int(input("Lua chon cua ban: "))
        if n==0:
            break
        if n==3:
            my_class.add_student("list_student.bin")
            print("Nhan Enter de tiep tuc!")
            i=input()
            continue
        else:
            my_class.read_file("list_student.bin")
            print(my_class.list_student)
            if n == 1:
                name=input("Nhap ten sinh vien can tim: ")
                result=my_class.find_name(name)
                print_student(result)
                print("Nhan Enter de tiep tuc!")
                i=input()
                continue
            elif n ==2:
                id=input("Nhap ma so sinh vien can tim: ")
                result=my_class.find_id(id)
                print_student(result)
                print("Nhan Enter de tiep tuc!")
                i=input()
                continue
        if n < 0 and n > 3:
            print("Ban nhap sai, vui long nhan enter de nhap lai.")
            i=input()
