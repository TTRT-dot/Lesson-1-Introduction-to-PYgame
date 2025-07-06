#import and initialize pygame
import pygame
pygame.init()
white = (255,255,255)
blue = (0,0,255)

#Clock
clock = pygame.time.Clock()

#creating the display surface object
#or specific dimention...e(X,Y)
display_surface=pygame.display.set_mode((1940,1020))

#set the pygame widnow name
pygame.display.set_caption("Football Images")

#creating a surface object, image is drawn on it.
image=pygame.image.load('Football.png')
image1=pygame.image.load('fireball.png')
#Set the size for the image
DEFAULT_IMAGE_SIZE=(900,900)

#Scale the image to your needed size
image = pygame.transform.scale(image,DEFAULT_IMAGE_SIZE)
image1 = pygame.transform.scale(image1,DEFAULT_IMAGE_SIZE)
#Set a default position
DEFAULT_IMAGE_POSITION=(1000,10)
DEFAULT_IMAGE1_POSITION=(10,10)
#infinate loop
while True:
    display_surface.fill(white)
    display_surface.blit(image,DEFAULT_IMAGE_POSITION)
    display_surface.blit(image1,DEFAULT_IMAGE1_POSITION)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.flip()
    clock.tick(30)