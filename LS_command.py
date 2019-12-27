#ls command
import os
import sys


# current directory
i=os.getcwd()
print(i)

#Name of the directory whose file we want to list
l =input("(Name_of the directory $ ")

#Changing to specific directory
os.chdir(l)
# current directory after change
i=os.getcwd()
print(i)

#to list the files and sub directory in the given directory
print(os.listdir(i))
z=os.listdir(i)


"""
#NOT IMPORTANT: WE ARE TRANSFERING IT TO THE LIST IF WE WANT TO STORE
p=[l for l in z]
print(p)
#[i in os.listdir(DIR_NAME)]
#print(i)

"""
