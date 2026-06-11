import pygame
import sys


class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, font):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = font

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color

        pygame.draw.rect(screen, current_color, self.rect, border_radius=10)
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False


class UI:
    def __init__(self, width=1024, height=768):
        pygame.init()
        pygame.mixer.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("AI Rock-Paper-Scissors")

        # Fonts
        self.font_title = pygame.font.SysFont("Arial", 54, bold=True)
        self.font_body = pygame.font.SysFont("Arial", 28)
        self.font_score = pygame.font.SysFont("Arial", 36, bold=True)

        # Palette Colors
        self.COLOR_BG = (30, 30, 40)
        self.COLOR_PANEL = (45, 45, 60)
        self.COLOR_PRIMARY = (70, 130, 180)
        self.COLOR_ACCENT = (100, 200, 100)

    def draw_text(self, text, font, color, x, y, center=False):
        surface = font.render(text, True, color)
        rect = surface.get_rect()
        if center:
            rect.center = (x, y)
        else:
            rect.topleft = (x, y)
        self.screen.blit(surface, rect)

    def draw_background(self):
        self.screen.fill(self.COLOR_BG)