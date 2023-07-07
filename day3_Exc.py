
age = int('33') #1
height = float(169.3) #2
cplex_num = 1 - 1j #3
type(cplex_num)


# 4
base = int(input('Enter the base : '))
height = int(input('Enter the height : '))
area_triange = 0.5 * base * height
print('area_triange :', area_triange)


# 5
a = int(input('Enter side_a : '))
b = int(input('Enter side_b : '))
c = int(input('Enter side_c : '))

print('perimeter of the triangle : ', a + b + c)


# 6 
length_t = int(input('Enter length : '))
width_t = int(input('Enter width : '))
print('area : ', length_t * width_t)
print('perimeter : ', 2*(length_t * width_t))


# 7
r = float(input('Enter radius : '))
print('area : ', 3.14 * r * r)
print('perimeter : ', 2 * 3.14 * r)

# 8 : Calculate the slope, x-intercept and y-intercept of y = 2x -2
def line_s(xs):
    return 2*xs-2

def slope_1(a, b):
   return (line_s(float(b)) - line_s(float(a))) / b - a
    
# y = 2x-2
slope_1(2, -2)


# 9 : Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

def slope_Euclidean(x1, y1, x2, y2) : 
    import math
    print('Slope is : ', (float(y2) - float(y1)) / (float(x2) - float(x1)))
    print('Euclidean is : ', math.sqrt(
        int((float(y1) - float(x1)) ** 2 +  (float(y2) - float(x2)) ** 2)
        ))
    
    # 10 Compare the slopes in tasks 8 and 9.
    x1, y1, x2, y2 = 2, 2, 6, 10

    slope_1(2, 2) ==  math.sqrt(
        int((float(y1) - float(x1)) ** 2 +  (float(y2) - float(x2)) ** 2)
        )


# 11 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

def y(x, a, b, c):
    x = float(x)
    return a*x**2 + b*x + c

y(2, 1, 6, 9)


def x_roots(x, a, b, c):
    delta = b**2 - 4*a*c
    print('root1 : ', ((-b + math.sqrt(delta))) / 2*a)
    print('root1 : ', ((-b - math.sqrt(delta))) / 2*a)

x_roots(2, 1, 6, 9)

y(-3, 1, 6, 9)


# 12
len('python')
len('dragon')

len('python') > len('dragon')

# 13
'on' in ('python' and 'dragon')

# 14
'jargon' in ('I hope this course is not full of jargon')


# 15
'on' not in ('python' or 'dragon')


# 16

str(float(len('python')))


# 17

def check_even(x):
    x = float(x)
    if (x % 2 == 0):
        print(x, 'is Even.')
    else : 
        print(x, 'is odd.')


check_even(3)

# 18
 7//3 == int(2.7)


# 19
type('10') == type(10)

# 20

int('9.8') == 10



# 21
hours = float(input('Enter the hour : '))
rate_per_hour = float(input('Enter the rate_per_hour : '))
print('Your weekly earning is : ', hours * rate_per_hour)


# 22
years = float(input('Enter the years : '))
print('You have lived for', (100-years)*365*24*60*60, 'seconds.')



# 23
print('', 1, 1, 1, 1, 1,'\n',2, 1, 2, 4, 8, '\n', 3, 1, 3, 9, 27, '\n', 4, 1, 4, 16, 64, '\n', 5, 1, 5, 25, 125)

