#Chay chuong trinh: mo bang Vs code nhan phai chuot chon Run Python File in Terminal
import unittest
from SettingClasses import Class
from datetime import date

class TestClass(unittest.TestCase):
    #Kiem tra ham doc va viet file
    def test_write_read_file(self):
        my_class=Class()
        my_class.write_file("test_file.bin",'1234','Dat','36291')
        my_class.read_file("test_file.bin")
        self.assertEqual(my_class.list_student[len(my_class.list_student)-1],['1234','Dat','13/05/1999'],"Ham doc va viet file bi loi!")
    #Kiem tra ham tim sinh vien theo ten
    #Goi them ham doc file
    def test_find_name(self):
        my_class=Class()
        my_class.read_file("test_file.bin")
        self.assertEqual(my_class.find_name("Dat"), ['1234', 'Dat', '13/05/1999'],"Ham tim sinh vien theo ten bi loi!")
    #Kiem tra ham tim sinh vien theo ma so sinh vien
    #Goi them ham doc file
    def test_find_id(self):
        my_class=Class()
        my_class.read_file("test_file.bin")
        self.assertEqual(my_class.find_id("1234"), ['1234', 'Dat', '13/05/1999'],"Ham tim sinh vien theo ma so sinh vien bi loi!")
    
if __name__ == '__main__':
    unittest.main()