
########## Variables 
first_name = 'David'
last_name = 'Dourvash'
country = 'Iran'
city = 'Esfahan'
age = 33
is_married = False
skills = ['R', 'Sql', 'Python', 'PBI', 'SPSS']
person_info = {
    'first_name' : 'David', 
    'last_name' : 'Dourvash', 
    'country' : 'Iran', 
    'city' : 'Esfahan'
}


print('Hello, World!') # The text Hello, World! is an argument
print('Hello', ',', 'World', '!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument



print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)


########## Declaring Multiple Variable in a Line

first_name, last_name, country, age, is_married = 'David', 'Dourvash', 'Esfahan', 33, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)



first_name = input('What is your name : ')
age = input('How old are you ? ')

print(first_name)
print(age)


########## Checking Data types and Casting
first_name, last_name, country, city, age = 'David', 'Dourvash', 'Iran', 'Esfahan', 33
print(type('David'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'David','age':33, 'is_married':False}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set

num_int = 10
print('num_int', num_int)
num_float = float(num_int)
print('num_float', num_float)


# float to int
gravity = 9.81
print(int(gravity))             # 9

# str to int or float
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6


# str to list
first_name = 'David'
print(first_name)               # 'David'
first_name_to_list = list(first_name)
print(first_name_to_list)




########## Exercises - Day 2
