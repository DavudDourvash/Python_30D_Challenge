# Exercises - Day 2

## Exercises: Level 1

# Day 2: 30 Days of python programming


first_name = 'David'
last_name = 'Dourvash'
full_name = 'David Dourvash'
country = 'Iran'
city = 'Esfahan'
age = 33
year = 2023
is_married = False
is_true = True
is_light_on = True
first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = 'Davoud', 'Dourvash', 'David Dourvash', 'Iran', 'Esfahan', 33, 2023, False, True, True

## Exercises: Level 2
### 1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

### 2
print(len(first_name))

### 3
len(first_name) == len(last_name)

### 4
num_one = 5
num_two = 4
#### i
num_one_add_two = num_one + num_two
#### ii
num_one_diff_two = num_one - num_two

#### iii
num_one_product_two = num_one * num_two

### iv
num_one_division_two = num_one / num_two

### v

### vi
num_one_power_two = num_one ** num_two


### vii
import math
num_one_floor_division_two = math.floor(num_one / num_two)


### 5
# The radius of a circle is 30 meters. 

#### i 
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
radius = 30
area_of_circle = math.pi * (radius ** 2)


#### ii
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * math.pi * radius


#### iii
# Take radius as user input and calculate the area.
import math
radius = int(input('Enter the radius : '))
area_of_circle = math.pi * (radius ** 2)



### 6
def person_information():
    global first_name, last_name, country, age
    first_name = input('first_name : ')
    last_name = input('last_name : ')
    country = input('country : ')
    age = int(input('age : '))
    
person_information()


### 7
help('keywords')

