from SettingClasses import Class
import os

if __name__ == '__main__':
    my_class=Class()
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
            if n == 1:
                name=input("Nhap ten sinh vien can tim: ")
                print(my_class.find_name(name))
                print("Nhan Enter de tiep tuc!")
                i=input()
                continue
            elif n ==2:
                id=input("Nhap ma so sinh vien can tim: ")
                print(my_class.find_id(id))
                print("Nhan Enter de tiep tuc!")
                i=input()
                continue
        if n < 0 and n > 3:
            print("Ban nhap sai, vui long nhan enter de nhap lai.")
            i=input()
