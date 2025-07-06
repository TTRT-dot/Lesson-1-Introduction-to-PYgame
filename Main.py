#import necessary Libraries
import pygame

#initialize required modules
pygame.init()

#Setup Window geometry
screen=pygame.display.set_mode((1960,1010))

#Create a loop to run till the game is quit by user
done=False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    #Make the chnges visible
    pygame.display.flip()