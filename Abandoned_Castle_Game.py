print(r'''
          <|
           A             
          /.\       
     <|  [""M#      
      A   | #              
     /.\ [""M#             
    [""M# | #  U"U#U                 
     | #  | #  \ .:/    
     | #  | #___| #     
     | "--'     .-"     
   |"-"-"-"-"-#-#-##    
   |     # ## ######     
    \       .::::'/     
     \      ::::'/      
   :8a|    # # ##      
   ::88a      ###       
  ::::888a  8a ##::.    
  ::::::888a88a[]::::
 :::::::::SUNDOGa8a::::. ..              
 :::::8::::888:Y8888:::::::::...      
::':::88::::888::Y88a______________________________________________________
:: ::::88a::::88a:Y88a                                  __---__-- __
' .: ::Y88a:::::8a:Y88a                            __----_-- -------_-__
  :' ::::8P::::::::::88aa.                   _ _- --  --_ --- __  --- __--
.::  :::::::::::::::::::Y88as88a...s88aa.

''')
print("Welcome to Notting Hill abandoned castle!")
first_option = input("Your mission is to find a way to get out alive. \n"
                     "Left or right? ").lower()
if first_option == "left":
    print(r'''
          _,-""-._
        ,"        ".
       /    ,-,  ,"'
      "    /   \ | o|
      \    `-o-"  `-',
       `,   _.--'`'--`
         `--`---'                    |   _)
           ,' '      _  /  _ \  ` \   _ \ |  -_)
         ./ ,  `,    ___|\___/_|_|_|_.__/_|\___|
         / /     /
        (_)))_ _,"
           _))))_,
  --------(_,-._)))-------------------------------
''')
    print("\nThe zombie guard found you and killed you. Game over.")
elif first_option == "right":
    second_option = input("You got to the lake outside the castle."
                          " Great job! "
                          "Do you want to swim or wait? ").lower()
    if second_option == "wait":
        print(r'''.  o ..                  
     o . o o.o                
          ...oo               
            __[]__            
         __|_o_o_o\__         
         \""""""""""/         
          \. ..  . /          
     ^^^^^^^^^^^^^^^^^^^^''')
        print("\nA boat is here to rescue you!")
        final_option = input("You get on the boat and there are 3 buttons:"
                             " pink, blue and green. Only one gets the boat"
                             " going to get out. Which colour do you choose? ").lower()
        if final_option == "pink":
            print(r'''                                      
                        888                Y8P                 
                        888                                    
 .d88b. 888  88888888b. 888 .d88b. .d8888b 888 .d88b. 88888b.  
d8P  Y8b`Y8bd8P'888 "88b888d88""88b88K     888d88""88b888 "88b 
88888888  X88K  888  888888888  888"Y8888b.888888  888888  888 
Y8b.    .d8""8b.888 d88P888Y88..88P     X88888Y88..88P888  888 
 "Y8888 888  88888888P" 888 "Y88P"  88888P'888 "Y88P" 888  888 
                888                                            
                888                                            
                888                                       ''')
            print("\nBurned by the fire. Game over.")
        elif final_option == "blue":
            print(r''' 
                    ,_> `.   ,';
                ,-`'      `'   '`'._
             ,,-) ---._   |   .---''`-),.
           ,'      `.  \  ;  /   _,'     `,
        ,--' ____       \   '  ,'    ___  `-,
       _>   /--. `-.              .-'.--\   \__
      '-,  (    `.  `.,`~ \~'-. ,' ,'    )    _\
      _>    \     \ ,'  ') )   `. /     /    <,.
   ,-'   _,  \    ,'    ( /      `.    /        `-,
   `-.,-'     `.,'       `         `.,'  `\    ,-'
    ,'       _  /   ,,,      ,,,     \     `-. `-._
   /-,     ,'  ;   ' _ \    / _ `     ; `.     `(`-\
    /-,        ;    (o)      (o)      ;          `'`,
  ,~-'  ,-'    \     '        `      /     \      <_
  /-. ,'        \                   /       \     ,-'
    '`,     ,'   `-/             \-' `.      `-. <
     /_    /      /   (_     _)   \    \          `,
       `-._;  ,' |  .::.`-.-' :..  |       `-.    _\
         _/       \  `:: ,^. :.:' / `.        \,-'
       '`.   ,-'  /`-..-'-.-`-..-'\            `-.
         >_ /     ;  (\/( ' )\/)  ;     `-.    _<
         ,-'      `.  \`-^^^-'/  ,'        \ _<
          `-,  ,'   `. `"""""' ,'   `-.   <`'
            ')        `._.,,_.'        \ ,-'
             '._        '`'`'   \       <
                >   ,'       ,   `-.   <`'
                 `,/          \      ,-`
                  `,   ,' |   /     /
                   '; /   ;        (
                    _)|   `       (
                    `')         .-'
                      <_   \   /    
                        \   /\(
                         `;/  `
''')
            print("\nA lion appeared out of nowhere. You got eaten. "
                  "Game over.")

        elif final_option == "green":
          print(r'''88                                                         
88                                                         
88                                                         
88,dPPYba,  8b,dPPYba, ,adPPYYba, 8b       d8  ,adPPYba,   
88P'    "8a 88P'   "Y8 ""     `Y8 `8b     d8' a8"     "8a  
88       d8 88         ,adPPPPP88  `8b   d8'  8b       d8  
88b,   ,a8" 88         88,    ,88   `8b,d8'   "8a,   ,a8"  
8Y"Ybbd8"'  88         `"8bbdP"Y8     "8"      `"YbbdP"''')

          print("\nYou win! Congrats!")
        else:
            print("You choose a door that doesn't exist. "
                  "Game over.")
    else:
        print(r''' 
                                  ,'::|
                                 /::::|
                               ,'::::o\                                      _..
            ____........-------,..::?88b                                  ,-' /
    _.--"""". . . .      .   .  .  .  ""`-._                           ,-' .;'
   <. - :::::o......  ...   . . .. . .  .  .""--._                  ,-'. .;'
    `-._  ` `":`:`:`::||||:::::::::::::::::.:. .  ""--._ ,'|     ,-'.  .;'
        """_=--       //'doo.. ````:`:`::::::::::.:.:.:. .`-`._-'.   .;'
            ""--.__     P(       \               ` ``:`:``:::: .   .;'
                   "\""--.:-.     `.                             .:/
                     \. /    `-._   `.""-----.,-..::(--"".\""`.  `:\
                      `P         `-._ \          `-:\          `. `:\
                                      ""            "            `-._)''')
        print("\nYou got eaten by a big shark. Game over.")
else:
        print("Game over.")


input("\nPress ENTER to close this window")
