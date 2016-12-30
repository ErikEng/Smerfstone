# Written Feb 2015 (It was one of my first programs that weren't part of an assignment)
#here's my simple attempt at writing a simple hearthstone game


#so the idea is that I have a list for the deck, the hand, the board and perhaps graveyard if i can be bothered
#I have a carddraw func that will genarate unique cards from the deck
#then you can at the first turn choose to return some cards by rerolling the carddraw without adding the drawn cards to the used pile
#then you can 
#first value is attack, second is life, third is mana cost

from random import randint
from tkinter import *
i=0
j=-1
k=0
repeatcheck=0
answ=-1
decksize=19
fatiguedmg=0

numattackers=0
usedcards=[]
enusedcards=[]
enhand=[]
hand=[]
spellhand=[]
mana=0
enmana=0
turn=0
enboard=[]
frboard=[]
c=0
enlife=20
frlife=20
decksize=12
endecksize=12



def greetings():
    print("Greeting! This is the super official Smerfstone[9]")
    print("The game of smerfstone is about killing your opponent with creatures and spells")
    print("But due to budget constraints you'll have to use a lot of imagination")
    print("The cards work as following")
    print("The first value is the damage a spell or minion can deal")
    print("The second value is the minions health, spells have 0 health")
    print("The third value is the mana cost for each card")
    print("Your mana replenishes and increases by ten at the start of each turn")
    print("The first one to deal 20 damage to the opponent wins")
    boardprint("The Smerfstone Layout")
    print("Here's the board")
    print("Your hand and the board are as of now empty, but when the game starts it will be filled with numbers")
    print("Every triplet of numbers is one card")
    print("So for example, [3,2,20, 1,1,10], would mean that you have")
    print("One card with 3 attack and 2 health for 20 mana")
    print("And 1 card with 1 attack and one heath for 10 mana")
    print("cards with 0 hp are spells that instantly will deal its damage to a minion or the opponent")

#general funcs
def spacecont():
    anykey=input("Press enter to continue")
    if anykey!=[]:
        print(" ")
              
def manaq():
    if mana!=0:
        print("Your Hand")
        print(hand)
        yesorno("You still have mana left, do you wish to play another card?:")
        global cont
        if cont==1:
           summonface()
        else:
           return
    else:
        return


def yesorno(question):
        global cont
        cont=str(input(question))
        if cont=="yes" or cont=="Yes" or cont=="YES" or cont=="y":
           cont=1
        
        elif cont=="no" or cont=="NO" or cont=="No" or cont=="n" or cont=="N":
            cont=0
        
        else:
            print("I didn't understand that, write 'yes' or 'no'")
            yesorno(question)


    
#Smerfstone funcs
def numbertocard(cardnr, playerhand):
   if playerhand==usedcards:
     ahand=hand
   else:
      ahand=enhand
   c=cardnr
   if c==1:
      ahand.extend([2, 1, 10])
    
   elif c==2:
      ahand.extend([3, 2, 20])
  
   elif c==3:
      ahand.extend([2, 3, 10])

   elif c==4:
      ahand.extend([3, 4, 30])
   
   elif c==5:
      ahand.extend([5, 5, 50])
  
   elif c==6:
      ahand.extend([2, 0, 10])

   elif c==7:
      ahand.extend([3,0, 20])
      
   elif c==8:
       ahand.extend([2,0, 10])
       
   elif c==9:
       ahand.extend([4, 0, 30])
       
   elif c==10:
       ahand.extend([2, 1, 10])

   elif c==11:
       ahand.extend([4,5, 40])
   elif c==12:
       ahand.extend([1,3,10])
   elif c==13:
       ahand.extend((3,4,40))
   elif c==14:
       ahand.extend((3,2,20))
   elif c==15:
       ahand.extend((5,7,60))
   elif c==16:
       ahand.extend((4,5,40))
   elif c==17:
       ahand.extend((5,1,30))

   else:
      ahand.extend([2, 2, 10])


    

def carddraw(carddeck, decksize):
   if len(carddeck)//3==decksize:

       fatiguedmg+=1
       print("You are out of cards! You take", fatiguedmg, "fatigue damage!")
       frlife-=fatiguedmg
   n=randint(1,decksize)
   for card in carddeck:
      while card==n:
         n=randint(1,decksize)
   numbertocard(n,carddeck)
   carddeck.append(n)



            
def boardprint(face):
     print("---------------------------------------------------------------------")
     print("Turn", turn, "         ",face)
     print("Enemy HP:", enlife, "         enmana", enmana)
     print("Enemy hand [", len(enhand)//3, "cards ]")
     print(enhand, spellhand)
     print("The Board")
     print(" ")
     print(enboard)
     print("vs")
     print(frboard)
     print(" ")
     print("Your HP:", frlife, "              Mana:", mana)
     print("        Your Hand", "[",len(hand)//3 , "cards ]")
     print(hand)
     print("---------------------------------------------------------------------")

def summonface():

    global mana
    cardnum=int(input("What card will you play?: "))
    cardtoplay=hand[0+3*cardnum-3:3+3*cardnum-3]
    if cardnum>len(hand)//3:
        print("You don't have that many cards!")
        
        yesorno("Do you wish to play another card?")
        if answ==1:
          summonface()
        else:
           return
    if cardtoplay[2]>mana:
      while cardtoplay[2]>mana:
        print("You don't have enough mana!")
        yesorno("Do you wish to play another card?")
        if answ==1:
          summonface()
        else:
           break
    elif cardtoplay[1]==0:
            mana=mana-cardtoplay[2]
            hand[3*cardnum-3:3*cardnum]=[]
            spellface(cardtoplay)
                   
    else:
         frboard.extend(cardtoplay)
         hand[0+3*cardnum-3:3+3*cardnum-3]=[]
         mana=mana-cardtoplay[2]
         print("You have summoned a", cardtoplay, "to the battlefield!")
         print("You have", mana , "mana left")

    manaq()


def attackerscheck():
    global numattackers
    numattackers=len(frboard)//3
    print("You have", numattackers, "minions ready to attack")
    return

def spellface(dacard):
    global enface
    global enboard
    global enlife
    print("You cast a",dacard[0], "damage spell!")

    spelltarget=int(input("What opponent do you wish to cast the spell on?:"))
    if spelltarget==0:
          enlife-=dacard[0]
          print("Your opponents life is down to", enlife,"!")
    elif spelltarget>len(enboard)/3:
            print("There's no such target!")
            spellface(dacard)
    else:
        enboard[spelltarget*3-2]-=dacard[0]

        deathcheck(" ", 1)
   

        


            
def attackface(nrattackers):
    global enlife
    global enboard
    anykey=[]
    print("You have", nrattackers, "minions ready to attack")
    for attacker in range(nrattackers):
        defender=int(input("Who shall be attacked?"))
        if defender==0:
            enlife-=frboard[3*attacker]
            print("You dealt", frboard[3*attacker], "damage to the opponent")
     
        elif defender>len(enboard)//3:
            print("That enemy doesn't exist, but you get an extra shot at attacking")
            defender=int(input("Who shall be attacked?"))
            if defender==0:
               enlife-=frboard[0]
            elif defender>enboard/3:
               print(frboard[0+3*attacker-3:3+3*attacker-3],"didn't attack")
            else:
               enboard[1+3*defender-3]-=frboard[0+3*attacker-3]
        else:
            enboard[-2+3*defender]-=frboard[3*attacker]
            frboard[1+3*attacker]-=enboard[-3+3*defender]

    
def deathcheck(deathname,deathtype):
 numbe=-1
 enumbe=-1
 nrdead=0
 for value in (frboard):
  numbe+=1
  if value<=0:
        print("Your minion number", 1+numbe//3, "has died")
        frboard[numbe-1 :numbe+2]=[]
        nrdead+=1
        
 for envalue in (enboard):
     enumbe+=1
     if envalue<=0:
        print("The opposing minion number", 1+enumbe//3, "has died")
        enboard[enumbe-1:enumbe+2]=[]
        nrdead+=1
 if nrdead!=0:
    boardprint(deathname)
 if deathtype==1:
     return


 print("Your turn is over")
 spacecont()


def herodeath():
 if enlife<=0:
        print("Your opponent has no HP left!")
        print("Victory!")
        credits()
        
 if frlife<=0:
        print("You have no HP left!")
        print("Defeat!")
        credits()
def credits():

    print("thanks for playing Smerfstone[9]")
    print("The End")
      


#enemy "strat"
def spellsorting():
  print("spellsort")
  nu=-1
  friendlyhealth=frboard[1::3]
  for number in enhand:
      nu+=1

      if number==0:
          spellcard=enhand[nu-1:nu+2]
          spellhand.extend(spellcard)
          enhand[nu-1:nu+2]=[]
  #print("hi")
  nu=-1
  for number in enhand:
      nu+=1

      if number==0:
 
          spellcard=enhand[nu-1:nu+2]
          spellhand.extend(spellcard)
          enhand[nu-1:nu+2]=[]

def ensum():
    playable=[]
    h=0
    ho=0
    himana=0
    hicard=[]
    global repeatcheck
    global enmana
    manacostls=enhand[2::3]
    for cost in manacostls:
        h+=1
        if cost>himana and cost<=enmana:
          himana=cost
          hicard=enhand[h*3-3:h*3]
          ho=h

    if h==0:
        print("the opponent played no minions")
        return
    else:
        enboard.extend(hicard)
        enmana-=himana
        enhand[ho*3-3:ho*3]=[]
    if enmana==0:

        return
   
    elif repeatcheck==0:
        repeatcheck=1
        ensum()
    else:
        return
   
        
def spellcast():
  #print("spell start")
  mu=-1
  mum=0
  tu=0
  bu=0

  frhpls=frboard[1::3]
  spdmgls=spellhand[0::3]
  #print(mu, "mu1")
  #print("spdmg1", spdmgls)
  global frlife
  global enmana
  if spellhand==[]:
      print("no spells")
      return
  if frhpls!=[]:
    for frminhp in frhpls:
      tu+=1
      #print("kom")
      mu=0
      mum=0
      for spdmg in spdmgls:
     
          mu+=1
          mum+=1
          spdmgls=spellhand[0::3]
          #print(spdmg, "spdmg")
          #print(spdmgls, "spdmgls")
          #print("cow")
          #print(mu, "muvi")
          #print(mum, "mum")
          #print(spellhand, "spellhand")
          #print(spdmgls, "spDmgLs")
          #print(len(spdmgls), "lenght")
          
          if mu>len(spdmgls):
              #print("why is this happening?")
              break
          if enmana==0:
             
             break
          #print(spellhand[mu*3-1], "spellmana")
          if spdmg==frminhp or spdmg==frminhp+1 and spellhand[mu*3-1]<enmana:
              #print("nr", tu, "hp")
              #print("nr", mu, "attack")
              #print(spellhand[mu*3-1], ":spellh mana", enmana, "enmana")
              kortman=spellhand[mu*3-1]
              if kortman>enmana:
                  #print("error, still something weird")
                  return
             # print(spellhand,  "ori")
              #print(frboard, "frboard")
              #print(tu, "tu")
 
              defcard=frboard[tu*3-3:tu*3]
              sp2play=spellhand[mum*3-3:mum*3]
              enmana-=spellhand[mum*3-1]
              
              print("The opponent cast a", sp2play,"spell and killed your",defcard, "!")
              frboard[tu*3-3:tu*3]=[]
              spellhand[mu*3-3:mu*3]=[]
              #print(enmana, "enman")
              spellcast()



def enatk():
  tu=0
  bu=0
  frhpls=frboard[1::3]
  spdmgls=spellhand[0::3]
  
  print(spdmgls, "spd")
  enmdls=enboard[::3]
  print(enmdls, "enmdls")
  nrrnds=len(frhpls)
  global frlife
  global enmana
 
  for mindmg in enmdls:
      tu+=1
      print("kom")
      mu=0
      mum=0
     
      if frhpls!=[]:
       for frminhp in frhpls:
            print(enmdls, "enmdls")
            print("teeste")
            bu+=1
            if len(frboard)==0:
             frlife-=mindmg
             print("You were attacked by a minion and lost", mindmg, "health")
            if -2+bu*3>len(frboard):
                print("y bu?")
                break
            elif mindmg<=frboard[bu*3-3] and mindmg>=frboard[bu*3+-2]:    #if minion has enough atk to kill and has lower dmg
               print("teste fly")
               print(enboard, "enboard")
               print(frboard, "frboard")
               enboard[tu*3-2]-=frboard[bu*3-3]
               frboard[bu*3-3:bu*3]=[]
               print(enboard, "enboard")
               print(frboard, "frboard")
              
               if enboard[tu*3-2]<=0:
                   enboard[tu*3-3: bu*3]=[]
      
            else:
                frlife-=mindmg
                print("An enemy minion attacked you, you lost", mindmg, "hp!")
      else:
           print(nrrnds, "nrrnds")
           
           frlife-=mindmg
           print("An enemy minion attacked you, you lostidoodled", mindmg, "hp!")
            


#the game order below
greetings()
spacecont()
f=0
for i in range(3):
   carddraw(usedcards, decksize)
for f in range(4):
   carddraw(enusedcards, endecksize)

while enlife>0 and frlife>0:
    j+=1
    mana=10+j*10
    enmana=10+j*10
    turn=1+j
    carddraw(usedcards, decksize)
    carddraw(enusedcards, endecksize)
   
    boardprint("Opening Phase")
    attackerscheck()
    summonface()
    if numattackers>0:
      boardprint("Attacking Phase")
      attackface(numattackers)
      spacecont()
      deathcheck("Death Phase",0)
    if enlife<=0 or frlife<=0:
      break
    spacecont()
    spellsorting()
    boardprint("Enemy Phase")
    spellcast()
    enatk()
    ensum()
    boardprint("Enemy Phase")
    spacecont()
    #deathcheck()
herodeath()
