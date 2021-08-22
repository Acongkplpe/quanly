import numpy as np
arr1 = np.array([0]*10,dtype = int)
arr2 = np.array([0]*10,dtype = int)
arr3= np.array([0]*10,dtype = int)
def show(n):
    for i in range(n):
        print(arr1[i],end='   ')
def inputt(arr1,n):
    for i in range(n):
        arr1[i]=int(input('nhap vao mang '+str(i+1)+'la: '))
    return arr1
def chen(mang,pos,value):
    mang[n] = value
    print(mang)
    for i in range(len(mang)-1,pos,-1):
        mang[i],mang[i-1]= mang[i-1],mang[i]
    return mang
#def ghep_xapxeptunhoden_lon(mang1,mang2,mang3):
        
#begin
n = int(input('so luong can nhap vao mang:  '))
inputt(arr1,n)
pos = int(input('vi tri phan tu can chen la: '))
value= int(input ('nhap phan tu ma ban can chen'))  
chen(arr1,pos,np.array([value],dtype = int))
show(n)
#ghep_xapxeptunhoden_lon(arr1,arr2,arr3)
    