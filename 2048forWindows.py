import random
import msvcrt
from os import system, name 
from colorama import *




# to clear last grid
def clear():  
    if name == 'nt': 
        _ = system('cls') 
  
# to take starting inputs
def Start_Game():
    print("Instructions :")
    print("input W to move Blocks upward")
    print("input A to move Blocks ledtward")
    print("input S to move Blocks downward")
    print("input D to move Blocks Rightward")
# to set size of board
    size_board =  int(input("enter the size of board : ")) 
    size_board = 5 if size_board < 0 else size_board
# to check and set the end tile number
    end_num = int(input("enter the number of end tile : "))
    x = end_num
    isPowOf2 = False
# to check the input number is power of 2 or not
    while  x > 0 :
        x = x / 2
        if x==1 or x==2 or x==4 or x==8 :
            isPowOf2 =True
            break

    if isPowOf2 == False:
        print("the number enter by you is not power of 2 so number on end tile is set to 2048")
        end_num = 2048
    return size_board , end_num

# to set initial setup of the game
def Game_Setup ():
    size_board , end_num = Start_Game()
    game_array = []
    for i in range(size_board):
        temp = []
        for j in range(size_board):
            temp.append(0)
        game_array.append(temp)
    show_array(game_array)
    return game_array , end_num
# to print game board on terminal
def show_array (game_array):
# to change the colour of the game board
    print(Fore.GREEN )
    l = len(game_array)
    for i in range (l):
        for j in range(l):
            if game_array[i][j] != 0 :
                print(game_array[i][j] , end= " ")
            else :
                print(" ",end=" ")
        print("")
# to genrate random number for position
def genrate_random(l):
    x = int(random.random() * l*l)
    return x // l , x % l
#  to rung game
def Run_game(game_array ,end_num):
# to check the you win or not
    win = iswin(game_array , end_num)
    loose = isloose(game_array)
    rightinput = True
    l = len(game_array)
    
    while (win == False) and (loose == False):
        
        
        clear()
        win = iswin(game_array , end_num)
        loose = isloose(game_array)
        
        
       
        while(rightinput):
            i , j = genrate_random(l)
            if game_array[i][j] != 0:
                i , j = genrate_random(l)
                
            else :
                break

        
        game_array[i][j] = 2
        show_array(game_array)
        win = iswin(game_array , end_num)
        loose = isloose(game_array)
        if win :
            print("you won the game")
            return
        if loose :
            print("you loose the game")
            return
        
        User_input = msvcrt.getch()
        
        rightinput = update_game_array(str(User_input),game_array)
        
        win = iswin(game_array , end_num)
        loose = isloose(game_array)
        if win :
            print("you won the game")
            return
        if loose :
            print("you loose the game")
            return

    
# to check that player is loose or not

def isloose(game_array):
    l = len(game_array)
    
    for i in range(l):
        for j in range(l):
            if game_array[i][j] == 0:
                return False
    return True
# to check player is win or not
def iswin(game_array , end_num):
    l = len(game_array)
    for i in range(l):
        for j in range(l):
            if game_array[i][j] == end_num:
                return True
    return False

# to update game array after every move it calls corresponding functions as per inputs
def update_game_array(User_input,game_array):
    print(Fore.RED )
    l = len(game_array)
    
    
    if User_input == "b'W'" or User_input == "b'w'":
        move_upward(User_input,game_array,l)
            
    elif User_input == "b's'" or User_input == "b'S'":
        move_downward(User_input,game_array,l)
            
    elif User_input == "b'A'" or User_input == "b'a'":
        move_leftward(User_input,game_array,l)
            
    elif User_input == "b'D'" or User_input == "b'd'":
        move_rightward(User_input,game_array,l)
            
# if player input wrong key then it prints enter right input
    else :
        print("enter right input")
        return False
    return True

def move_upward(User_input,game_array,l):
    for j in range(l):
        for i in range(l):
            for k in range(i+1 ,l):
                if game_array[k][j] != 0:
                    if game_array[i][j] == game_array[k][j]:
                        game_array[i][j] *= 2
                        game_array[k][j] = 0
                        break
                    else :
                        break
    for j in range(l) :

	    count = 0
	    i=0
	    while(i<l):
		    if game_array[i][j] == 0:
			
			    count+=1
		    else:
			    game_array[i-count][j] = game_array[i][j]
			    if count != 0:
				    game_array[i][j]= 0
			    i = i-count
			    count=0
		    i+=1

def move_downward(User_input,game_array,l):
    for j in range(l):
        for i in range(l-1,-1,-1):
            for k in range(i-1,-1,-1):
                if game_array[k][j] != 0:
                    if game_array[k][j] == game_array[i][j]:
                        game_array[i][j] *= 2
                        game_array[k][j] = 0
                        break
                    else:
                        break
    for j in range(l):
        count = 0
        i= l-1
        while i >= 0:
            if game_array[i][j] == 0:
                count += 1
            else :
                game_array[i+count][j] = game_array[i][j]
                if count != 0:
                    game_array[i][j] = 0
                i += count
                count = 0
            i -= 1
         
def move_leftward(User_input,game_array,l):
    for j in range(l):
        for i in range(l):
            for k in range(i+1 ,l):
                if game_array[j][k] != 0:
                    if game_array[j][k] == game_array[j][i]:
                        game_array[j][i] *= 2
                        game_array[j][k] = 0
                        break
                    else :
                        break
    for j in range(l) :

	    count = 0
	    i=0
	    while(i<l):
		    if game_array[j][i] == 0:
			
			    count+=1
		    else:
			    game_array[j][i-count] = game_array[j][i]
			    if count != 0:
				    game_array[j][i]= 0
			    i = i-count
			    count=0
		    i+=1

def move_rightward(User_input,game_array,l):
    for j in range(l):
        for i in range(l-1,-1,-1):
            for k in range(i-1,-1,-1):
                if game_array[j][k] != 0:
                    if game_array[j][k] == game_array[j][i]:
                        game_array[j][i] *= 2
                        game_array[j][k] = 0
                        break
                    else:
                        break
    for j in range(l):
        count = 0
        i= l-1
        while i >= 0:
            if game_array[j][i] == 0:
                count += 1
            else :
                game_array[j][i+count] = game_array[j][i]
                if count != 0:
                    game_array[j][i] = 0
                i += count
                count = 0
            i -= 1
         
    
# the main function which calls required functions
game_array , end_num = Game_Setup()
Run_game(game_array ,end_num)  



