# problem:
# input: n*n matrix
# 4*5
# # list1=[[26,94,92,15,31],
# #        [74,67,52,56,39],
# #        [92,68,16,31,9],
# #        [21,29,79,39,10]]
# path SENESEESWNN
# OUTPUT :555
# INPUT 3*3
# 123
# 456
# 789
# ESENWSSW
# OUTPUT:32
# ESENWSSW ARE 125632587
# SUM 32=1+2+5+6+3+8+7
# VALUE NOT REPEAT
list1=[]
row1=int(input("enter the row "))
col1=int(input("enter the column"))
for i in range(row1):
    temp=[]
    for j in range(col1):
        temp.append(int(input("enter the element")))
    list1.append(temp)
str1=input("enter the direction ")
sum1=[]
row=0
col=0
sum1.append(list1[row][col])
for i in range(len(str1)):
    if(str1[i]=='s'):
        row+=1
        if(row<row1):
          sum1.append(list1[row][col])
        else:
            row-=1
    elif(str1[i]=='n'):
        row-=1
        if(row>=0):
          sum1.append(list1[row][col])
        else:
            row+=1
    elif(str1[i] == 'w'):
        col -= 1
        if(col>=0):
          sum1.append(list1[row][col])
        else:
            col+=1
    elif(str1[i] == 'e'):
        col += 1
        if(col<col1):
          sum1.append(list1[row][col])
        else:
            col-=1
print(sum1)
sum1.sort()
i=0
while(i<len(sum1)-1):
    if(sum1[i]==sum1[i+1]):
        sum1.pop(i)
    i+=1
print(sum(sum1))
