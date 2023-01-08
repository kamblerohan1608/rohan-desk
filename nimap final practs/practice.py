# Q.1

# total = 0
# i=1
# while i<=10:
#     num =  int(input('Enter the number : '))
#     total = total + num
#     i+=1
# print('The Total Is : ',total,' And The Average Is : ' , total/10)

# Q.2

# *
# **
# ***
# ****
# b.
#    *  
#  *** 
# *****
#  *** 
#    *  
# c.
# 1010101010
#  1010101
#   10101 
#    101  
#     1   

# a.

# n=int(input('Enter the number : '))

# i=1
# while i<=n:
#     j=1
#     while j<=i-1:
#         print(' ',end=' ')
#         j+=1
#     k=n
#     while k>=i:
#         print('*',end=' ')
#         k-=1
#     l=n
#     while l>=i+1:
#         print('*',end=' ')
#         l-=1
#     i+=1
#     print()
# m=1
# while m<=n-1:
#     o=n
#     while o>=m+2:
#         print(' ',end=' ')
#         o-=1
#     p=1
#     while p<=m+2:
#         print('*',end=' ')
#         p+=1
#     q=1
#     while q<=m-1:
#         print('*',end=' ')
#         q+=1

#     m+=1
#     print()




# n=int(input('Enter the number : '))

# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print('*',end=' ')
#         j+=1
#     k=n
#     while k>=i+1:
#         print(' ',end=' ')
#         k-=1
    
#     l=n
#     while l>=i+2:
#         print(' ',end = " ")
#         l-=1

#     m=1
#     while m<=i:
#         if m != n:
#             print('*',end=' ')
#         m+=1

#     print()
#     i+=1

# i=1
# while i<=n-1:

#     j=n
#     while j>=i+1:
#         print('*',end=' ')
#         j-=1
    
#     k=1
#     while k<=i-1:
#         print(' ',end=" ")
#         k+=1

#     l=1
#     while l<=i:
#         print(' ',end=' ')
#         l+=1
    
#     m=n
#     while m>i:
#         print('*',end=" ")
#         m-=1

#     print()
#     i+=1


# n=int(input('Enter the number : '))

# i=1
# while i<=n:

#     j=n
#     while j>=i+1:
#         print(' ',end=' ')
#         j-=1
#     k=1
#     while k<=i:
#         print('*',end=' ')
#         k+=1
#     l=1
#     while l<=i-1:
#         print('*',end=' ')
#         l+=1

#     print()
#     i+=1

# i=1
# while i<=n-1:

#     j=1
#     while j<=i:
#         print(' ',end =' ')
#         j+=1

#     k=n
#     while k>=i+1:
#         print('*',end=' ')
#         k-=1

#     l=n
#     while l>=i+2:
#         print('*',end=' ')
#         l-=1

#     print()
#     i+=1




# n=int(input('Enter the number : '))

# i=1
# while i<=n:

#     j=n
#     while j>=i+1:
#         print(' ',end=' ')
#         j-=1


#     k=1
#     while k<=i:
#         print('*',end=' ')
#         k+=1

#     print()
#     i+=1

# i=1
# while i<=n-1:

#     j=1
#     while j<=i:
#         print(' ',end=' ')
#         j+=1

#     k=n
#     while k>=i+1:
#         print('*',end=' ')
#         k-=1

#     print()
#     i+=1


# Q.

# 10101|0101
#  1010|101
#   101|01 
#    10|1  
#     1   


# n=int(input('enter The number : '))


# i=1
# while i<=n:

#     k=1
#     while k<=i-1:
#         print(' ',end='')
#         k+=1

#     j=n-i+1
#     j=(j*2)-1
#     while j>=1:
#         if j%2==0:
#             print('0',end='')
#         else:
#             print('1',end='')
#         j-=1

#     print()
#     i+=1


# prime number with while

# n=int(input('Enter The Number : '))

# num=[]
# i=n
# while i>1:
#     j=i
#     div=0
#     while j>=1:
#         if i%j==0:
#             div+=1
#         j-=1
#     if div<=2:
#         num.append(str(i))
#     i-=1

# print(f"The Prime Numbers between {n} till 1 are {','.join(num)}")





# sorting techniques 

# Bubble sort 


ls=[5,4,3,2,1,0,10,43,2]

# for i in range(0,len(ls)-1):
#     for j in range(0,len(ls)-i-1):
#         if ls[j] > ls[j+1]:
#             ls[j],ls[j+1] = ls[j+1],ls[j]

# print(ls)


# for i in range(len(ls)-1,0,-1):
#     for j in range(i):
#         if ls[j]<ls[j+1]:
#             ls[j],ls[j+1] = ls[j+1],ls[j]

# print(ls)



# i=len(ls)-1
# while i>=1:
#     j=0
#     while j<i:
#         if ls[j] > ls[j+1]:
#             ls[j],ls[j+1] = ls[j+1],ls[j]
#         j+=1
#     i-=1
# print(ls)



# selection sort : 

# ls=[5,6,7,10,15,28,2,4,0,35]

# def descendingSelectionSort(MyList):
#     for i in range(len(MyList) - 1):
#         minimum = i
#         for j in range(len(MyList)-1,i,-1):
#             if(MyList[j] < MyList[minimum]):
#                 minimum = j
#         if(minimum != i):
#             MyList[i], MyList[minimum] = MyList[minimum], MyList[i]
#     return MyList

# print(descendingSelectionSort(ls))


# ls=[5,6,7,10,15,28,2,4,0,35]


# for i in range(len(ls)-1):
#     min=i
#     for j in range(len(ls)-1,i,-1):
#         if ls[j] > ls[min]:
#             min=j
#     if min!=i:
#         ls[i],ls[min]=ls[min],ls[i]
# print(ls)


# for i in range(len(ls)-1,0,-1):
#     for j in range(i):
#         if ls[j]>ls[j+1]:
#             ls[j],ls[j+1]=ls[j+1],ls[j]

# print(ls)


# for i in range(len(ls)-1,0,-1):
#     for j in range(i):
#         if ls[j] > ls[j+1]:
#             ls[j],ls[j+1]=ls[j+1],ls[j]

# print(ls)

# for i in range(len(ls)-1):
#     min=i
#     for j in range(len(ls)-1,i,-1):
#         if ls[j]>ls[min]:
#             min=j
#     if min != i:
#         ls[i],ls[min]=ls[min],ls[i]

# print(ls)


ls=[5,6,7,10,15,28,2,4,0,35]

# i=len(ls)-1
# while i>=1:
#     j=0
#     while j<i:
#         if ls[j]>ls[j+1]:
#             ls[j],ls[j+1]=ls[j+1],ls[j]
#         j+=1
#     i-=1
# print(ls)


# bubble sort for while 

# for i in range(len(ls)-1,0,-1):
#     for j in range(i):
#         if ls[j]>ls[j+1]:
#             ls[j],ls[j+1]=ls[j+1],ls[j]

# print(ls)

# i=len(ls)-1
# while i>=1:

#     j=0
#     while j<i:
#         if ls[j]>ls[j+1]:
#             ls[j],ls[j+1]=ls[j+1],ls[j]
#         j+=1
#     i-=1
# print(ls)


# selection sort 

for i in range(len(ls)-1):
    min=i
    for j in range(len(ls)-1,i,-1):
        if ls[j]<ls[min]:
            min=j
    ls[i],ls[min] = ls[min],ls[i]

print(ls)