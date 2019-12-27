#ls command
import os
import sys
import time
file_name= sys.argv[1:]
#Name of the directory whose file we want to list
#DIR_NAME= input("Name_of the directory $ ")
# current directory
i=os.getcwd()
print(i)
#to list the file of specific directory
l=input("(Please provide the input in'' for target directory ) $ ")
os.chdir(l)
#i= sys.argv[1:0]
i=os.getcwd()
print(i)
print(os.listdir(i))
z=os.listdir(i)
p=[l for l in z]
print(p)

#To check the file already exist or not
#o =input("(Please provide the input in '' for new file ) $ ")
#file_name= sys.argv[1:0]
print(file_name)
for i in file_name:
    if i in p:  #if file already exist then the time stam will be changed
        os.utime(i)#This is use to modify the date

    else:  #else new emplty file will be created
        with open(i,'w') as f:
            pass
