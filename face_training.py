
from ntpath import join
import os


path = r'C:\Users\ADMIN\Face_mask_detect_Dat\face'
name = 'Dinh Trong Dat' 

personName = name + '.jpg'
dir_img = os.path.join(path,personName)
print(dir_img)