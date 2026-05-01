import pygame

class PyGameVisuals:
    def __init__(self, width=400, height=400, name=None, defaultFill=(0, 0, 0), scale=1):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.defaultFill = defaultFill
        self.clock = pygame.time.Clock()
        self.scale = 1
        pygame.display.set_caption(name)

    def clear(self):
        self.screen.fill(self.defaultFill)

    def drawRectangle(self, x, y, width=10, height=10, color=(255, 255, 255)):
        rectangle = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen, color, rectangle)

    def drawEntity(self, entity, color):
        pos = entity.components["position"]
        if not pos: return

        self.drawRectangle(pos.x*self.scale, pos.y*self.scale, color=color)

    def drawText(self, text, x, y, font, color=(255, 255, 255)):
        img = font.render(text, True, color)
        self.screen.blit(img, (x, y))

    def tick(self, fps):
        self.clock.tick(fps)

    def setScale(self, scale):
        self.scale = scale

    def update(self):
        pygame.display.flip()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True