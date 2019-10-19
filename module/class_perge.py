import sys
import pygame
from pygame.locals import *
from module.class_variable import *

pygame.init()
pygame.font.init()
pygame.display.set_caption("font test")
char_font = pygame.font.Font("C:\\Users\\atshr\\AppData\\Local\\Programs\\Python\\Python37-32\\laboratory\\font\\pek_tak.ttf", 500)
num_font = FontSet.font_file

class PergeFont:
    vowel = ("a", "i", "u", "e", "o", "y")
    tone = ("5", "?")
    # 2次元配列の3次元配列(頭子音の有無、語長の順にアクセス)(ダミーの配列をいれている)
    char_pos = (
                   (
                       (None), 
                       [(12, 12)], 
                       ((0, 10), (68, 10)), 
                       ((5, 25), (70, 5), (70, 60)), 
                       ((5, 25), (70, 3), (70, 58), (70, 108)), 
                       ((2, 17), (50, 3), (50, 58), (50, 108), (120, 58)), 
                       ()
                   ), 
                   (
                       (None), 
                       [(12, 12)], 
                       ((15, 8), (15, 75)), 
                       ((15, 3), (15, 45), (15, 110)), 
                       ((5, 3), (5, 30), (5, 105), (75, 70)), 
                       ((5, 3), (5, 30), (5, 105), (75, 30), (75, 80)), 
                   ),
               )

    char_size = (
                    (
                       (None), 
                       [(180, 180)], 
                       ((100, 170), (100, 200)), 
                       ((120, 150), (120, 150), (120, 150)), 
                       ((80, 150), (120, 100), (120, 100), (120, 100)), 
                       ((80, 150), (100, 100), (100, 100), (100, 100), (100, 100)),
                       ()
                    ), 
                    (
                       (None), 
                       [(180, 180)], 
                       ((150, 120), (150, 120)), 
                       ((100, 70), (100, 100), (100, 100)), 
                       ((100, 70), (100, 120), (100, 100), (100, 100)), 
                       ((100, 70), (100, 120), (100, 100), (100, 70), (100, 120)), 
                    ), 
                )
    
    tf = lambda image, siz: pygame.transform.scale(image, siz)
    
    @staticmethod
    def construct(word):
        word_img = pygame.Surface((200, 200))
        word_img.fill(Const.space_color)
        has_cap, has_tone = 1, False
        length = len(word)
        
        if word[0] not in PergeFont.vowel: has_cap = 0
        if word[-1] in PergeFont.tone: has_tone = True
        pos_list = PergeFont.char_pos[has_cap][length]
        size_list = PergeFont.char_size[has_cap][length]
        
        if length > 3:
            for char, pos, size in zip(word, pos_list, size_list):
                if char is word[0] and has_cap == 0:
                    char_img = char_font.render(char, True, (0, 0, 0))
                else:
                    char_img = char_font.render(char, True, (0, 0, 0))
                char_img = PergeFont.tf(char_img, size)
                word_img.blit(char_img, pos)
        else:
            for char, pos, size in zip(word, pos_list, size_list):
                if char is word[0] and has_cap == 0:
                    char_img = char_font.render(char, True, (0, 0, 0))
                else:
                    char_img = char_font.render(char, True, (0, 0, 0))
                char_img = PergeFont.tf(char_img, size)
                word_img.blit(char_img, pos)
        return word_img
    
    @staticmethod
    def wrap_up(sentense, height, width):
        if len(sentense) <= 2:
            sentense_img = pygame.Surface((width, height))
            sentense_img.blit(num_font.render(sentense, True, (0, 0, 0)), (0, 0))
        sentense = sentense.replace("1", "5")
        sentense = sentense.replace("2", "?")
        word_list = list(sentense.split())
        sentense_img = pygame.Surface((len(word_list)*width, height))
        sentense_img.fill(Const.space_color)
        for num, word in enumerate(word_list):
            sentense_img.blit(PergeFont.tf(PergeFont.construct(word), (width, height)), (width*num, 0))
        return sentense_img

def main():
    screen = pygame.display.set_mode((1051, 631))
    a = PergeFont.wrap_up("a io ai2 uai1 uaip2 t xy hue dau2 maun1", 47, 47)

    while True:
        screen.fill((255, 255, 0, 0))
        screen.blit(a, (10, 10))
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

if __name__ == "__main__":
    main()
