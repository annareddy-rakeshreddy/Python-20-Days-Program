# # # def add(x,y):
# # #     return(x+y)
# # # a=int(input("1:"))
# # # b=int(input("2:"))
# # # c=add(a,b)
# # # print(c)

# # # def fact(n):
# # #     if n<=1:
# # #         return(n)
# # #     return n*fact(n-1)
# # # n=int(input())
# # # print(fact(n))



# # def sum(n):
# #     if n<=2:
# #         return(n)
# #     return n+sum(n-1)
# # n=int(input())
# # print(sum(n))

    
# # def fibb(n):
# #     if n<=1:
# #         return(n)
# #     if n==1:
# #         return 1
# #     return fibb(n-1)+fibb(n-2)





# n = 10
# a, b = 0, 1
# count = 0
# while count < n:
#     print(a, end=" ")
#     a, b = b, a + b
#     count += 1


def fibonacci_with_list(n):
    fib_series=[0,1]
    for i in range(2,n):
        fib_series.append(fib_series[-1]+fib_series[-2])
    return fib_series
print(fibonacci_with_list(10))


