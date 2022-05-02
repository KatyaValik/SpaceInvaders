screen_width = 600
screen_height = 600
background_image = 'images//background.jpg'
frame_rate = 60

player_width = 25
player_height = 25
player_image = "images//background.jpg"

invaders_offset_y = 30
invader_width = 25
invader_height = 25
invader_offset_x = 20
invader_offset_y = 5
invader_down_offset = 25
invaders_start_count = 6
invader_image = "images//background.jpg"

bullet_width = 5
bullet_height = 10
bullet_image = "images//background.jpg"
bullet_pause = 0.2
bullet_dist = 0.3

invaders_down_border = 400

space_bullet_pause = 1
space_bullet_image = "images//background.jpg"
space_bullet_width = 5
space_bullet_height = 10

shelter_width = 100
shelter_height = 5
shelter_image = "images//background.jpg"
shelter_space = 100
shelter_colours = [(0, 30, 254),
                    (3, 158, 255),
                    (0, 223, 255),
                    (255, 255, 255)]
shelter_damage_max = len(shelter_colours) - 1

initial_lives = 3

score_offset = 0
status_offset_y = 0
lives_offset = 100
levels_offset = 200
text_color = (255, 255, 255)
font_name = 'Arial'
font_size = 20

message_duration = 2

levels = ['level1', 'level2', 'level3']
levels_count = len(levels) - 1

invaders_type = ['usual', 'hardy']
