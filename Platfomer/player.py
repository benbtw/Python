import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.image = pygame.image.load("sunnyland\PNG\sprites\player\idle\player-idle-1.png")
        self.idle = [pygame.image.load("sunnyland\PNG\sprites\player\idle\player-idle-1.png"), 
                     pygame.image.load("sunnyland\PNG\sprites\player\idle\player-idle-2.png"), 
                     pygame.image.load("sunnyland\PNG\sprites\player\idle\player-idle-3.png"),
                      pygame.image.load("sunnyland\PNG\sprites\player\idle\player-idle-4.png")]
        self.walk_right = [pygame.image.load("sunnyland\PNG\sprites\player\Run\player-run-1.png"),
                           pygame.image.load("sunnyland\PNG\sprites\player\Run\player-run-2.png"),
                           pygame.image.load("sunnyland\PNG\sprites\player\Run\player-run-3.png"),
                           pygame.image.load("sunnyland\PNG\sprites\player\Run\player-run-4.png"),
                           pygame.image.load("sunnyland\PNG\sprites\player\Run\player-run-5.png"),
                           pygame.image.load("sunnyland\PNG\sprites\player\Run\player-run-6.png")]
        self.index = 0
        self.count = 0
        self.direction = "Right"
    
    def update(self, dt):
        self.count += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.position.x  -= 300  * dt
            if self.count > 6:
                self.index += 1
                self.count = 0
            if self.index >= len(self.walk_right):
                self.index = 0
            self.image = self.walk_right[self.index]
            self.direction = "Left"
        elif keys[pygame.K_d]:
            self.position.x += 300  * dt
            if self.count > 6:
                self.index += 1
                self.count = 0
            if self.index >= len(self.walk_right):
                self.index = 0
            self.image = self.walk_right[self.index]
            self.direction = "Right"
        else:
            if self.count > 6:
                self.index += 1
                self.count = 0
            if self.index >= len(self.idle):
                self.index = 0
            self.image = self.idle[self.index]
    
    def draw(self, surface):
        if self.direction == "Right":
            surface.blit(self.image, self.position)
        elif self.direction == "Left":
            surface.blit(pygame.transform.flip(self.image, True, False), self.position)