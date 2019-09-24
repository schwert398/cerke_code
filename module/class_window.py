import sys
import pygame
from pygame.locals import *
from module.class_constant import *
from module.class_variable import *

def locator(point):
    if point[0] <= 140: dest_x = 30
    elif point[0] < Const.display_size[0]-140: dest_x = point[0]-140
    else: dest_x = Const.display_size[0]-310
    
    if point[1] > Const.display_size[1]-140: dest_y = Const.display_size[1]-170
    else: dest_y = point[1]
    
    return dest_x, dest_y

class Window:
    base_window = pygame.Surface((280, 140), flags=pygame.SRCALPHA)
    base_window.set_alpha(0)
    base_window.fill((0, 0, 0, 127))
    base_window.fill((247, 247, 232, 7), (1, 1, 278, 138))
    button = pygame.Surface((130, 50), flags=pygame.SRCALPHA)
    button.set_alpha(0)
    button.fill((0, 0, 0))
    button.fill((245, 245, 230), (1, 1, 128, 48))
    
    
    def __init__(self, font_tuple, yes_no_list):
        self.question = font_tuple[0]
        self.question_pos_x = font_tuple[1][0]
        self.question_pos_y = font_tuple[1][1]
        self.yes = yes_no_list[0][0]
        self.yes_pos_x = yes_no_list[0][1][0]
        self.yes_pos_y = yes_no_list[0][1][1]
        self.no = yes_no_list[1][0]
        self.no_pos_x = yes_no_list[1][1][0]
        self.no_pos_y = yes_no_list[1][1][1]
    
    def render(self, screen, point):
        dest_x, dest_y = locator(point)
        
        while True:
            screen.blit(Window.base_window, (dest_x, dest_y))
            screen.blit(Window.button, (dest_x+8, dest_y+80))
            screen.blit(Window.button, (dest_x+142, dest_y+80))
            screen.blit(self.question, (dest_x+self.question_pos_x, dest_y+self.question_pos_y))
            screen.blit(self.yes, (dest_x+self.yes_pos_x, dest_y+self.yes_pos_y))
            screen.blit(self.no, (dest_x+self.no_pos_x, dest_y+self.no_pos_y))
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_SPACE:
                        return None
                    if event.key == K_y:
                        return True
                    if event.key == K_n:
                        return False
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if dest_y+80 <= y and y <= dest_y+130:
                        if dest_x+8 <= x and x <= dest_x+138:
                            return True
                        if dest_x+142 <= x and x <= dest_x+278:
                            return False
            pygame.display.update()

