import re

def get_password_strength(passwd):
 
    strength = 0
 
    if re.search('[A-ZА-Я]', passwd) and re.search('[a-zа-я]', passwd):
        strength += 3
        
    elif re.search('[A-ZА-Я]', passwd):
        ball += 2
        
    else:
        strength += 1
 
    if re.search('[0-9]', passwd):
        strength += 1
 
    if 6 < len(passwd)< 10:
        strength += 2
        
    elif len(passwd)<10:
        strength += 2
        
    else:
        strength += 3
 
    if re.search('[{}@#$%^&+=*()?!.,~]', passwd):
        strength += 5
    
    return strength

password = input('Введите пароль: ')

if __name__ == '__main__':
    result = get_password_strength(password)
    print (result)
