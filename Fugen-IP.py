# By PewFam 
# June 12 2022, 13:51:24
import random
import pystyle
from pystyle import Colorate, Colors, Center
from os import system,name
if name == 'nt':
    system('cls')
else:
    system('clear')
header = """
 ________   ___    _   .-_'''-.       .-''-.  ,---.   .--.             .-./`) .-------.  
|        |.'   |  | | '_( )_   \    .'_ _   \ |    \  |  |             \ .-.')\  _(`)_ \ 
|   .----'|   .'  | ||(_ o _)|  '  / ( ` )   '|  ,  \ |  |             / `-' \| (_ o._)| 
|  _|____ .'  '_  | |. (_,_)/___| . (_ o _)  ||  |\_ \|  |  _ _    _ _  `-'`"`|  (_,_) / 
|_( )_   |'   ( \.-.||  |  .-----.|  (_,_)___||  _( )_\  | ( ' )--( ' ) .---. |   '-.-'  
(_ o._)__|' (`. _` /|'  \  '-   .''  \   .---.| (_ o _)  |(_{;}_)(_{;}_)|   | |   |      
|(_,_)    | (_ (_) _) \  `-'`   |  \  `-'    /|  (_,_)\  | (_,_)--(_,_) |   | |   |      
|   |      \ /  . \ /  \        /   \       / |  |    |  |              |   | /   )      
'---'       ``-'`-''    `'-...-'     `'-..-'  '--'    '--'              '---' `---'      by PewFam on GitHub
                                                                                         
"""
print(Colorate.Vertical(Colors.green_to_blue, Center.Center(header)))
list3 = [1,2,3,5,6,7,8,9]
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list2 = ["", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
a = input('\nHow many ip ? % ')
print('\n\n')
for a in range(int(a)):
    
    print(Colorate.Diagonal(Colors.red_to_yellow , (str(random.choice(list3)) + str(random.choice(list3)) + "." + str(random.choice(list1)) + str(random.choice(list1)) + str(random.choice(list1)) +"." + str(random.choice(list1)) +str(random.choice(list1)) +"." + str(random.choice(list1))+str(random.choice(list2)) )))
    print()
