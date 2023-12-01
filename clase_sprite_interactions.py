import pygame
from clase_jugador import Player
from clase_enemigo import Enemy
from clase_archivo import File
from clase_plataforma import Plataforma
from clase_portal import Portal
from clase_items import Item


class Sprite_interactions():
    def __init__(self,screen_width,screen_height,screen) -> None:

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.delta_ms = None
        self.time= None
        self.letras_precionadas = None
        self.lista_de_eventos = None
        self.letras_precionadas = None
        self.item_porperty = File.create_property_list("info.json","r","level_one","items")
        self.plataforma_porperty = File.create_property_list("info.json","r","level_one","plataforma")
        self.enemy_property = File.create_property_list("info.json","r","level_one","enemigo")

        self.item_list = []
        self.plataform_list = []
        self.enemy_list = []

        self.item_group = pygame.sprite.Group()
        self.plataform_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.portal_group = pygame.sprite.Group()

        self.player = Player(self.screen_width,self.screen_height,self.plataform_list)
        self.portal = Portal()
        self.screen = screen
        # Create class list
        for item_dict in self.item_porperty:
            item = Item(item_dict.get("inicial_x"),item_dict.get("inicial_y"),item_dict.get("item_path"))
            self.item_list.append(item)
            
        for plataforma_dict in self.plataforma_porperty:
            plataforma = Plataforma(plataforma_dict.get("rect_speed_x"),plataforma_dict.get("rect_speed_y"),
                            plataforma_dict.get("inicial_x"),plataforma_dict.get("inicial_y"),plataforma_dict.get("pixel_limit_rigth"),
                            plataforma_dict.get("pixel_limit_left"),plataforma_dict.get("lado"),
                            plataforma_dict.get("plataform_path"),plataforma_dict.get("plataform_scale"))
            self.plataform_list.append(plataforma)
  
        for enemy_dict in self.enemy_property:
            enemy = Enemy(enemy_dict.get("rect_speed_x"),enemy_dict.get("rect_speed_y"),
                            enemy_dict.get("inicial_x"),enemy_dict.get("inicial_y"),enemy_dict.get("pixel_limit_rigth"),
                            enemy_dict.get("pixel_limit_left"),enemy_dict.get("pixel_limit_y"),enemy_dict.get("bullet_path"),
                            enemy_dict.get("walk_path"),
                            enemy_dict.get("row"),enemy_dict.get("colum"),enemy_dict.get("separate_files"))
            self.enemy_list.append(enemy)    

    def add_sprite_to_group(self):
        #Item
        for new_item in self.item_list:
            self.item_group.add(new_item)
            self.item_group.update()
        #Plataform
        for new_plataform in self.plataform_list:
            self.plataform_group.add(new_plataform)
            new_plataform.do_movement()
            new_plataform.draw(self.screen)
            self.plataform_group.update() 
        #Enemy
        for new_enemy in self.enemy_list:
            self.enemy_group.add(new_enemy.bullets_group,new_enemy)
            new_enemy.do_movement(self.time,self.delta_ms)
            self.enemy_group.update()  
        #Portal
        self.portal.do_animation(self.delta_ms)
        self.portal_group.update()
        self.portal_group.add(self.portal) 
        #PLayer
        self.player.do_movement(self.letras_precionadas,self.lista_de_eventos,self.time,self.delta_ms)
        self.player_group.update() 
        self.player_group.add(self.player,self.player.bullets_group)
              

    def draw(self):
        self.item_group.draw(self.screen)
        self.plataform_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.player.draw(self.screen)
        self.player_group.draw(self.screen)
        self.portal_group.draw(self.screen)

    def update(self):
        self.add_sprite_to_group()

        for plataforma in self.plataform_list:
            if self.player.feet_rect.colliderect(plataforma.ground_rect) :
                self.player.rect.bottom = plataforma.ground_rect.top
                self.player.rect_speed_y = 0
                self.player.jumping = False
            if self.player.head_rect.colliderect(plataforma.ground_rect):
                self.player.rect_speed_y = 0
            if self.player.left_rect.colliderect(plataforma.right_rect):
                """Si el lado izquierdo del jugador colisiona con el lado derecho de una plataforma, 
                el jugador se coloca justo al lado derecho de esa plataforma."""
                self.player.rect.left = plataforma.right_rect.right
            if self.player.right_rect.colliderect(plataforma.left_rect):
                self.player.rect.right = plataforma.left_rect.left
