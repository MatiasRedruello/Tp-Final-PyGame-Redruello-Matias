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
        self.current_level = "level_one"  
        self.screen = screen 
        self.total_score = 0
        self.level_config()
       

    def level_config(self):
        
        self.delta_ms = None
        self.time= None
        self.game_time_score = 60
        self.time_left = 0
        self.letras_precionadas = None
        self.lista_de_eventos = None
        self.letras_precionadas = None
        

        self.item_porperty = File.create_property_list("info.json","r",self.current_level,"items")
        self.plataforma_porperty = File.create_property_list("info.json","r",self.current_level,"plataforma")
        self.enemy_property = File.create_property_list("info.json","r",self.current_level,"enemigo")
        self.traps_propery = File.create_property_list("info.json","r",self.current_level,"traps")

        self.item_list = []
        self.plataform_list = []
        self.enemy_list = []
        self.traps_list = []

        self.item_group = pygame.sprite.Group()
        self.plataform_group = pygame.sprite.Group()
        self.traps_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.enemy_bullets_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()

        self.portal_group = pygame.sprite.Group()
        self.player = Player(self.screen_width,self.screen_height,self.plataform_list)
        self.player.score = self.total_score
        self.portal = Portal()
        self.game_over = False
        self.defuntion_time = 0
        self.win_time = 0
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

        #Usa la misma clase que las plataformas
        for traps_list in self.traps_propery:
            trap = Plataforma(traps_list.get("rect_speed_x"),traps_list.get("rect_speed_y"),
                            traps_list.get("inicial_x"),traps_list.get("inicial_y"),traps_list.get("pixel_limit_rigth"),
                            traps_list.get("pixel_limit_left"),traps_list.get("lado"),
                            traps_list.get("plataform_path"),traps_list.get("plataform_scale"))
            self.traps_list.append(trap)


        for enemy_dict in self.enemy_property:
            enemy = Enemy(enemy_dict.get("rect_speed_x"),enemy_dict.get("rect_speed_y"),
                            enemy_dict.get("inicial_x"),enemy_dict.get("inicial_y"),enemy_dict.get("pixel_limit_rigth"),
                            enemy_dict.get("pixel_limit_left"),enemy_dict.get("pixel_limit_y"),enemy_dict.get("bullet_path"),
                            enemy_dict.get("walk_path"),
                            enemy_dict.get("row"),enemy_dict.get("colum"),enemy_dict.get("separate_files"),enemy_dict.get("lives_remaining"),
                            enemy_dict.get("lives_path"),enemy_dict.get("attack_path"),enemy_dict.get("die_path"),enemy_dict.get("sound_enemy_damege"))
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
        #Traps
        for new_traps in self.traps_list:
            self.traps_group.add(new_traps)
            new_traps.do_movement()
            new_traps.draw(self.screen)
            self.traps_group.update()

        #Enemy
        for new_enemy in self.enemy_list:
            self.enemy_group.add(new_enemy)
            self.enemy_bullets_group.add(new_enemy.bullets_group)
            new_enemy.do_movement(self.time,self.delta_ms)
            new_enemy.draw(self.screen)
            new_enemy.update()
            new_enemy.bullets_group.update()
            new_enemy.bullets_group.draw(self.screen)
            self.enemy_group.update()  
        #Portal
        self.portal.do_animation(self.delta_ms)
        self.portal.update()
        self.portal_group.add(self.portal) 
        self.portal_group.update()
        #PLayer
        self.player.do_movement(self.letras_precionadas,self.lista_de_eventos,self.time,self.delta_ms)
        self.player.bullets_group.update()
        self.player_group.add(self.player)
        self.player_group.update() 
        
              

    def draw(self):
    
        self.item_group.draw(self.screen)
        self.plataform_group.draw(self.screen)
        self.traps_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.player.bullets_group.draw(self.screen)
        self.player.draw(self.screen)
        self.player_group.draw(self.screen)
        self.portal_group.draw(self.screen)

    def collide_player_with_plataform(self):
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
    
    def collide_player_bullet_with_enemy(self):
        for bullet in self.player.bullets_group:
            collision_enemies = pygame.sprite.spritecollide(bullet, self.enemy_group, True)
            if collision_enemies:
                bullet.kill()
                for enemy_hit in collision_enemies:
                    enemy_hit.sound_damege.play()
                    enemy_hit.lives_remaining -= 1  # Reduce las vidas del enemigo
                    enemy_hit.lives.counter -= 1
                    if enemy_hit.lives_remaining == 0:
                        enemy_hit.kill()
                        enemy_hit.alive = False
                        self.total_score += 1000
                        self.player.score = self.total_score 
                        
                        # necesario par aeliminar el "fantasma de la bullet"
                        for enemy_bullet in self.enemy_bullets_group:
                            enemy_bullet.kill()


    def collide_player_bullet_with_plataform(self):
        for bullet in self.player.bullets_group:
            collision_plataform = pygame.sprite.spritecollide(bullet, self.plataform_group, True)
            if collision_plataform:
                bullet.kill()
                                    
    def collide_enemy_bullet_with_player(self):
        #probar con recorrer la lista
        for bullet in self.enemy_bullets_group:
            collision_player = pygame.sprite.spritecollide(bullet, self.player_group, True)   
            if collision_player:
                bullet.kill()
                for player_hit in collision_player:
                    self.player.sound_damege.play()
                    player_hit.lives_remaining -= 1  # Reduce las vidas del enemigo
                    player_hit.lives.counter -= 1
                    if player_hit.lives_remaining == 0:
                        player_hit.alive = False
                        self.game_over = True
                        self.defuntion_time = self.time

    def collide_player_with_enemy(self):
        for enemy in self.enemy_list:
            if enemy.alive:

                if self.player.left_rect.colliderect(enemy.right_rect):
                    # Retroceso hacia la izquierda
                    self.player.rect.x = enemy.rect.right + 100
                    self.player.sound_damege.play()  # Ajusta el valor según tu preferencia
                    self.player.lives_remaining -= 1  # Reduce las vidas del enemigo
                    self.player.lives.counter -= 1
                elif self.player.right_rect.colliderect(enemy.left_rect):
                    # Retroceso hacia la derecha
                    self.player.rect.x = enemy.rect.left - 100 
                    self.player.sound_damege.play() # Ajusta el valor según tu preferencia
                    self.player.lives_remaining -= 1  # Reduce las vidas del enemigo
                    self.player.lives.counter -= 1
                #Si me quede sin vidas termina el juego
                if self.player.lives_remaining == 0:
                    self.player.alive = False
                    self.player.kill()
                    self.game_over = True
                    self.defuntion_time = self.time
                # Verificar límites de la pantalla para el jugador
                if self.player.rect.left < 0:
                    self.player.rect.left = 0
                elif self.player.rect.right > self.screen_width:
                    self.player.rect.right = self.screen_width                        


    def collide_player_with_item(self):
        collision_items = pygame.sprite.spritecollide(self.player, self.item_group, True) 
        for item in collision_items:
            if not item.collected:  # Verificar si el ítem no ha sido recogido antes
                item.collected = True  # Marcar el ítem como recogido
                self.total_score += 500
                self.player.score = self.total_score

    def collide_player_with_portal(self):
        collision_portal = pygame.sprite.spritecollide(self.player, self.portal_group, False)
        if collision_portal:
            if not self.portal.inside_the_portal:
                self.portal.inside_the_portal = True
                time_difference =  (self.game_time_score-self.time_left) 
                end_score = (self.game_time_score - time_difference)*100
                self.total_score += end_score
                self.player.score = self.total_score
                self.win_time = self.time
                           
            
    def update(self):
        self.add_sprite_to_group()
        self.collide_player_with_plataform()
        self.collide_player_bullet_with_enemy()
        self.collide_enemy_bullet_with_player()
        self.collide_player_with_item()
        self.collide_player_with_enemy()
        self.collide_player_with_portal()
        self.collide_player_bullet_with_plataform()

