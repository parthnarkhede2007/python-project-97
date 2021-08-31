import random

print("number guessing game")

number = random.randint(1, 20)

chances = 0

print("guess a number between 1 to 9")

while chances < 5:
    guess = int(input("enter the number"))

    if(guess == number):
        print("noice you won")

        break

    elif(guess < number):
         print("your guess was too low guess a number higher")          

    else:
        print("your guess was to high guess a number lower")

        chances +=1

    if not chances < 5:
        print("YOU LOSE, THE NUMEBR IS :",number)
            

                

                
                    


         

         
               

               
                   

                   

                    
                        
             


    
    
     
 


      


    

         


           


               


                
                  
         
         
           
         




