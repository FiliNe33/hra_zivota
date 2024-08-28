import numpy as np
import pygame
import time

# Nastavení barev buněk pomocí RGB kódů
barva_zive = (139, 117, 0)
barva_mrtve = (205, 205, 180)
barva_umirajici = (205, 205, 0)
barva_mrizky = (225, 225, 225)

pygame.init()
pygame.display.set_caption("hra života")

# Aktualizace stavů buněk a přidělování barev
def akt(obrazovka, bunky, vel, progres=False): 
    akt_bunky = np.zeros((bunky.shape[0], bunky.shape[1]))

    for rad, sl in np.ndindex(bunky.shape):
        zive = np.sum(bunky[rad-1:rad+2, sl-1:sl+2]) - bunky[rad, sl]

        if bunky[rad, sl] == 1:
            barva = barva_zive
            if zive < 2 or zive > 3:
                if progres:
                    barva = barva_umirajici
                    
            elif 2 <= zive <= 3:
                akt_bunky[rad, sl] = 1

        else:
            barva = barva_mrtve
            if zive == 3:
                akt_bunky[rad, sl] = 1
                if progres:
                    barva = barva_zive

        # Vykreslení 
        pygame.draw.rect(obrazovka, barva, (sl * vel, rad * vel, vel - 1, vel - 1))

    return akt_bunky

# Hlavní funkce řídící průběh hry
def main():
    obrazovka = pygame.display.set_mode((900, 600))
    bunky = np.zeros((60, 90))

    obrazovka.fill(barva_mrizky)
    akt(obrazovka, bunky, 10)

    pygame.display.update()

    spusteno = False

    # Nekonečná smyčka s hlavními ovládacími prvky
    while True:
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                pygame.quit()
                return
            
            elif x.type == pygame.KEYDOWN:
                if x.key == pygame.K_SPACE:
                    spusteno = not spusteno
                    akt(obrazovka, bunky, 10)
                    pygame.display.update()

            if pygame.mouse.get_pressed()[0]:
                poz = pygame.mouse.get_pos()
                bunky[poz[1] // 10, poz[0] // 10] = 1
                akt(obrazovka, bunky, 10)
                pygame.display.update()

        obrazovka.fill(barva_mrizky)

        if spusteno:
            bunky = akt(obrazovka, bunky, 10, progres=True)
            pygame.display.update()

        time.sleep(0.01)

# Je-li soubor spuštěn jako hlavní program, spustí se funkce main
if __name__ == "__main__":
    main()