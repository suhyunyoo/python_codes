#!/usr/bin/env python
import os

print "######################################################################"
print "Python practice #8 26 November 2013"
print "Written by Daniel Yoo"
print ""


###various way to find path
print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, file = os.path.split(full_path)
print(path + ' --> ' + file + "\n")

print("This file directory only")
print(os.path.dirname(full_path) + "\n")

##Find current working directory
str1=os.getcwd()
str2=str1.split('/')
n=len(str2)

path=str2[n-1]
print path