print(r'''                          o
                       _---|         _ _ _ _ _
                    o   ---|     o   ]-I-I-I-[
   _ _ _ _ _ _  _---|      | _---|    \ ` ' /
   ]-I-I-I-I-[   ---|      |  ---|    |.   |
    \ `   '_/       |     / \    |    | /^\|
     [*]  __|       ^    / ^ \   ^    | |*||
     |__   ,|      / \  /    `\ / \   | ===|
  ___| ___ ,|__   /    /=_=_=_=\   \  |,  _|
  I_I__I_I__I_I  (====(_________)___|_|____|____
  \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_|
   |[]      '|   | []  |`__  . [  \-\--|-|--/-/
   |.   | |' |___|_____I___|___I___|---------|
  / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] |
 <===>  |   .|-=-=-=-=-=-=-=-=-=-=-|   |    / \
 ] []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===>
 ] []| ` |   |/////////\\\\\\\\\\.||__.  | |[] [
 <===>     ' ||||| |   |   | ||||.||  []   <===>
  \T/  | |-- ||||| | O | O | ||||.|| . |'   \T/
   |      . _||||| |   |   | ||||.|| |     | |
../|' v . | .|||||/____|____\|||| /|. . | . ./
.|//\............/...........\........../../\\\
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# --- TREASURE ISLAND GAME LOGIC ---

# Step 1: The Crossroad
# Ask the user: "You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n"
# - If they type 'left': They survive and move to the next step.
# - If they type 'right': Print "You fell into a hole. Game Over." and end the game.
# - (Tip: You can use .lower() on the input so 'Left' or 'LEFT' still works)

# Step 2: The Lake
# If they chose 'left' above, ask: 
# "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n"
# - If they type 'wait': They survive and move to the next step.
# - If they type 'swim': Print "You get attacked by an angry trout. Game Over." and end the game.

# Step 3: The Three Doors
# If they chose 'wait' above, ask:
# "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n"
# - If they type 'red': Print "It's a room full of fire. Game Over."
# - If they type 'yellow': Print "You found the treasure! You Win!"
# - If they type 'blue': Print "You enter a room of beasts. Game Over."
# - If they type anything else: Print "You chose a door that doesn't exist. Game Over."

a=input("Bsdk teri mar chuki hai tu abhi cross road pe khada hai kaha jayega left ya right\n ")
if a=="right":
    print("Mkb aag bhosdi teri mar gayi hai ")
elif a=="left":
    b=input("Bhosdi tu lake pe aa gaya ab bata upar jayega ya niche:\n")
    if b=="upar":
        print("Mar gayi teri ja upar haha emoji")
    elif b=="niche":
        c=input("lodu tu aagya hai aab cid me ab kaha jayega gate1 me ya gate2 me: \n")
        if c=="gate1":
            print("7 karoddddddddddddd jeeet gaya tu now go back to your pahetic life ")
        elif c=="gate2":
            print("Margayi teri ")
else:
    print("HAHA kuch bhi likh diya hai na loduuu hahah")