'''Pandas is a library used to implement data structure data-frame and series,
here series is a single-dimensional array and data-frame is a multi-dimensional array'''
import pandas as pd#here pd is an alias
d1={'a':10,'b':20,'c':30}#d1 is dictionary here so in output index values will be key value and values will be printed as output only
s1=pd.Series(d1)#Series object is one-dimensional labelled array
print(s1)
