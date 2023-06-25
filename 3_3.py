name = input('Enter your name: ')
age = input('How old are you?: ')
city = input('What city are you from?: ')

text1 = 'Hello, ' + name + '.'  + ' Your age is: ' + str(age) + '.' ' Your city is ' + city + '.'
text2 =  'Hello, {}. Your age is: {}. Your city is {}.'.format(name, age, city)
text3 = f'Hello, {name}. Your age is: {age}. Your city is {city}.'
print(text1)
print(text2)
print(text3)