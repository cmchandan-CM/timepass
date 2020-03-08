# problem:::
# input: 6
# output:1101110
# define:  binary OF 6 is 110
#  binary OF 110 is 1101110
def bintodec(val):
    str = val
    res=''
    str = str[::-1]
    list = []
    for i in range(len(str)):
        if (str[i] == '1'):
            list.append(i)
    k = 0
    for i in list:
        k += pow(2, i)
    return k
def dectobin(val):
    #val = int(input("enter the integer value"))
    temp = val
    list = []
    sum = 0
    k = True

    while k == True:
        j = 0
        while int(pow(2, j)) <= val:
            j += 1
        list.append(int(pow(2, j - 1)))
        val = val - int(pow(2, j - 1))
        sum += int(pow(2, j - 1))
        if (sum == temp):
            k = False
        else:
            k = True
    list2 = []
    for i in range(len(list)):
        g = 0
        while pow(2, g) <= list[i]:
            if pow(2, g) == list[i]:
                list2.append(g)
            g += 1
    list3 = []
    for i in range(list2[0] + 1):
        list3.append('0')
    for i in range(len(list3)):
        for i in list2:
            list3[i] = '1'
    str1 = ''
    for i in range(len(list3)):
        str1 += str(list3[i])
    res=str1[::-1]
    return res
val=int(input("enter the integer value : "))
val=dectobin(val)
val=dectobin(int(val))
print(val)
