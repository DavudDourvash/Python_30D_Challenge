multiline_string = '''I am a data scientist and enjoy my career.
I didn't find anything as valuable as love.
That is why I'm trying to migrate and being with sima.'''
print(multiline_string)


#    \n: new line
#    \t: Tab means(8 spaces)
#    \\: Back slash
#    \': Single quote (')
#    \": Double quote (")

print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote



#    %s - String (or any object with a string representation, like numbers)
#    %d - Integers
#    %f - Floating point numbers
#    "%.number of digitsf" - Floating point numbers with fixed precision

# Strings only
first_name = 'David'
last_name = 'Dourvash'
language = 'R'
age = 33
formated_string = 'I am %s %s , I\'m %d years old. I teach %s.' %(first_name, last_name, age,language)
print(formated_string)

# New Style from python 3
formated_string2 = 'I am {} {} , I\'m {} years old. I teach {}.'.format(first_name, last_name, age,language)
print(formated_string2)


# String Interpolation / f-Strings (Python 3.6+)
print(f'I am {first_name} {last_name}, I\'m {age} years old. I teach {language}')



language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

language[0]
first_name[-1]

first_name[2:]
first_name[-2:]

'Hello World!'[::-1]

# Skipping Characters While Slicing
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto



#    join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'


web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'


challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']


challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON


