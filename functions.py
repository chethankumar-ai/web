# def voting_age(n,id):
#     if n>=18 and id=="yes":
#         print("eligible")
#     else:
#         print("not eligible")

# voting_age(int(input("ENTER THE AGE:")),input("enter the voter id yes or no:"))10

# def triangle(s1,s2,s3):
#     if s1==s2 and s2==s3:
#         print("equilateral triangle")
#     elif s1==s2 or s2==s3 or s3==s1:
#         print("isoscles triangle")

# triangle(10,10,10)

#write a program to denote season based on month
# def season(n):
#     if n==1 or n==11 or n==12:
#         print("winter")
#     elif n==2 or n==3:
#         print("spring")
#     elif n==4 or n==5 or n==6:
#         print("summer")
#     elif n==7 or n==8 or n==9:
#         print("rainy/mansoon")
#     elif n==10:
#         print("autumn")

    
# season(int(input("enter the season")))

# in a railway station there are four passangers find the oldest among the passesner
# def oldest():
#     p1=int(input("enter the p1 age:"))
#     p2=int(input("enter the p2 age:"))
#     p3=int(input("enter the p3 age:"))
#     p4=int(input("enter the p4 age:"))
#     if p1>p2 and p1>p3 and p1>p4:
#         print("p1 is greater age among four")
#     elif  p2>p3 and p2>p3 and p2>p4:
#         print("p2 is greater age among four")
#     elif p3>p4:
#         print("p3 is greater age among the four")
#     else:
#         print("p4 is greater age among the four")

# oldest()

# write a progring is positive or negative number
# def pos_nev(n):
#     if n>0:
#         print("positive")
#     elif n<0:
#         print("negative")
#     else:
#         print("zero")

# pos_nev(int(input("Enter the number")))
 
# write a program check whether a a women can travell free of cost or not
def free_travell():
    gender=input("enter the gender male/female:")
    if gender == "female":
        state=input("enter the state")
        if state=="karnataka":
            id=input("enter the id yes/no")
            if id =='yes':
                print("you can travell without money")
    else:
        print("not eligible")

free_travell()

