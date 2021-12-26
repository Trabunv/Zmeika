import pygame


class Button:
    def __init__(self, x=0, y=0, width=0, height=0, text='', rgb=(255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.str = text
        self.font = pygame.font.SysFont('serif', 48)
        self.text = self.font.render(self.str, False, (0, 180, 0))
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill(rgb)
        # self.button = pygame.Rect(self.x, self.y, self.width, self.height)

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def set_font(self, font_path, size=48, rgb=(0, 0, 0)):
        self.font = pygame.font.Font(font_path, size)
        self.text = self.font.render(self.str, False, rgb)

    def set_text_color(self, rgb=(0, 0, 0)):
        self.text = self.font.render(self.str, False, rgb)

    def set_button_color(self, rgb):
        self.surf.fill(rgb)

    def set_text(self, text):
        self.text = self.font.render(text, False, (0, 180, 0))

    def is_pressed(self):
        x, y = pygame.mouse.get_pos()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                # sys.exit()
                pygame.quit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if (i.button == 1
                        and (self.x <= x <= self.x + self.width)
                        and (self.y <= y <= self.y + self.height)):
                    return True
        return False

    def is_hovered(self):
        x, y = pygame.mouse.get_pos()
        if (self.x <= x <= self.x + self.width) and (self.y <= y <= self.y + self.height):
            return True
        return False

    def draw(self, screen):
        text_rect = self.text.get_rect(center=(self.x + self.width/2, self.y + self.height/2))
        screen.blit(self.surf, (self.x, self.y))
        screen.blit(self.text, text_rect)
