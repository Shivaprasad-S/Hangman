import random
import os
#hang_list=['shivu','vikram','sumanth','python','pushpa']
#hang_list=['abcde','abc','abcd','abcdef','a','ab']
hang_list=['hyundai','honda','kia','benz','audi','maruti','mahindra','renault','skoda','ford','nissan','toyato','tata']
#hang_list=['benz']
wrong_guess=wrong_counter=0
word_display=""
guess_lst=[]
word=random.choice(hang_list)
guess_counter=0
os.system('cls')
word_length=len(word)
random_word_list=list("#"*word_length)
print("Guess the Car Manufacturer")
print("#"*word_length)
while True:
    if word_display==word:
        break
    elif wrong_guess<word_length:
        guess_counter=0
        wrong_counter=0
        #print(guess_lst)
        guess=input("enter a charector")
        for x in guess_lst:
            #print(x,guess)
            if x==guess:
                os.system('cls')
                print("Guess the Car Manufacturer")
                print(word_display) 
                print("input already entered")
                wrong_counter=1
                guess_counter=1
                #guess_lst.append(guess)
            #break
        if wrong_counter==0:
            guess_lst.append(guess)
            
            os.system('cls')
            for i in range(len(word)):
                word_display="".join(random_word_list)
                #print(word[i])
                if guess==word[i]:
                    random_word_list.insert(i,guess)
                    random_word_list.pop(i+1)
                    word_display="".join(random_word_list)
                    os.system('cls')
                    print("Guess the Car Manufacturer")
                    print(word_display)
                    guess_counter=1
                    if word==word_display:
                        os.system('cls')
                        print("Your Guess is correct...")
                        print(word_display)
                        print("Well done... congrats...")
                        break
                    else:
                        print("Good Guess...")
                        print("wrong attempt remaining=",word_length-wrong_guess)
        if guess_counter == 0:
            os.system('cls')
            #print(guess_counter)
            print("Guess the Car Manufacturer")
            print(word_display)
            wrong_guess+=1
            for i in guess_lst:
                if i!=guess:
                    guess_lst.append(guess)

            #guess_lst.append(guess)
            if word_length-wrong_guess!=0:
                print("wrong guess")
                print("wrong attempt remaining=",word_length-wrong_guess)
    else:
        os.system('cls')
        print("Car Manufactuter name is")
        print(word)
        print("Sory... Better Luck Next time")
        break

    


