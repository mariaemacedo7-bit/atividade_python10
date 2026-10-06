import pygame

pygame.init()

tela = pygame.display.set_mode((800, 600))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

    tela.fill("skyblue")
    pygame.draw.circle(tela, "yellow", (100, 50), 30)
    pygame.display.flip()


    