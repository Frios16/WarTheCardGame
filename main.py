import pygame #imports 
import random 


pygame.init() #initializes Pygame
pygame.display.set_caption("WAR.. The Card game") #sets the window title 
screen = pygame.display.set_mode ((700,500)) #Creates game screen 

doExit = False 
clock = pygame.time.Clock() # start game clock 
turn = False 

class card: 
    def __init__(self,suit,number):
      self.suit = suit
      self.number = number
    def draw(self,x,y):
        pygame.draw.rect(screen, (255,255,255), (x, y,100,180))
        pygame.draw.rect(screen, (0,0,0), (x,y,100,180), 3)
        font = pygame.font.Font('freesansbold.ttf',24)
        text = font.render(str(self.number),1,(0,0,0))
        text2 = font.render(str(self.suit),1,(250,0,0))
        screen.blit(text, (x+30, y+30))
        screen.blit(text2, (x+10, y+60))

        #font = pygame.draw.rect(screen, (255,255,255), (x, y,100,180))
        #text = 
        #text2 = 
          #x+30 and y+30


#create a bunch of bricks.
#c1 = card(0,4)
#c2 = card(2,9)
#c3 = card(1,7)

Deck = list() # creates lIsT(array) called deck
for j in range(4):
    for i in range(13):
        Deck.append(card(j,i))

random.shuffle(Deck) # randomizes the deck / shuffles

p1hand = list()
p2hand = list()
p1Discard = list()
p2Discard = list() 


for i in range(26): # goes through 
    p1hand.append(Deck[i])
for j in range (26, 52):
    p2hand.append(Deck[j])



while not doExit: #game loop -----------------------------------
  clock.tick(60) #FPS

  event =pygame.event.wait()

  if event.type == pygame.QUIT:#mo changed this to all uppercase
    doExit = True 
  if event.type == pygame.MOUSEBUTTONDOWN:
    turn = True 
  if event.type == pygame.MOUSEBUTTONUP:
    turn = False 
  if event.type == pygame.MOUSEMOTION:
    mousePos = event.pos


  #Game logic-------------------------------------

  if len(p1hand)<=0 or len(p2hand)<=0:
      if len(p1Discard)>len(p2Discard):
          print("Player 1 wins!")
      else:
          print("Player 2 wins!")
      doExit = True 

  if turn and len(p1hand) > 0 and len(p2hand) > 0:

    if p1hand[len(p1hand)-1].number>p2hand[len(p2hand)-1].number:

      print("player 1 wins round! ")
      p1Discard.append(p1hand[len(p1hand)-1])
      p1Discard.append(p2hand[len(p2hand)-1])
      p1hand.pop(len(p1hand)-1)
      p2hand.pop(len(p2hand)-1)

    else:
      print("player 2  wins round!")
      p2Discard.append(p1hand[len(p1hand)-1])
      p2Discard.append(p2hand[len(p2hand)-1])
      p1hand.pop(len(p1hand)-1)
      p2hand.pop(len(p2hand)-1)



  

  # render section --------------------------------
  screen.fill((0,150,0)) # Screen color

  #for i in range(52):
   #   Deck[i].draw(20+i*5, 20+i*3)

  for i in range(0,len(p1Discard)):
    p1hand[i].draw( 400+4*i, 50 )
  for i in range (0,len(p2Discard)):
    p2hand[i].draw( 400+4*i, 250 )

  #mo commented these out, you already had them above your game loop
  #p1hand = list()
  #p2hand = list()
  #p1Discard = list()
  #p2Discard = list() 

  #c1.draw(250,100)
  #c2.draw(100,200)
  #c3.draw(400,200)


  #update game screen
  pygame.display.flip()

pygame.quit()
