import pygame, sys, math, time

ctime = time.localtime()
size = width, height = 760, 600
pygame.init()
win = pygame.display.set_mode(size)


class Hand:
    def __init__(self, color, length, rotation, value):
        self.color = color
        self.length = length
        self.rotation = rotation
        self.angle = math.pi / 30 * value

    def draw(self):
        color = self.color
        length = self.length
        angle = self.angle
        cos = math.cos(angle - math.pi / 2)
        sin = math.sin(angle - math.pi / 2)
        pygame.draw.line(
            win,
            color,
            (width / 2, height / 2),
            (width / 2 + length * cos, height / 2 + length * sin),
            5)

    def update(self):
        self.angle = (self.angle + self.rotation)


storks = [
    Hand(color=(255, 0, 0), length=200, rotation=math.pi / 30, value=ctime.tm_sec),  # sec stroke
    Hand(color=(0, 255, 0), length=150, rotation=math.pi / 1800, value=ctime.tm_min),  # minutes stroke
    Hand(color=(100, 100, 255), length=100, rotation=math.pi / 108000, value=ctime.tm_hour * 5)  # hours stroke
]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    win.fill((40, 40, 40))
    pygame.draw.circle(win, (0, 255, 128), (width / 2, height / 2), 250, 15)
    for s in storks:
        s.update()
        s.draw()
    pygame.display.flip()
    time.sleep(1)
