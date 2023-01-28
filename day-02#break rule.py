#break rule
# n=int(input("enter ur no. : "))
# for i in range(0,n+1):
#     if i==8:
#         break
#     print(i)
       
# #=================================================        
#continue rule
# n=int(input("enter ur no. : "))
# for i in range (0,n+1):
#     if i==9:   # When we use continue rule then the loop is no more dependent on any other condition
#         continue
#     print(i)

# #===============================================================================
# Diamond star 
# def triangle(n):
#     for i in range(1,n+1):                                   # 333333333333333333333333333333333
#         print(" "*(n-i) + " *"*(i))
# triangle(10)        


# #==============================================================================
#guessing lottery no. game ...
# lottery_no=45
# guess=1
# ur_no=int(input("try ur no. : "))
# game__over=False
# while not game__over:
#     if ur_no==lottery_no:
#         print(f"hurrey uh won and you guessed {guess}times")
#         game__over=False
#         print("Thank uh for playing , Hope uh enjoyed :)")
#         break

#     elif ur_no<lottery_no:
#         print("oops wrong guess,entered too low ")
#         guess+=1
#         ur_no=int(input("guess again : "))

#     else:
#         print('oops wrong guess,enterd too high ')
#         guess+=1
#         ur_no=int(input("guess again : "))


# #===================================================================================
# n =" ram "
# for i in range(1,15,2):
#     print(n,i)
# for i in range(15,0,-2):
#     print(n,i)

# ###====================================================================
# name = 'harshit   '
# for i in "mohit":
#     print(name,i)
# #==================================================================================
# a=int(input("enter A : "))
# b=int(input("enter B :"))
# c=int(input("enter C :"))
# def add_the_no(a,b,c):
#     return(a+b+c)
# print(add_the_no(a,b,c))

# ##==============================================================================

# def my_name(name):                              
#     return (name[-1])
# print(my_name("Amartya"))

# ##================================================================================
# def odd__even(num):
#     if num%2==0:
#         return ("Even")
#     else:
#         return("Odd")
# print(odd__even(33))  

# ##============================================================================
# def odd_even(num):
#     if num%2 == 0:
#         return ("even")
#     return 'odd'
    
# print(odd_even(1123421))

# ##===============================================================================
# def is_odd_even(num):

#     if num%2 == 0:
#         return True
#     return False
# print(is_odd_even(9))

# ##=======================================================================================
# def even__odd(num):
#     return num%2==0
# print(even__odd(67))

# ##=============================================================================================
# def greater(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# num1=int(input("num1 : "))
# num2=int(input("num2 : "))
# bigger=greater(num1,num2)
# print(f'{bigger} is greater') 


# ##================================================================================================
# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# num1=int(input("num1 : "))
# num2=int(input("num2 : "))
# num3=int(input("num3 : "))
# biggest=greatest(num1,num2,num3)
# print(f'{biggest} is the greatest')


# #==============================================================================
# ##wrong code
# def new_greatest(a,b,c):
#      # bigger = greater(a,b)
#      return greater(greater(a,b),c)
# print(new_greatest(1000,100,10))
# #==============================================================================
# def is_plaindrom(word):
#     reserved_word = word[::-1]
#     if word == reserved_word:
#         return True
#     else:
#         return False
# print(is_plaindrom("naman")) 
# print(is_plaindrom("horse"))   

# ##=================================================================================


# def is_palindrom(word):
#     if word == word[::-1]:
#         return True
#     return False
# print(is_plaindrom(input())) 
# print(is_plaindrom(input()))  

# ##=================================================================================

# def is_palindrom(word):
#     return word == word[::-1]
# print(is_palindrom("naman"))
# print(is_palindrom("abmmba"))

# ##=================================================================================
# ##  output is true
# str1 = str('python')
# str2 = 'python'
# print(str1 == str2,str1 is str2)

# #=================================================================================
# # fibonacci series
# for i in range(1,11):
#      print(i, end =",")

# #================
# def fibonacci_seq(n):
#     a=0
#     b=1
#     if n == 1:
#         print(a)
#     elif n == 2:
#         print(a,b)
#     else:
#         print(a,b, end = " ")
#         for i in range (n-2):
#             c = a+b
#             a = b
#             b = c
#             print(b , end = " ")

# print(fibonacci_seq(20))
# #==============================================================================================
# # scope
# x = 5 # global varibale

# def function():
#     global x
#     x = 8  # local variables
#     return x

# print(x)             # output is 5
# print(function())       # output is 7
# print(x)             # output is 7


# #===============================================================================================
# number = [1,2,3,4]
# print(number)
# print(number[3])

# word = ['hey','think big','iphone']
# print(word)
# print(word[:])
# print(word[:0])
# print(word[:1])
# print(word[:2])
# print(word[:3])

# mixed = ['wonderfull',1,5,'ram',10,'infiniet','hanumaan']
# print(mixed)
# print(mixed[:])
# mixed[1]='two' 
# mixed[1:]='two'
# print(mixed)



# #===========================================================================
# fruit=['papaya','pineapple']
# fruits=['mango','grapes','apple','banana','apple']
# fruits.append('apple')
# fruits.insert(1,'orange')
# fruits.extend(fruit)
# print(fruits)

# ###
# fruits.pop()
# del fruits[3]
# print(fruits)
# fruits.remove('apple')
# print(fruits)



# #============================================================================
# my_name = 'yes i am',' Amartya '.split(' ,')
# print(my_name)



# #### split method
# name, age = input('enter your name and age: ').split(',')
# print(name,age)
# print(age)


# ##########  join method
# charchil_raj = ['yes iam' ,'charchil']
# print(' ,'.join(charchil_raj))




# 
# n=(input("no. : "))  
# j=n
# i=1
# while i<n:
#     j=j*(n-i)
#     i+=1
# print(j)

# c=int(input("no. "))
# num=list(range(0,c+1))
# print(num)

# for k in range(0,int(n)+1):
#     j=k
#     i=1
#     while i<k:
#         j=j*(k-i)
#         i+=1
# print(j)
# if n[0]+n[1]+n[2]==n


# a=['abc','tuv','xyz']
# for i in (range(0,len(a))):
#     b=a[i]
#     c=b[::-1]
#     printlist(c)

# class Animal:
#     def __init__(self,kind,color,legs,domestic,carnivorous):
#         self.animalkind=kind
#         self.animalcolor=color
#         self.animallegs=legs
#         self.animaldomestic=domestic
#         self.animalcarnivorous=carnivorous

# dog=Animal("dog","black and white","four","True",True)
# print(dog.animalkind)
# print(dog.animalcolor)
# print(dog.animallegs)


class Animal:
    def __init__(self,kind,color,legs,domestic,carnivorous):
        self.animalkind=kind
        self.animalcolor=color
        self.animallegs=legs
        self.animaldomestic=domestic
        self.animalcarnivorous=carnivorous

    def printname(self):
        print(self.animalkind,self.animalcolor,self.animaldomestic,self.animalcolor)
dog=Animal("dog","black and white","four","True",True)
dog.printname()
