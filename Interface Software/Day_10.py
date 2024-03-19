# # Input Stream
# '''
# Input Stream means the flow of data between the input source and the reciving source
# Input Source may be from the comand promt , from any file etc where the reciving sources may be a file or may a comandpromt etc.
# Here the main intension is how to pass the datas between the different sources.
# Following are the steps 
#     1. Make the connection between two sources by using pipelines and that pipe line we are calling as Stream.Thoese streaming pipeline can contain bit stream where only bits will pass and the second is the character steam where only character will pass.
#     2.There may a file in any format which we need to open it in some mode may be read mode or write mode
    
#     Example 1:
#         write to a file 
#         -create a file say(gift.txt)
#         -as we are writing the mode is w(write)
        
# '''




import os
import sys


# f = open("gift.txt",'w')
# print(type(f))
# str = input("Enter")
# f.write(str)
# f.close()

# '''
# f is referance for the TextIOWrapper
# '''
# # Ex-2 File Handeling with read mode 
#     # step1 - connection to be open with a destination file where the mode is read mode
#             #    now we are a function as a read so that the content of the file can be read and return type of the string
# f = open("gift.txt",'r')
# # print(type(f))
# str = f.read()
# print(str)
# f.close()

# f = open("gift.txt",'a')
# str = input("enter")
# f.write("\t"+str)
# f.close()

# # # take the file name as input (gift.txt)
# # #find the file path.
# # # #if it is matching then open the file in read mode if not matching it will file does not exists and it will exit from the comand prompt
# # # as the mode is read read the content of the file and read

# fname = input("enter the file name")
# print(os.path)
# if os.path.isfile(fname):
#     f= open(fname,"r")
# else:
#     print(fname+"does not exit")
#     sys.exit()
    
# print("Contains are ")
# str =f.read()
# print(str)
# f.close()

# # #Ex- 3

# a = open("gift.txt",'r')
# s = a.readline()
# print(type(s))

# s1 = s[1]
# print(s1)
# print(s1[:1])

# #Ex-4
# f1 = open("3AfW.gif","rb")
# f2 = open("gift.gif","wb")
# bytes = f1.read()
# f2.write(bytes)
# f1.close()
# f2.close()


# #copy the contain of a file to another file (ABC.py to ABC1.py)
# f1 = open("ABC.py",'r')
# text = f1.read()
# f2 = open("ABC1.py",'w')
# f2.write(text)

# #There are multiple lines in a file(*text) now print {using for loop}
# #   last line last word
#     # first line last word
#     #first line last letter
#     # all the first lines
    
# file1 = open("NEW.txt","r")
# line = file1.readlines()

# for i in range(len(line)):
#     print(line[i],end='')
# print("\n")
# print(line[-1])    
    
# '''
# OBJECT INPUT STREAM AND OBJECT OUTPUT STREAM BY USING PICKLE
# Pickle is a class in Python
# # In the earlier example, we created a file and passed the reference string to a file.
# # We also copied an image.
# # If we want to pass an object of a class from one machine to another machine, then follow these steps:
# # 1- Import pickle, which is serialization and deserialization.
# # 2- Make an object of a class. Then, using the serialization concept, where it uses a bit stream, a function is written so that the object can pass to a file.
# # 3- Then from that file, we have to read the content of the file using two functions of the file for writing of the object:
# #    - dump: which is the dumping of the object.
# #    - load: To load the content of the file into the object input stream, and the object state can be deserialized to the original object.
# '''