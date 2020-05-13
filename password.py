def password(pw): 
      
    SpecialSym =['$', '@', '#'] 
    val = True
      
    if len(pw) < 8: 
        print("The length of password should be more than 8") 
        val = False
          
    if len(pw) > 16: 
        print("The length of password should not exceed 16") 
        val = False
          
    if not any(char.isdigit() for char in pw): 
        print('Password should have at least one number') 
        val = False
          
    if not any(char.isupper() for char in pw): 
        print('Password should have at least 1 uppercase letter') 
        val = False
          
    if not any(char.islower() for char in pw): 
        print('Password should have at least 1 lowercase letter') 
        val = False
          
    if not any(char in SpecialSym for char in pw): 
        print('Password should have at least 1 of the symbols from $, @, #') 
        val = False
    if val: 
        return val 
  
def main(): 
    pw = input("Enter the Password:")
      
    if (password(pw)): 
        print("Password is valid") 
    else: 
        print("Invalid Password") 
          

if __name__ == '__main__': 
    main() 