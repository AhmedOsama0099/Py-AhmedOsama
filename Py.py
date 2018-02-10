print("                                        Wlecome to Nim-21 game!")
sum=21
while True: #player agin or not
    
    x=int(input("how many numbers player: "))
    while x!=1 and x!=2:
        print("this game can be played by 1 player or 2 players")
        x=int(input("how many numbers player: "))
    if x==2: #2 users
        while True:
            player1=int(input("player1 please enter num: "))
            while player1!=1 and player1!=2 and player1!=3:
                print("please enter num from 1:3")
                player1=int(input("player1 plese enter num: "))
            
            
            if sum==2:
                
                    while player1!=1 and player1!=2:
                        print("player1 plase enter num from 1,2")
                        player1=int(input("player1 please enter num: "))
            sum=sum-player1
            print("coins= ",sum)           

            if sum==1:
                print("player1 Won!")
                break
            if sum==0:
                print("player2 Won")
                break
            
            player2=int(input("player2 plese enter num: "))        
            while player2!=1 and player2!=2 and player2!=3:
                print("please enter num from 1:3")
                player2=int(input("player2 plese enter num: "))
            
            
            if sum==2:
                 while player2!=1 and player2!=2 :
                    print("plase enter num from 1,2")
                    player2=int(input("player2 please enter num: "))
            sum=sum-player2   
            print("coins= ",sum)   
            if sum==1:
                print("player2 Won!")
                break
            if sum==0:
                print("player1 Won")
                break
            
            
           
    if x==1:
        y=int(input("1=hard & 2=easy: "))
        while y!=1 and y!=2:
              print("this game is easy and hard only")
              y=int(input("1=hard & 2=easy: "))
        if y==1: #hard computer :D Try to win! 
            player2=0
             
            while sum!=0:
                player1=int(input("player1 plese enter num: "))
                while player1!=1 and player1!=2 and player1!=3:
                    print("please enter num from 1:3")
                    player1=int(input("player1 plese enter num: "))
                sum=sum-player1
                print("coins= ",sum)
                
                if sum==2:
                    player2=1
                    sum=sum-player2
                    print("computer= ",player2)     
                    print("coins= ",sum )   
                if sum==1:
                    print("computer Won!")
                    break
                if sum==0:
                    
                    print("player1 Won")
                    break

                player2=4-player1 
                print("computer: ",player2)
                sum=sum-player2
                print("coins= ",sum)
                if sum==2:
                     while player1!=1 and player1!=2 :
                        print("plase enter num from 1,2")
                        player1=int(input("player1 please enter num: "))
                     sum=sum-player1   
                     print("coins= ",sum)   
                if sum==1:
                    
                    print("computer Won!")
                    break
                if sum==0:
                    print("player1 Won")
                    break
            
        if y==2:  #easy computer
                     import random
                     sum=21          
                     v=random.randint(2,3)     
                     print("computer: ",v)           
                     sum=sum-v
                     print("coins= ",sum)
                     player2=int
                     while sum!=0:               
                     
                         player1=int(input("player1 plese enter num: "))
                         while player1!=1 and player1!=2 and player1!=3:
                             print("please enter num from 1:3")
                             player1=int(input("player1 plese enter num: "))

                         if sum==2:
                             while player1!=1 and player1!=2 :
                                   print("plase enter num from 1,2")
                                   player1=int(input("player1 please enter num: "))
                         sum=sum-player1
                         print("coins= ",sum)

                         if sum==1:
                             print("player1 Won!")
                             break
                         if sum==0:
                             print("computer Won!")
                             break
                         
                         if sum==2:
                             player2=1
                         elif sum==3:
                             player2=2
                         elif sum==4:
                             player2=3
                         else:
                             player2=4-player1 
                         print("computer: ",player2)
                         sum=sum-player2
                         print("coins= ",sum)
                         if sum==1:
                             print("computer Won!")
                             break
                         if sum==0:
                            print("player1 Won!")
                            break
    m=int(input("play again press:1 exit press:2 >> "))#player agin or not
    while m!=1 and m!=2:     
        print("no more options")
        m=int(input("play again press:1 exit press:2 >> "))
    sum=21
    if m==2:
        break
            
            
      
        
