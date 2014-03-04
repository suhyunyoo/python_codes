#!/usr/bin/env python

def divide(a,b):
	q = a/b
	r = a - q*b
	return (q,r)

def Gugu(n):
	result = []
	for i in range(1,10):
		print(n*i)
		result.append(n*i)
	return result
	