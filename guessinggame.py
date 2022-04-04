# Guessing Game



word = "JESUS CHRIST"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess!= word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1    
    else:
        out_of_guesses = True 
        
if guess_count == 3:
        print("OUT OF GUESSES, YOU LOSE!")
else:
        print("YOU WIN")
           

    
    
    


    

