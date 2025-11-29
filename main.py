import logic
import storage

while True :

    user_choose = logic.choose_strength()
    if user_choose == 'exit' :
        print("Goodbye,the programm is closed.")
        break
    password = logic.generate_password(user_choose)
    storage.save_password(password)
    print(f"The generated password: {password} (saved!)")

        
