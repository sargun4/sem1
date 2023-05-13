def pattern(n):
    def upper_triangle(space=0):
        if space==n:
            return None
        else:
            print("* "*(n-space),end="")
            print("  "*2*space+"* "*(n-space))
            return upper_triangle(space+1)
    def lower_triangle(space=n-2):
        if space<0:
            return None
        else:
            print("* "*(n-space),end="")
            print("  "*2*space+"* "*(n-space))
            return lower_triangle(space-1)
    upper_triangle()
    lower_triangle()
n=int(input())
pattern(n)






#  def upper_spaces(space): #no .of spaces in upper pattern
#     if (space == 0):
#         return
#     for i in range(2):
#         print(" ", end = "")

#     upper_spaces(space - 1) # reducing no. of spaces to be printed by 1

# def upperpattern(astrsk_ctr): #astrsk_ctr= no. of asterisks
#     if (astrsk_ctr == 0):
#         return
#     print("*", end = " ")
#     upperpattern(astrsk_ctr - 1)
    

  
# def Upper(n, num):
#     if (n == 0):
#         return
#     upperpattern(n)
#     upper_spaces(2*(num - n)) #spaces printed
#     upperpattern(n)
#     print() #next line
  
#     Upper(n - 1, num)

# #lower pattern
# def lower_spaces(space):
#     if (space == 0):
#         return
#     for i in range(2):
#         print(" ", end = "")
#     lower_spaces(space - 1)# reducing no. of spaces to be printed by 1

# def lowerpattern(astrsk_ctr):
#     if (astrsk_ctr == 0):
#         return
#     print("*", end = " ")
#     lowerpattern(astrsk_ctr - 1)
  
# def Lower(n, num):
  
#     if (n == 0):
#         return
#     lowerpattern(num - n + 1)
#     lower_spaces(2 * n - 2)
#     lowerpattern(num - n + 1)
#     print()#next line
  
#     Lower(n - 1, num)
# print()
# n = int(input())
# Upper(n, n)
# Lower(n, n)



# for i in range(1,n+1):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     for j in range(i):
#         print(" ",end=" ")
#     print()    

# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()    

