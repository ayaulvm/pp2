import re
#1.
s = input('Input your string: ')

check = re.compile('ab*')

n = check.search(s)

if n:
    print("Found: ", n.group())

else:
    print('No match')

#2.
s = input('Input your string: ')

check = re.compile('ab{2, 3}')

n = check.search(s)

if n:
    print("Found: ", n.group())

else:
    print('No match')

# 3. 
s = input('Input your string: ')
check = re.compile('[a-z]+_[a-z]+')
n = check.search(s)

if n:
    print("Found: ", n.group())

else:
    print('No match')

# 4.
s = input('Input your string: ')

check = re.compile('[A-Z][a-z]+')

n = check.search(s)

if n:
    print("Found: ", n.group())

else:
    print('No match')

# 5. 
s = input('Input your string: ')

check = re.compile('a.*b$')

n = check.search(s)

if n:
    print("Found: ", n.group())

else:
    print('No match')

# 6. 
s = input('Input your string: ')

print(re.sub(r'[ ,.]', ':', s))

# 7. 
s = input('Input your string: ')

def snake_to_camel(s):
    words = s.split('_')
    c_words = words[0].capitalize() + ''.join(word.capitalize() for word in words[1:])
    return c_words    
    
print(snake_to_camel(s))

# 8. 
s = input('Input your string: ')

def space_between_big(s):
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', s)
    return result

print(space_between_big(s))

# 9. 
s = input('Input your string: ')
def insert_spaces_between_capitals(s):
    return re.sub(r"([a-z])([A-Z])", r"\\1 \\2", s)

# 10. 
s = input('Input your string: ')

def camel_to_snake(s):
    result = re.sub('([a-z])([A-Z])', r'\1_\2', s)
    return result
    
print(camel_to_snake(s))
