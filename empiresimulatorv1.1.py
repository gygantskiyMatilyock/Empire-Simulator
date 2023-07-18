import random
import time
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

print("███████╗███╗░░░███╗██████╗░██╗██████╗░███████╗")
print("██╔════╝████╗░████║██╔══██╗██║██╔══██╗██╔════╝")
print("█████╗░░██╔████╔██║██████╔╝██║██████╔╝█████╗░░")
print("██╔══╝░░██║╚██╔╝██║██╔═══╝░██║██╔══██╗██╔══╝░░")
print("███████╗██║░╚═╝░██║██║░░░░░██║██║░░██║███████╗")
print("╚══════╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝")

print("░██████╗██╗███╗░░░███╗██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░  ██╗░░░██╗░░███╗░░")
print("██╔════╝██║████╗░████║██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗  ██║░░░██║░████║░░")
print("╚█████╗░██║██╔████╔██║██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝  ╚██╗░██╔╝██╔██║░░")
print("░╚═══██╗██║██║╚██╔╝██║██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗  ░╚████╔╝░╚═╝██║░░")
print("██████╔╝██║██║░╚═╝░██║╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║  ░░╚██╔╝░░███████╗")
print("╚═════╝░╚═╝╚═╝░░░░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝")
print(" ")
print("ＭＡＤＥ   ＢＹ:   ＳＴＥＰＡＮ,   ＰＥＤＲＯ   ＡＮＤ   ＭＡＵＲＩＣＩ")

#invest
BitcoinP = random.randint (-15, 15)
EthereumP = random.randint (-20, 20)
AppleP = random.randint (-25, 25)
MicrosoftP = random.randint (-30, 30)
SolanaP = random.randint (-75, 75)
DogecoinP = random.randint (-100, 100)
SandboxP = random.randint (-500, 500)

BitcoinY = 0
EthereumY = 0
AppleY = 0
MicrosoftY = 0
SolanaY = 0
DogecoinY = 0
SandboxY = 0

#mine

minecost = 50 #inv
startcoal = 5
coal = 1 #inv
pricecoal = 5

startcopper = 3
copper = 1 #inv
pricecopper = 15

startiron = 3
iron = 1 #inv
priceiron = 25

startgold = 1
gold = 1 #inv
pricegold = 50

startemerald = 0
emerald = 1 #inv
priceemerald = 150

startdiamond = 0
diamond = 1 #inv
pricediamond = 500

#dungeon

dungeon1probab = random.randint(1, 6)
r = 5

#items

banana = 1
apple = 1
startmoney = 100
startapples = 10
startbananas = 2
Upgrade1 = 100000
Upgrade2 = 300000
allfruits = (startapples, startbananas)
r = 5
banana = 1
apple = 1
startmoney = 100
startapples = 10
startbananas = 2
Upgrade1 = 100
Upgrade2 = 300
allfruits = (startapples, startbananas)
warlord_stick = 0
obsidian_crystal = 0
magma_block = 0
piece_magic_stick = 0
piece_of_asteroid = 0
bone_of_dragon = 0
legendary_wood = 0
piece_of_artifact = 0

#combat system

player_health = 100 
player_damage = 10
basic_sword = 0
stone_sword = 0
magic_stick = 0
legendary_excalibur = 0
if basic_sword == 1:
    player_damage = player_damage + 2
if stone_sword == 1:
    player_damage = player_damage + 5
if magic_stick == 1:
    player_damage = player_damage + 10
if legendary_excalibur == 1:
    player_damage = player_damage + 30



#lvl system
xp = 0
boss1xp = 0
missionxp = 0
lvl = 0
boss1_health = 120
boss1_damage = 15
boss2_health = 1000
boss2_damage = 40

#house system
house = 0
storage_apples = 0
storage_bananas = 0
storage_coal = 0
storage_iron = 0
storage_iron = 0
storage_copper = 0
storage_gold = 0
storage_emerald = 0
storage_diamond = 0
storage_warlord_stick = 0
storage_obsidian_crystal = 0
storage_magma_block = 0
storage_piece_magic_stick = 0
storage_piece_of_asteroid = 0
storage_bone_of_dragon = 0
storage_legendary_wood = 0
storage_piece_of_artifact = 0
storage_stone_sword = 0
storage_basic_sword = 0
ak_47 = 0

#work

time_poor =  60
time_normal = 110
time_rich =  300
time_insane = 600
time_Ilegal = 30

#ilegal

time_jail = random.randint(60, 1000)
drug_dealing_earn = random.randint(5000, 40000)
bank_heist_earn = random.randint(10000, 50000)
assasin_earn = random.randint(50000, 500000)
smugling_earn = random.randint(5000, 30000)
dd = random.randint(1, 10)

while True:
    dungeon1probab = random.randint(1, 6)
    forest1probab = random.randint(1, 5)

    
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print("*Hint if you have less than 0$ you lose")
    print(" ")
    print("Menu: Buy, Sell, Invest, Wallet, Upgrades, Dungeons, Inventory, Mine, Investstats, World, Boss, Casino, Work, Stop")
    print(" ")
    print(" ")
    print("Money:", startmoney,"$"  ,"                                         "                    "Level", lvl)
    print(" ")
    print("Health:", player_health, "HP")
    print(" ")
    print(" ")
    x = input("Enter:   ")

    if x == "Ilegal Activities":
        print("Hey, you little criminal, you choosed Ilegal activities...")
        print("")
        print("You can:")
        print("---------------")
        print("")
        print("Deal Drugs(5k-40k earnings, 70% going to jail)")
        print("Bank Heist(10k-50k earnings, 75% going to jail)")
        print("Assasin(50k-500k earnings, 90% going to jail)")
        print("Smuggling(5k-30k earnings, 60% going to jail)")
        cia = input("Where would you like to work?:     ")

        if cia == "Deal Drugs":
            if dd >= 8:
                print("Wait until the time finish to earn your money:")
                for i in range(time_Ilegal):
                    print(time_Ilegal - i)
                    time.sleep(1)
                print("Congratulations, you finished working")
                startmoney += drug_dealing_earn
            elif dd <= 7:
                print("You got cought dealing drugs, you will now go to jail!")
                for i in range(time_jail):
                    print(time_jail - i)
                    time.sleep(1)
                print("Congratulations, you got out of jail!")

        if cia == "Bank Heist":
            if dd >= 8:
                print("Wait until the time finish to earn your money:")
                for i in range(time_Ilegal):
                    print(time_Ilegal - i)
                    time.sleep(1)
                print("Congratulations, you finished working")
                startmoney += bank_heist_earn
            elif dd <= 7:
                print("You got cought robbing the bank, you will now go to jail!")
                for i in range(time_jail):
                    print(time_jail - i)
                    time.sleep(1)
                print("Congratulations, you got out of jail!")

        if cia == "Assasin":
            if dd == 10:
                print("Wait until the time finish to earn your money:")
                for i in range(time_Ilegal):
                    print(time_Ilegal - i)
                    time.sleep(1)
                print("Congratulations, you finished working")
                startmoney += assasin_earn
            elif dd <= 9:
                print("You got cought killing someone, you will now go to jail!")
                for i in range(time_jail):
                    print(time_jail - i)
                    time.sleep(1)
                print("Congratulations, you got out of jail!")

        if cia == "Smuggling":
            if dd >= 5:
                print("Wait until the time finish to earn your money:")
                for i in range(time_Ilegal):
                    print(time_Ilegal - i)
                    time.sleep(1)
                print("Congratulations, you finished working")
                startmoney += smugling_earn
            elif dd <= 4:
                print("You got cought dealing drugs, you will now go to jail!")
                for i in range(time_jail):
                    print(time_jail - i)
                    time.sleep(1)
                print("Congratulations, you got out of jail!")




    if x == "Casino":
      c1 = random.randint(1, 10)
      c2 = random.randint(1, 10)
      c3 = random.randint(1, 10)
  
      choose_money_bet = int(input("How much money do you want to bet?"))
      startmoney = startmoney - choose_money_bet
  
      print("Your numbers are:")
      print(c1, c2, c3)
  
      if c1 == c2 and c2 == c3:
          print("You just won x3 your bet!")
          startmoney = startmoney + choose_money_bet*3
  
      elif c1 == c2 and c2 == c3 and c1 == 7:
          print("JACKPOT!!!")
          print("You just won x10 your bet!")
          startmoney = startmoney + choose_money_bet*10
  
      else:
          print("sorry, you lost your bet...")
        

    choose_money_bet = 0



    if x == "Boss":
            print(" ")
            print("Choose the boss you want to fight with: ")
            print(" ")
            print("BOSS ====> Lvl 1")
            print("?????? ====> Final Boss")
            print(" ")
            w = input("Enter yout boss:   ")
            if w == "B3sop1":
                print("")
                print("Type ATTACK to continue")
                print(" ")
                ws = input("Enter:   ")
                if ws == "ATTACK":
                    while True:
                        print("You just attacked!")
                        print(" ")
                        boss2_health = boss2_health - player_damage
                        player_health = player_health - boss2_damage
                        print("-You now have",player_health,"HP of Health")
                        print(" ")
                        print("-The boss now has",boss2_health, "HP of Health")
                        print(" ")
                        print("Touch any key to continue")
                        wd = input("Enter: ")
                        if wd == "a":
                            print(" ")
                        if boss2_health <= 0:
                            xp = xp + 25
                            boss2health = 1500
                            player_health = 100
                            print("You have passed the game, well done!")
                            break
                        if player_health <= 1:
                            break
            if w == "BOSS":
                print("")
                print("Type ATTACK ===> to attack the boss")
                print(" ")
                ws = input("Enter:   ")
                if ws == "ATTACK":
                    while True:
                        print(" ")
                        print(" ")
                        print("You just attacked!")
                        print(" ")
                        boss1_health = boss1_health - player_damage
                        player_health = player_health - boss1_damage
                        print("-You now have",player_health, "HP of Health")
                        print(" ")
                        print("-The boss now has",boss1_health, "HP of Health")
                        print(" ")
                        print(" ")
                        print("Touch any key to continue ")
                        wd = input("Enter:   ")
                        if wd == "a":
                            print(" ")
                        if boss1_health <= 0:
                            xp = xp + 25
                            boss1_health = 120
                            player_health = 100
                            print("You have defeat succesfully the boss!")
                            break
                        if player_health <= 1:
                            break

    if x == "Dungeons":
        print(" ")
        print("Type 1 for dungeon level one")
        print("Type 2 for dungeon level two")
        print("Type 3 for dungeon level three")
        print(" ")
        print("Note: as the level of dungeon increases the risk of losing and winning bigger amounts of items and money also increases")
        print(" ")
        lvld = input("Choose your dungeon:")
        if lvld == "1":
            print("Lvl-1  ")
            print("-------")
            print("       ")
            print("REWARDS")
            print("-------")
            print("Obsidian_crystal")
            print("Warlord_stick")
            print("Lose 25$")
            print("Nothing")
            print(" ")
            q = input("Type 'a' to start ===>")
            if q == "a":
                print(" ")
                print(dungeon1probab)
                print(" ")
                if dungeon1probab == 1:
                    print("You lost 25 dolars!")
                    startmoney = startmoney - r*5
                if dungeon1probab == 2:
                    print("Nothing happened")
                if dungeon1probab == 3:
                    print("You just won a Warlord stick!")
                    warlord_stick = warlord_stick + 1
                if dungeon1probab == 4:
                    print("You just lost 25 dolars!")
                    startmoney = startmoney - 25
                if dungeon1probab == 5:
                    print("Nothing happened")
                if dungeon1probab == 6:
                    print("You just won an obsidian crystal!")
                    obsidian_crystal = obsidian_crystal + 1
        if lvld == "2":
            print("Lvl-2  ")
            print("-------")
            print("       ")
            print("REWARDS")
            print("-------")
            print("Magma_block")
            print("Piece_Magic_Stick")
            print("Lose 500$")
            print("Nothing")
            print(" ")
            q = input("Type 'a' to start ===>")
            if q == "a":
                print(" ")
                print(dungeon1probab)
                print(" ")
                if dungeon1probab == 1:
                    print("You lost 500 dolars!")
                    startmoney = startmoney - 500
                if dungeon1probab == 2:
                    print("Nothing happened")
                if dungeon1probab == 3:
                    print("You just won a Magma Block!")
                    magma_block = magma_block + 1
                if dungeon1probab == 4:
                    print("You just lost 500 dolars!")
                    startmoney = startmoney - 500
                if dungeon1probab == 5:
                    print("Nothing happened")
                if dungeon1probab == 6:
                    print("You just won a Piece of Magic Stick!")
                    piece_magic_stick = piece_magic_stick + 1
        if lvld == "3":
            print("Lvl-3  ")
            print("-------")
            print("       ")
            print("REWARDS")
            print("-------")
            print("Piece Of Asteroid")
            print("Bone of dragon")
            print("Lose 5000$")
            print("Nothing")
            print(" ")
            q = input("Type 'a' to start ===>")
            if q == "a":
                print(" ")
                print(dungeon1probab)
                print(" ")
                if dungeon1probab == 1:
                    print("You lost 5000 dolars!")
                    startmoney = startmoney - 5000
                if dungeon1probab == 2:
                    print("Nothing happened")
                if dungeon1probab == 3:
                    print("You just won a Piece of Asteroid!")
                    piece_of_asteroid = piece_of_asteroid + 1
                if dungeon1probab == 4:
                    print("You just lost 5000 dolars!")
                    startmoney = startmoney - 5000
                if dungeon1probab == 5:
                    print("Nothing happened")
                    if dungeon1probab == 6:
                        print("You just won a Bone of Dragon!")
                        bone_of_dragon = bone_of_dragon + 1

    if x == "Buy":
        print("")
        print("What do you want to buy?")
        print("")
        print("Type A ===> to buy properties \nType B ===> to buy objects")
        t = input("Enter:   ")
      
        if t == "B":
            print(" ")
            print("Fruits:")
            print("---------------")
            print(" ")
            print ("Apple 4$")
            print ("Banana 8$")
            print("AK-47 2000000$")
            print(" ")
            print("Dungeon items:")
            print("---------------")
            print(" ")
            print("Warlord stick 1500$")
            print(" ")
            
            y = input(("Enter:    "))
            if y == "Apple":
                z = int(input("Number of apples:   "))
                startapples = startapples + z
                startmoney = startmoney - z*4
            if y == "Banana":
                z = int(input("Number of bananas:    "))
                startbananas = startbananas + z
                startmoney = startmoney - z*8
            if y == "Warlord stick":
                z = int(input("Number of warlord sticks:    "))
                warlord_stick = warlord_stick + z
                startmoney = startmoney - z*1500
            if y == "AK-47":
                z = int(input("Number of guns:    "))
                glock_17 = ak_47 
                startmoney = startmoney - 2000000
                player_damage = player_damage + 200
                print("________________________________________________¶¶_¶¶¶¶¶¶¶¶¶")
                print(" ______________________________________________¶¶¶¶________¶¶")
                print("____________________________________________¶¶_¶¶¶_______¶¶")
                print("_____¶¶¶¶¶¶¶¶_____¶¶___¶¶¶¶_______________¶¶___¶¶______¶¶")
                print("___¶¶¶______¶¶¶__¶¶¶__¶¶________________¶¶____¶¶¶_____¶¶")
                print("____________¶¶¶__¶¶_¶¶¶_______________¶¶______¶¶_____¶¶")
                print("___¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶____¶¶¶¶¶¶¶¶¶__¶¶_______¶¶¶_____¶¶")
                print("_¶¶¶¶______¶¶¶__¶¶_¶¶¶___¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶")
                print("¶¶¶_______¶¶¶__¶¶¶__¶¶¶_____________________¶¶¶_____¶¶")
                print("¶¶¶¶____¶¶¶¶¶__¶¶____¶¶¶____________________¶¶_____¶¶")
                print("_¶¶¶¶¶¶¶¶_¶¶¶__¶¶_____¶¶____________________¶¶_____¶¶")
                print("______________________________________________________¶¶__")
                print("________________________________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")
                print("_______________________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__")
                print("________________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________")
                print("__________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________________")
                print("_________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________________")
                print("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________________________")
                print("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶_¶¶¶¶¶¶¶¶_________________________")
                print("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶___¶__¶¶¶¶¶¶________________________")
                print("_¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶_______________________")
                print("__¶¶¶¶¶¶¶¶¶______¶¶¶¶¶_______¶¶¶¶¶¶¶______________________")
                print("___¶¶¶¶¶¶________¶¶¶¶¶_________¶¶¶¶¶¶¶____________________")
                print("____¶¶¶¶_________¶¶¶¶¶__________¶¶¶¶¶¶¶¶__________________")
        if t == "A":
            print("")
            print("Properties")
            print("---------------")
            print(" ")
            print("House = 100000 money + 12 iron + 10 coal")
            print("")
            print("What do you want to buy?")
            ty = input("Enter:   ")
            if ty == "House":
                print("Check the Map")
                startcoal = startcoal - 10
                startiron = startiron - 12
                startmoney = startmoney - 100000
              
     
    if x == "Sell":
            print(" ")
            print("Fruits")
            print("---------------")
            print(" ")
            print ("Apple 4$")
            print ("Banana 8$")
            print(" ")
            print("Dungeon items")
            print("---------------")
            print(" ")
            print("Warlord stick 250$")
            print("Obsidian Crystal 450$ ")
            print("Magma Block 600$")
            print("Piece Magic Stick 700$")
            print("Piece of Asteroid 5000$")
            print("Dragon Bone 6000$")
            print(" ")
            yx = input(("Enter:     "))
            if yx == "Apple":
                z = int(input("Number of apples:   "))
                startapples = startapples - z
                startmoney = startmoney + z*5

            if yx == "Banana":
                z = int(input("Number of bananas:    "))
                startbananas = startbananas - z
                startmoney = startmoney + z*9
            if yx == "Warlord stick":
                z = int(input("Number of warlord sticks:    "))
                warlord_stick = warlord_stick - z
                startmoney = startmoney + z*250

            if yx == "Obsidian Crystal":
                z = int(input("Number of Obsidian Crystals:    "))
                obsidian_crystal = obsidian_crystal - z
                startmoney = startmoney + z*450

            if yx == "Magma Block":
                z = int(input("Number of Magma Blocks:    "))
                magma_block = magma_block - z
                startmoney = startmoney + z*600

            if yx == "Piece Magic Stick":
                z = int(input("Number of pieces of Magic stick:    "))
                piece_magic_stick = piece_magic_stick - z
                startmoney = startmoney + z*700

            if yx == "Piece of Asteroid":
                z = int(input("Number of pieces of asteroid:    "))
                piece_of_asteroid = piece_of_asteroid - z
                startmoney = startmoney + z*5000

            if yx == "Dragon Bone":
                z = int(input("Number of dragon bones:    "))
                bone_of_dragon = bone_of_dragon - z
                startmoney = startmoney + z*6000

    if x == "Invest":
        print(" ")
        print("Type B to buy ")
        print("Type S to sell ")
        ichoose = input("Choose:")
        print(" ")

        if ichoose == "S":
            print(" ")
            print("You Can Sell:")
            print(" ")
            print("Low Risk: Bitcoin, Ethereum, Apple, Microsoft")
            print(" ")
            print("High Risk: Solana, Dogecoin, Sandbox")
            print(" ")
            investsell = input("What do you want to Sell:      ")
            
            if investsell == "Bitcoin":
                print ("Price 30000$")
                print("Bitcoin = (-15%, 15%)")
                bbs = int(input("Number of Bitcoins:   "))
                print("You sold", bbs, "Bitcoins")
                BitcoinY = BitcoinY - bbs
                startmoney = startmoney + 30000*bbs + BitcoinP*bbs

            if investsell == "Ethereum":
                print ("Price 2000$")
                print("Ethereum = (-20%, 20%)")
                ees = int(input("Number of Ethereums:   "))
                print("You sold", ees, "Ethereums")
                EthereumY = EthereumY - ees
                startmoney = startmoney + 2000*ees + EthereumP*ees

            if investsell == "Apple":
                print ("Price 500$")
                print("Apple = (-25%, 25%)")
                aas = int(input("Number of Apple Stocks:   "))
                print("You sold", aas, "Apple Stocks")
                AppleY = AppleY - aas
                startmoney = startmoney + 500*aas + AppleP*aas

            if investsell == "Microsoft":
                print ("Price 400$")
                print("Microsoft = (-30%, 30%)")
                mms = int(input("Number of Microsoft Stocks:   "))
                print("You sold", mms, "Microsoft Stocks")
                MicrosoftYY = MicrosoftY - mms
                startmoney = startmoney + 400*mms + MicrosoftP*mms

            if investsell == "Solana":
                print ("Price 100$")
                print("Solana = (-75%, 75%)")
                sss = int(input("Number of Solana:   "))
                print("You sold", sss, "Solana")
                SolanaY = SolanaY - sss
                startmoney = startmoney + 100*sss + SolanaP*sss

            if investsell == "Dogecoin":
                print ("Price 5$")
                print("Dogecoin = (-100%, 100%)")
                dds = int(input("Number of Dogecoins:   "))
                print("You sold", dds, "Dogecoins")
                DogecoinY = DogecoinY - dds
                startmoney = startmoney + 5*dds + DogecoinP*dds

            if investsell == "Sandbox":
                print ("Price 1$")
                print("Sandbox = (-500%, 500%)")
                sss2 = int(input("Number of Sandbox:   "))
                print("You sold", sss2, "Sandbox")
                SandboxY = SandboxY - sss2
                startmoney = startmoney + 1*sss2 + BitcoinP*sss2

        
        if ichoose == "B":
            print(" ")
            print("You Can Invest in:")
            print(" ")
            print("Low Risk: Bitcoin, Ethereum, Apple, Microsoft")
            print("High Risk: Solana, Dogecoin, Sandbox")
            print(" ")
            invest = input("What do you want to Invest In?:      ")

            if invest == "Bitcoin":
                print ("Price 30000$")
                bb = int(input("Number of Bitcoins:   "))
                print("You bought", bb, "Bitcoins")
                BitcoinY = BitcoinY + bb
                startmoney = startmoney - 30000*bb

            if invest == "Ethereum":
                print ("Price 2000$")
                ee = int(input("Number of Ethereums:   "))
                print("You bought", ee, "Ethereums")
                EthereumY = EthereumY + ee
                startmoney = startmoney - 2000*ee

            if invest == "Apple":
                print ("Price 500$")
                aa = int(input("Number of Apple Stocks:   "))
                print("You bought", aa, "Apple Stocks")
                AppleY = AppleY + aa
                startmoney = startmoney - 500*aa

            if invest == "Microsoft":
                print ("Price 400$")
                mm = int(input("Number of Microsoft Stocks:   "))
                print("You bought", mm, "Microsoft Stocks")
                MicrosoftY = MicrosoftY + mm
                startmoney = startmoney - 400*mm

            if invest == "Solana":
                print ("Price 100$")
                ss = int(input("Number of Solana:   "))
                print("You bought", ss, "Solanas")
                SolanaY = SolanaY + ss
                startmoney = startmoney - 100*ss
            
            if invest == "Dogecoin":
                print ("Price 5$")
                dd = int(input("Number of Dogecoins:   "))
                print("You bought", dd, "Dogecoins")
                DogecoinY = DogecoinY + dd
                startmoney = startmoney - 5*dd
        
            if invest == "Sandbox":
                print ("Price 1$")
                ss2 = int(input("Number of Sandboxs:   "))
                print("You bought", ss2, "Sandboxs")
                SandboxY = SandboxY + ss2
                startmoney = startmoney - 1*ss2
    
    if x == "Investstats":
        print(" ")
        print("Bitcoin = (-15%, 15%)")
        print("Ethereum = (-20%, 20%)")
        print("Apple = (-25%, 25%)")
        print("Microsoft = (-30%, 30%)")
        print("Solana = (-75%, 75%)")
        print("Dogecoin = (-100%, 100%)")
        print("Sandbox = (-500%, 500%)")
        print(" ")

    if x == "Wallet":
        print(" ")
        print("You Have", startmoney, "$")
        print("You have", BitcoinY, "Bitcoin")
        print("You have", EthereumY, "Ethereum")
        print("You have", AppleY, "Apple Stocks")
        print("You have", MicrosoftY, "Microsoft Stoocks")
        print("You have", SolanaY, "Solana")
        print("You have", DogecoinY, "Dogecoins")
        print("You have", SandboxY, "Sandbox Tokens")

    if x == "Upgrades":
        print(Upgrade1, "$ ===> More health, Upgrade1")
        print(Upgrade2, "$ ===> More damage, Upgrade2")
        yz = input(("Enter Upgrade1 or Upgrade2: "))
        if yz == "Upgrade1":
         startmoney = startmoney - Upgrade1
         player_health =player_health*1.5
        if yz == "Upgrade2":
            startmoney = startmoney - Upgrade2
            player_damage = player_damage*2

    if x == "Stop":
        break
    if x == "DevTools":
        print(" ")
        print("*Enter the password*")
        print(" ")
        ld = input("Password code:   ")
        if ld == ("Xq45op12"):
            print(" ")
            print("Hi there Admin!")
            print(" ")
            print("New features unlocked!")
            print(" ")
            startapples = 1000000
            BitcoinY = 10000000000000
            startmoney = 9999999999999999999999999999999999999
            startdiamond = startdiamond + 100000000000000
            warlord_stick = warlord_stick + 100
            house = house + 1
    if x == "stop":
        break
    if x =="Inventory":
        print(startapples, "apples")
        print(startbananas, "bananas")
        print(startcoal, "coal")
        print (startiron, "iron")
        print(startcopper, "copper")
        print(startgold, "gold")
        print(startemerald, "emerald")
        print(startdiamond, "diamond")
        print(warlord_stick, "warlord stick")
        print(obsidian_crystal, "obsidian crystal")
        print(magma_block, "magma block" )
        print(piece_magic_stick, "piece of magic stick")
        print(piece_of_asteroid, "piece of asteroid" )
        print(bone_of_dragon, "bone of dragon")
        print(legendary_wood, "legendary wood")
        print(piece_of_artifact, "piece of artifact")
        print (stone_sword, "stone swords")
        print (basic_sword, "basic swords")
        
    if x == "Mine":
        print(" ")
        print("Mining cost 50$")
        print(" ")
        print("Type S ==> to Sell Minerals - 50$")
        print("Type M ==> to mine Minerals - 50$")
        print(" ")
        selectmine = input("Choose:   ")
        if selectmine == "M":
            startmoney = startmoney - minecost
            mr = random.randint(1,6)
            print("Your Number is...")
            print (mr)
            if mr == 1:
                print("You found 1 Emerald!")
                startemerald = startemerald + emerald
            if mr == 2:
                print("You found 1 Diamond!")
                startdiamond = startdiamond + diamond
            if mr == 3:
                print("You found 1 Gold!")
                startgold = startgold + gold
            if mr == 4:
                print("You found 1 copper")
                startcopper = startcopper + copper
            if mr == 5:
                print("You found 1 Iron!")
                startiron = startiron + iron
            if mr == 6:
                print("You found 1 Coal!")
                startcoal = startcoal + coal
        if selectmine == "S":
            print(" ")
            print("Coal +5$")
            print("Copper +15$")
            print("Iron +25$")
            print("Gold +50$")
            print("Emerald +150$")
            print("Diamond +500$")
            ys = input(("Enter:     "))
            if ys == "Coal":
                sr = int(input("Number of Coal:   "))
                startcoal = startcoal - sr
                startmoney = startmoney + sr*5

            if ys == "Copper":
                sr = int(input("Number of Copper:   "))
                startcopper = startcopper - sr
                startmoney = startmoney + sr*15
    
            if ys == "Iron":
                sr = int(input("Number of Iron:   "))
                startiron = startiron - sr
                startmoney = startmoney + sr*25

            if ys == "Gold":
                sr = int(input("Number of Gold:   "))
                startgold = startgold - sr
                startmoney = startmoney + sr*50

            if ys == "Emerald":
                sr = int(input("Number of Emerald:   "))
                startemerald = startemerald - sr
                startmoney = startmoney + sr*250

            if ys == "Diamond":
                sr = int(input("Number of Diamond:   "))
                startdiamond = startdiamond - sr
                startmoney = startmoney + sr*500
    
    if x == "World":
        print(" ")
        print("-----------------------------")
        print("Where are you going?")
        print("-----------------------------")
        print(" ")
        o = input("Type continue  ")
        if o == "continue":
            print(" ")
            print("    ▀   ")
            print("  ▀ ▀ ▀ ")
            print("    ▀   ")
            print(" ")
            print(" ")
            print("Choose: Middle, Up, Down, Right, Left")
            print(" ")
            p = input("Choose your next location:   ")
            if p == "Up":
                print("           ")    
                print("----------------------------------")
                print("You are now inside the crafting Zone")
                print("----------------------------------")
                print(" ")
                print("Type S ==> to see the crafting recipes")
                op = input("Enter S:    ")
                if op == ("S"):
                    print(" ")
                    print("--------RECIPES--------")
                    print(" ")
                    print("𝐵𝒶𝓈𝒾𝒸 𝓈𝓌𝑜𝓇𝒹 = (1) Warlord_stick + (1) Coal")
                    print(" ")
                    print("𝕾𝖙𝖔𝖓𝖊 𝕾𝖜𝖔𝖗𝖉 = (2) Warlord_stick + (1) Iron + (2) Emerald")
                    print(" ")
                    print("𝕸𝖆𝖌𝖎𝖈 𝕾𝖙𝖎𝖈𝖐 = (3) Magic stick pieces + (1) diamond")
                    print(" ")
                    print("𝕷𝖊𝖌𝖊𝖓𝖉𝖆𝖗𝖞 𝕰𝖝𝖈𝖆𝖑𝖎𝖇𝖚𝖗 = (1) Legendary wood + (2) Bone of dragon + (3) piece of asteroid + (1) piece of artifact")
                    print(" ")
                    ops = input("Type what sword you want to make:   ")
                    if ops == "Basic Sword":
                        print("You crafted a Basic Sword!")
                        basic_sword = basic_sword + 1
                        warlord_stick = warlord_stick - 1
                        coal = coal - 1
                    if ops == "Stone Sword":
                        print("You crafted a Stone Sword!")
                        stone_sword = stone_sword + 1
                        warlord_stick = warlord_stick - 2
                        iron = iron - 1
                        emerald = emerald - 2
                    if ops == "Magic Stick":
                        print("You crafted a Magic Stick!")
                        magic_stick = magic_stick + 1
                        piece_magic_stick = piece_magic_stick - 2
                        diamond = diamond - 1
                    if ops == "Legendary Excalibur":
                        legendary_excalibur = legendary_excalibur - 1
                        bone_of_dragon = bone_of_dragon - 2
                        piece_of_asteroid = piece_of_asteroid - 3

            if p == "Middle":
                print(" ")
                print("---------------------------------------")
                print("You are in the Crates area")
                print("----------------------------------------")
                print("Crates available:")
                print("Simple Crate -- 1250$")
                print("Advanced Crate -- 5500$")
                cm = input("Choose:    ")
                if cm == "Simple Crate":
                    print("In this crate you can get:")
                    print("2 Diamonds - 50%")
                    print("Magma Block - 30%")
                    print("Piece of Magic Stick - 18%")
                    print("Magic Stick - 2%")

                    sc = random.randint(1,100)
                    psc = print("Your number is", sc)
                    if psc <= 1 and psc >= 50:
                        print("You won 2 Diamonds!")
                        startdiamond = startdiamond + 2
                    if psc <= 51 and psc >= 80:
                        print("Magma Block!")
                        magma_block = magma_block + 1
                    if psc <= 81 and psc >= 98:
                        print("Piece of Magic Stick!")
                        piece_magic_stick = piece_magic_stick + 1
                    if psc <= 99 and psc >= 100:
                        print("Magic Stick!")
                        magic_stick = magic_stick + 1
                        startmoney = startmoney - 1250

                
                if cm == "Advanced Crate":
                    print("In this crate you can get:")
                    print("2 Ethereum - 50%")
                    print("3 Warlord Sticks - 30%")
                    print("Dragon Bone - 19%")
                    print("1M Money - 1%")
                    startmoney = startmoney - 5500

                    ac = random.randint(1,100)
                    pac = print("Your number is", ac)
                    if pac <= 1 and pac >= 50:
                        print("2 Ethereum")
                        EthereumY = EthereumY + 2
                    if pac <= 51 and pac >= 80:
                        print("3 Warlord Sticks!")
                        warlord_stick = warlord_stick + 3
                    if pac <= 81 and pac >= 99:
                        print("Dragon Bone!")
                        bone_of_dragon = bone_of_dragon + 1
                    if pac <= 99 and pac >= 100:
                        print("1M Money!")
                        startmoney = startmoney + 1000000

                    
            if p == "Down":
                print(" ")
                print("----------------------------")
                print("You are in the Forest")
                print("----------------------------")
                print("You can Look for apples and bananas here and them sell them")
                print(" ")
                print("Type A ===> to look for Apples")
                print("Type B ===> to look for Bananas")
                print(" ")
                cf = input("Choose:  ")

                if cf == "A":
                    print(" ")
                    print("Going for Apples is free but there is a possibility of losing money.")
                    print("   ")
                    lfa = input("Type a ==> to look for apples:   " )

                    if lfa == "a":
                        print(" ")
                        print(forest1probab)
                        print(" ")
                        if forest1probab == 1:
                            print("You lost 50 dolars!")
                            startmoney = startmoney - r*10
                        if forest1probab == 2:
                            print("Nothing happened")
                        if forest1probab == 3:
                            print("You just found 30 apples!")
                            startapples = startapples + 30
                        if forest1probab == 4:
                            print("You just lost 25 dolars!")
                            startmoney = startmoney - r*5
                        if forest1probab == 5:
                            print("You just found 40 apples!")
                            startapples = startapples + 40
                if cf == "B":
                    print(" ")
                    print("Going for Bananas is free but there is a possibility of losing money.")
                    print("   ")
                    lfb = input("Type a ==> to look for bananas:   " )

                    if lfb == "a":
                        print(" ")
                        print(forest1probab)
                        print(" ")
                        if forest1probab == 1:
                            print("You lost 100 dolars!")
                            startmoney = startmoney - r*20
                        if forest1probab == 2:
                            print("Nothing happened")
                        if forest1probab == 3:
                            print("You just found 30 bananas!")
                            startbananas = startbananas + 30
                        if forest1probab == 4:
                            print("You just lost 50 dolars!")
                            startmoney = startmoney - r*10
                        if forest1probab == 5:
                            print("You just found 40 bananas!")
                            startbananas = startbananas + 40
               

            if p == "Left":
                print(" ")
                print("--------------")
                print("*Who won the Football World Cup in 2010?*")
                print("--------------")
                xop = input("Enter:   ")
                if xop == "Spain":
                    print("Say it in spanish idiot")
                if xop == "España":
                    print("Remember this code: B3sop1")
                    print("")
                    print("*Final Boss code")
            if p == "Right":
                print(" ")
                print("You need to buy a house to come here")
                print("")
                if house == 1:
                    while True:
                        print(" ")
                        print(" ")
                        print("What do you want to do?")
                        print(" ")
                        print("Storage, Storage inventory, Menu")
                        xq = input("Choose:   ")
                        if xq == "Storage":
                            print("")
                            print("What do you want to do?")
                            print(" ")
                            print("A for storage things and B to take thing from the storage A")
                            xqs = input("Choose A or B:   ")
                            if xqs == "B":
                                xqsa = int(input("Number of apples:   "))
                                startapples = startapples - xqsa
                                storage_apples = storage_apples + xqsa
                                print("You have storaged the apples succesfully!")
                            if xqs == "A":
                                xqsa = int(input("Number of apples:   "))
                                startapples = startapples + xqsa
                                storage_apples = storage_apples - xqsa
                                print("You have storaged the apples succesfully!")
                            if xqs == "C":
                              print("You found the easter egg!, We are Maurici and Stepan, 2 of the main creators of this game and I just want to make sure you are getting good at this game so send something to cristianorlmano@gmail.com or stepangritsun@gmail.com to talk or something, bye!")
                                
                        if xq == "Storage inventory":
                            print(" ")       
                            print("Storage inventory") 
                            print(" ")
                            print(storage_apples, "apples")
                            print(storage_bananas, "bananas")
                            print(storage_coal, "coal")
                            print(storage_iron, "iron")
                            print(storage_copper, "copper")
                            print(storage_gold, "gold")
                            print(storage_emerald, "emerald")
                            print(storage_diamond, "diamond")
                            print(storage_warlord_stick, "warlord stick")
                            print(storage_obsidian_crystal, "obsidian crystal")
                            print(storage_magma_block, "magma block" )
                            print(storage_piece_magic_stick, "piece of magic stick")
                            print(storage_piece_of_asteroid, "piece of asteroid" )
                            print(storage_bone_of_dragon, "bone of dragon")
                            print(storage_legendary_wood, "legendary wood")
                            print(storage_piece_of_artifact, "piece of artifact")
                            print(storage_stone_sword, "stone swords")
                            print(storage_basic_sword, "basic swords")
                        if xq == "Menu":
                          break


    if x == "Work":
      print("Select your work:")
      print(" ")
      print("----------------------------------------")
      print("McDonalds ==> 60 seconds, 500$.")
      print("Officinist ==> 110 seconds, 1000$. ")
      print("Investor ==> 300 seconds, 3000$.")
      print("Medical Surgeon ==> 600 seconds, 7500$.")
      print("Mafia ==> 30 seconds, 30000$ (50% win or 50% end game)")
      print(" ")
      k = input("Choose your work:")
      uo = random.randint(1,2)
      if k == "McDonalds":
        print("Wait until the time finish to win your money:")
        for i in range(time_poor):
          print(time_poor - i)
          time.sleep(1)
        print("Congratulations, you finished working")
        startmoney += 500
        
      elif k == "Officinist":
        print("Wait until the time finish to win your money:")
        for i in range(time_normal):
          print(time_normal - i)
          time.sleep(1)
        print("Congratulations, you finished working")
        startmoney += 1000
          

      elif k == "Investor":
        print("Wait until the time finish to win your money:")
        for i in range(time_rich):
          print(time_rich - i)
          time.sleep(1)
        print("Congratulations, you finished working")
        startmoney +=3000

      elif k == "Medical Surgeon":
        print("Wait until the time finish to win your money:")
        for i in range(time_insane):
          print(time_insane - i)
          time.sleep(1)
        print("Congratulations, you finished working")
        startmoney += 9000

      elif k == "Mafia":
        if uo == 1:
            print("Wait until the time finish to win your money:")
            for i in range(time_Ilegal):
                print(time_Ilegal - i)
                time.sleep(1)
            print("Congratulations, you finished working")
            startmoney += 30000
        elif uo == 2:
            print("You got cought in the mafia, you will now go to jail!")
            for i in range(time_jail):
                print(time_jail - i)
                time.sleep(1)
            print("Congratulations, you got out of jail!")




    if startmoney < 0:
        print("You are in Bancarrupt")
        print("Game over")
        break
    if startapples < 0:
        print("If the world gives you apples, use them, if not dont try to break the rules of science")
        print("Game over")
        break
    if startbananas < 0:
        print("If the world gives you bananas, use them, if not dont try to break the rules of science")
        print("Game over")
        break
    if startcoal < 0:
        print("Srry for not letting you be hot this winter, but you have negative amount of coal")
        print("Game over")
        break
    if startcopper < 0:
        print("Dont try to build or use copper if you dont have it, you have negative amount of copper")
        print("Game over")
        break
    if startiron < 0:
        print("Dont try to be in Minecraft and create an iron armour, you have negative amount of Iron ")
        print("Game over")
        break
    if startgold < 0:
        print("Dont try to be like Mrbeast with 10M in Gold, you have negative amount of Gold")
        print("Game over")
        break
    if startemerald < 0:
        print("Dont try to be in Minecraft and trade with villagers, you have negative amount of Emeralds ")
        print("Game over")
        break
    if startdiamond < 0:
        print("Dont try to be in Minecraft and be so happy of finding diamonds, you have negative amount of Diamond ")
        print("Game over")
        break
    if warlord_stick < 0:
        print("You tried to have a XL stick, but you have a negative amount of warlord sticks")
        print("Game over")
        break
    if obsidian_crystal < 0:
        print("You wanted to have obsidian windows but you have a negative amount of obsidian crystals")
        print("Game over")
        break
    if magma_block < 0:
        print("You wanted to go to the Nether for some magma blocks, but you have a negative amount of them")
        print("Game over")
        break
    if piece_magic_stick < 0:
        print("You wanted to do some Magic, but you have a negative amount of pieces of magic stick")
        print("Game over")
        break
    if piece_of_asteroid < 0:
        print("You wanted to discover the aliens, but you have a negative ammount of pieces of asteroid")
        print("Game over")
        break
    if bone_of_dragon < 0:
        print("You wanted to talk with dragons, but you have a negative ammount of bones of dragon")
        print("Game over")
        break
    if legendary_wood < 0:
        print("You wanted to discover the paradise, but you have a negative ammount of legendary wood")
        print("Game over")
        break
    if piece_of_artifact < 0:
        print("You wanted to make your armour better, but you have a negative ammount of pieces of artifact")
        print("Game over")
        break
    if BitcoinY < 0:
        print("You wanted to be rich with cryptos, but you ran out of Bitcoin")
        print("Game over")
        break
    if EthereumY < 0:
        print("You wanted to be rich with cryptos, but you ran out of Ethereum")
        print("Game over")
        break
    if AppleY < 0:
        print("You wanted to be rich with stocks, but you ran out of Apple Inc. Stocks ")
        print("Game over")
        break
    if MicrosoftY < 0:
        print("You wanted to be rich with stocks, but you ran out of Microsoft stocks ")
        print("Game over")
        break
    if DogecoinY < 0:
        print("You wanted to be rich with cryptos, but you ran out of Dogecoin")
        print("Game over")
        break
    if SolanaY < 0:
        print("You wanted to be rich with cryptos, but you ran out of Solana")
        print("Game over")
        break
    if SandboxY < 0:
        print("You wanted to be rich with cryptos, but you ran out of Sandbox Token")
        print("Game over")
        break
    if basic_sword == 2:
        print("You only can have 1")
        print("Game over")
        break
    if stone_sword == 2:
        print("You only can have 1")
        print("Game over")
        break
    if magic_stick == 2:
        print("You only can have 1")
        print("Game over")
        break
    if legendary_excalibur == 2:
        print("You only can have 1")
        print("Game over")
    if ak_47 == 2:
        print("You look like a great terrorist ")
        print("Game over")
        break 
    if player_health < 1:
        print("You wanted to be SuperMan with infinite life, but you died ")
        print("Game over")
        print("───────▄▀▀▀▀▀▀▀▀▀▀▄▄")
        print("────▄▀▀░░░░░░░░░░░░░▀▄")
        print("──▄▀░░░░░░░░░░░░░░░░░░▀▄")
        print("──█░░░░░░░░░░░░░░░░░░░░░▀▄")
        print("─▐▌░░░░░░░░▄▄▄▄▄▄▄░░░░░░░▐▌")
        print("─█░░░░░░░░░░░▄▄▄▄░░▀▀▀▀▀░░█")
        print("▐▌░░░░░░░▀▀▀▀░░░░░▀▀▀▀▀░░░▐▌")
        print("█░░░░░░░░░▄▄▀▀▀▀▀░░░░▀▀▀▀▄░█")
        print("█░░░░░░░░░░░░░░░░▀░░░▐░░░░░▐▌")
        print("▐▌░░░░░░░░░▐▀▀██▄░░░░░░▄▄▄░▐▌")
        print("─█░░░░░░░░░░░▀▀▀░░░░░░▀▀██░░█")
        print("─▐▌░░░░▄░░░░░░░░░░░░░▌░░░░░░█")
        print("──▐▌░░▐░░░░░░░░░░░░░░▀▄░░░░░█")
        print("───█░░░▌░░░░░░░░▐▀░░░░▄▀░░░▐▌")
        print("───▐▌░░▀▄░░░░░░░░▀░▀░▀▀░░░▄▀")
        print("───▐▌░░▐▀▄░░░░░░░░░░░░░░░░█")
        print("───▐▌░░░▌░▀▄░░░░▀▀▀▀▀▀░░░█")
        print("───█░░░▀░░░░▀▄░░░░░░░░░░▄▀")
        print("──▐▌░░░░░░░░░░▀▄░░░░░░▄▀")
        print("─▄▀░░░▄▀░░░░░░░░▀▀▀▀█▀")
        print("▀░░░▄▀░░░░░░░░░░▀░░░▀▀▀▀▄▄▄▄▄")
        break 
    if storage_apples < 0:
        print("Dont take things that isnt yours! ")
        print("Game over")
        break 

    if boss2_health <= 0:
      print(" ")
      print(" ")
      print(" ")
      print(" ")
      print(" ")
      print(" ")
      print("Congratulations, hero! You have conquered the final quest and emerged victorious. As the credits roll, we would like to express our heartfelt gratitude for your incredible journey through our epic RPG adventure. This is our chance to extend special thanks to those whose contributions made this game a reality.\n")
      print(" ")
      print("To Tristan Jorritsma and Egor Sankov, our esteemed beta testers and photo models, your invaluable feedback and dedication pushed us to refine and polish every aspect of the game. Your tireless efforts helped us create a truly immersive and unforgettable experience.\n")
      print(" ")
      print("A profound appreciation goes out to Ksenia Mamaeva for capturing the essence of our game world through stunning photographs. Your artistic vision breathed life into every pixel, and your work will forever be cherished.\n")
      print(" ")
      print("We owe a debt of gratitude to Ilya Yarmalkevich for guiding us on the path to greatness as a remarkable teacher. Your wisdom and expertise guided us through the darkest dungeons of game development, allowing us to emerge triumphant.\n")
      print(" ")
      print("Marc Tresserras, your insightful opinions and suggestions played a vital role in shaping our game's narrative and mechanics. Your creative input allowed us to craft a story that resonates deeply with every player who ventured into our fantastical realm.\n")
      print(" ")
      print("Anier Velasco, Humberto Yusta, and Artem Padmaska, our esteemed teachers, your guidance and mentorship were instrumental in our growth as game developers. Your unwavering support and expertise paved the way for our success, and we are forever grateful for your unwavering dedication.\n")
      print(" ")
      print("To all the unsung heroes and the countless individuals who supported us on this arduous journey, we extend our deepest appreciation. Without your encouragement and enthusiasm, this game would never have reached such extraordinary heights.\n")
      print(" ")
      print("Finally, to our cherished players, YOU! We extend our utmost gratitude for embarking on this grand adventure with us. Your courage, determination, and unwavering support are the driving forces behind every line of code and every meticulously crafted world.\n")
      print(" ")
      print("With hearts filled with gratitude, we bid you farewell, knowing that you have become part of our legacy. You are the true heroes of this tale, and we hope the memories forged within our game will forever live on in your hearts.\n")
      print(" ")
      print("Made by Maurici, Stepan and Pedro as a project. Thanks everyone, now start again to find the easter egg, and if you send to cristianorlmano@gmail.com a screen capture, we will make a leaderboard in the website")
      print("Thank you for playing warrior!")

    print(" ")
    print(" ")
    print(" ")
