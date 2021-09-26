#Alfaizi Ahmad Zahran (Akanggendang)
#20210925
#Basic Temperature Convertor
#Python

from time import sleep

while True:

    print("\n\n\n######################")
    print("Temperature Convertor")
    print("######################")

    print('-------Start-------')
    print('-------About-------')
    print('-------Quit-------')
    print('you can type the shortcut, example:Start = S ')

    menu = input("\nAnswer : ")

    if menu =='S':
        print("Loading......")
        sleep(4)

        val_a = float(input("Input your Temperature : "))
        unit = input("Input your temperature unit (C,F,R,K) : ")
       
        if unit == 'C':
            conv_C = input("Convert To (R,F,K) : ")
            print("Loading......")
            sleep(4)
            if conv_C == 'R':
                print("The resuLt is ",val_a*(4/5), "Reamur")
            elif conv_C == 'F':
                print("The result is ",(val_a*9/5)+32,"Fahrenheit")   
            elif conv_C == 'K':
                print("The result is ",val_a+273,"Kelvin")     
            else:
                print("Invalid input")    

        elif unit == 'F':
            conv_F = input("Convert To (C,R,K) : ")
            print("Loading......")
            sleep(4)
            if conv_F == 'R':
                print("The result is ",(val_a-32)*(4/9),"Reamur")     
            elif conv_F == "C":
                print("The Result is ",(val_a-32)*(5/9),'Celcius')    
            elif conv_F == "K":
                print("The result is ",(val_a-32)*5/9 + 273.15,'Kelvin')    
                

        elif unit == 'R':
            Conv_R = input("Convert To (C,F,K) : ")
            print("Loading.......")   
            sleep(4)
            if Conv_R == 'C':
                print("The result is ",(5/4)*val_a,"Celcius")
            elif Conv_R == 'F':
                print("The result is ",(9/4)*val_a+32,"FAhrenheit")
            elif Conv_R == 'K':
                print("The Result is ",(5/4)*val_a+273,"Kelvin")
            else:
                print("Invalid Input")  

        elif unit == 'K':
            Conv_K = input("Convert To (C,F,R) : ")   
            print("Loading.......") 
            sleep(4)
            if Conv_K == 'C':
                print("The result is ",val_a-273,'Celcius')
            elif Conv_K == 'R':
                print('The result is ',(4/5)*(val_a-273),'Reamur')
            elif Conv_K == 'F':
                print("The result is ",(val_a-273,15)*95+32,"Fahrenheit")     


    elif menu == 'A':
        print("Hi There, My name is Alfaizi you can call me faiz or aknggandang")
        print("I am a high school student,now i'm 17 ")
        print("i start studying programing in 2020")
        print("if you have any question,suggestion ,and critic you can follow and DM my Instagram (@retikulum.endoplasma002)")
        print("take it easy your life")

    elif menu == 'Q':
        quit()
            




                     


  


        
 
            







        








        








