import pygame

pygame.init()

screen=pygame.display.set_mode((200,200))
done=False
while not done:
    for event in pygame.event.get():
      if pygame.event==pygame.QUIT:
         done=True

    pygame.draw.rect(screen,(90,130,20),pygame.Rect(30,30,60,60))

    pygame.display.flip()