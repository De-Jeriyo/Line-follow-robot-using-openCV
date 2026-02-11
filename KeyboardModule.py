import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((100, 100))


def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()

    return ans


def main():
    if getKey('UP'):
        print('Key Up was pressed')
    if getKey('DOWN'):
        print('Key Down was pressed')
    if getKey('LEFT'):
        print('Key Left was pressed')
    if getKey('RIGHT'):
        print('Key Right was pressed')
    if getKey('a'):
        print('Key A was pressed')
    if getKey('s'):
        print('Key S was pressed')
    if getKey('d'):
        print('Key D was pressed')
    if getKey('w'):
        print('Key W was pressed')

if __name__ == '__main__':
    init()
    while True:
        main()