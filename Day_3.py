# list_1 = [3,6,4,5,6,3]        
# first_sum = sum(list_1)       
# second_sum = sum(set(list_1))*2                     #List 
# res = second_sum-first_sum
# print(res)

# n = int(input("Enter input : "))
# fact = 1
# for i in range(n,1,-1):                              #Factorial
#     fact *= i        #(fact = fact*i)
# print(fact)

# n = 5
# fact = 0
# for i in range(1,11):                                  #Sum of factorial of 1st 10 of input
#     fact = n*i + fact
# print(fact)

# list_1 = [1,7,9,7,4,6,2]
# target = 7
# for i in range(len(list_1)):                          #linear search
#     if target==list_1[i]:
#         print(i)
#         break

# list_1 = [1,2,3,4,5,6,7,8,9,10]
# target = int(input("Enter the Target : "))
# start = 0
# end = len(list_1)-1
# index = -1
# while(start<=end):
#     middle = (start+end)//2
#     if list_1[middle]==target:
#         index = (middle)
#         break
#     elif list_1[middle]>target:
#         end = middle-1
#     elif list_1[middle]>target:
#         start = middle+1
# if index != -1:
#     print(index)
# else:
#     print("Not found")



# n=int(input("Enter the number of stars: "))
# for i in range(1,n+1):                          #star pattarn                           
#     print("* "*i)



# n=int(input("Enter number of stars:"))
# for i in range(n,0,-1):                      #inverted star pattrn
#     print("* "*i)


# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):                  # number patten
#         print(j,end=" ")
#     print()


# n=int (input())
# for i in range(1,n+1):
#     str1=""
#     for j in range(1,i+1):        #number pattern
#         str1+=str(j)+" "
#     print(str1)



# n=int (input())
# for i in range(1,n+1):                      
#     for spaces in range(1,n-i+1):
#        print(" ",end=" ")                   # pyramid
#     for maps in range(1,2*i):
#         print("*",end=" ")
#     print()  


# n=int(input())
# for i in range(1,n+1):                 # (n-i)= for spaces pyramid
#     print(" "*(n-i)+"* "*i)



# n=int(input())
# for i in range(n,0,-1):              #reverse pyramid
#     print(" "*(n-i)+"* "*i)


# n=int(input())
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print("* "*i)                            # hollow triangle
#     else:
#         print("*"+" "*(2*i-3)+"*")


# n=int(input())
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print(" "*(n-i)+"* "*i)
#     else:
#         print(" "*(n-1)+" "*(2*i-2)+"*"+" "*(n-1))





        