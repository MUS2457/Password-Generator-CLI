import random
import string

def choose_strength() :

    while True :
        valid = ["weak", "normal", "strong"]
        user = input(f"Choose strength: {valid}.").strip().lower()
        if user == '' :
            print("please one of the 3 options")
            continue
        if user in valid or user == 'exit':
            return user
        else:
            print("Invalid option, please choose one of:", valid)

def generate_password(strength):

    if strength == 'weak' :
        letter = string.ascii_letters
        password_letter = random.choices(letter,k = 6)
        password = ''.join(password_letter)
        return password
    elif strength == 'normal' :
        let_num = string.digits + string.ascii_letters
        password_let_num = random.choices(let_num,k = 10 )
        password = ''.join(password_let_num)
        return password
    elif  strength == 'strong' :
        let_num_pu = string.digits + string.ascii_letters + string.punctuation
        password_let_num_pu = random.choices(let_num_pu,k = 14 )
        password = ''.join(password_let_num_pu)
        return password
    # i didnt add else on purpose since first def fc hundles the bad output


    
