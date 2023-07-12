#Question 1
def hello_name(user_name):
    """Write a function to print 'hello_USERNAME!' USERNAME is the input"""
    print("hello_"+user_name+"!")
hello_name('USERNAME')

#Question 2
def first_odds():
    """Write a function, first_odds that prints the odd numbers 1-100 and reutnrs nothing"""
    print(list(range(1,100,2)))
first_odds()

#Question 3
def max_num_in_list(a_list):
    #Return the max number of a given list
    print(max(a_list))

max_num_in_list([5,10,12,6])
max_num_in_list([5,10,12,6,22,13,46,1200])

#Question 4
def is_leap_year(a_year):
    #Write a function to return if the given year is a leap year.

leap_year = input("Input a year, and I will tell you if it is a leap year ")
leap_year = int(leap_year)

if leap_year % 4 == 0:
    print("That is a leap year!")

elif leap_year % 400 == 0:
    print("That is a leap year!")

elif leap_year % 100 == 0:
    print("That is NOT a leap year.")

else:
    print("That is NOT a leap year.")

# Question 5
def is_consecutive(a_list):
    #Check if numbers in a list are consecutive 