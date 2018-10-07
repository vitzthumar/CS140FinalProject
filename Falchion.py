# Test menu for final project

import intrographics
import random

w = 800
h = 800
window = intrographics.window(w, h)
background_color = (111, 40, 40)
window.fill(background_color)


# This function clears all objects on screen
def clear_screen():
    for shape in window.all():
        window.remove(shape)


# Defines the main menu with 4 different options, start, how to play, credits, and quit game
def main_menu():
    global start_button, how_to_play_button, credits_button, exit_game_button
    start_button = window.image(w / 40, h / 40, "Start Button.gif")
    how_to_play_button = window.image(w / 40, h / 40 + h / 4, "How to Play Button.gif")
    credits_button = window.image(w / 40, h / 40 + h / 2, "Credits Button.gif")
    exit_game_button = window.image(w/ 40, h / 40 + h * 3 / 4, "Exit Game Button.gif")


# Defines the click function for the main menu
def main_menu_click(x, y):

    if start_button.left < x < start_button.right and start_button.top < y < start_button.bottom:
        clear_screen()
        window.offLeftClick(main_menu_click)
        game_logic()

    if how_to_play_button.left < x < how_to_play_button.right and how_to_play_button.top < y < how_to_play_button.bottom:
        clear_screen()
        how_to_play_menu()
        window.onLeftClick(how_to_play_menu_click)
        window.offLeftClick(main_menu_click)

    if credits_button.left < x < credits_button.right and credits_button.top < y < credits_button.bottom:
        clear_screen()
        credits_menu()
        window.onLeftClick(credits_menu_click)
        window.offLeftClick(main_menu_click)

    if exit_game_button.left < x < exit_game_button.right and exit_game_button.top < y < exit_game_button.bottom:
        window.close()


# Defines the credits menu
def credits_menu():
    global back_button
    credits_menu_image = window.image(0, 0, "Credits Menu.gif")
    back_button = window.rectangle(60, 60, 360, 160)
    back_button.border(0)


def credits_menu_click(x, y):
    if back_button.left < x < back_button.right and back_button.top < y < back_button.bottom:
        clear_screen()
        main_menu()
        window.onLeftClick(main_menu_click)
        window.offLeftClick(credits_menu_click)


# Second option from main menu, details rules, controls, unit stats & abilities
def how_to_play_menu():
    global back_button, controls_button, rules_button, how_to_play_menu_image, warrior_button, rogue_button, mage_button, cleric_button
    how_to_play_menu_image = window.image(0, 0, "How to Play Menu.gif")
    back_button = window.rectangle(20, 20, 360, 160)
    back_button.border(0)
    rules_button = window.rectangle(20, 220, 760, 160)
    rules_button.border(0)
    controls_button = window.rectangle(420, 20, 360, 160)
    controls_button.border(0)
    warrior_button = window.rectangle(20, 640, 160, 120)
    warrior_button.border(0)
    rogue_button = window.rectangle(220, 640, 160, 120)
    rogue_button.border(0)
    mage_button = window.rectangle(420, 640, 160, 120)
    mage_button.border(0)
    cleric_button = window.rectangle(620, 640, 160, 120)
    cleric_button.border(0)


# Defines the click function for the how to play menu
def how_to_play_menu_click(x, y):

    if back_button.left < x < back_button.right and back_button.top < y < back_button.bottom:
        clear_screen()
        main_menu()
        window.onLeftClick(main_menu_click)
        window.offLeftClick(how_to_play_menu_click)
    if controls_button.left < x < controls_button.right and controls_button.top < y < controls_button.bottom:
        clear_screen()
        controls_menu()
        window.onLeftClick(unit_menu_click)
        window.offLeftClick(how_to_play_menu_click)
    if rules_button.left < x < rules_button.right and rules_button.top < y < rules_button.bottom:
        clear_screen()
        rules_menu()
        window.onLeftClick(unit_menu_click)
        window.offLeftClick(how_to_play_menu_click)
    if warrior_button.left < x < warrior_button.right and warrior_button.top < y < warrior_button.bottom:
        clear_screen()
        warrior_menu()
        window.onLeftClick(unit_menu_click)
        window.offLeftClick(how_to_play_menu_click)
    if rogue_button.left < x < rogue_button.right and rogue_button.top < y < rogue_button.bottom:
        clear_screen()
        rogue_menu()
        window.onLeftClick(unit_menu_click)
        window.offLeftClick(how_to_play_menu_click)
    if mage_button.left < x < mage_button.right and mage_button.top < y < mage_button.bottom:
        clear_screen()
        mage_menu()
        window.onLeftClick(unit_menu_click)
        window.offLeftClick(how_to_play_menu_click)
    if cleric_button.left < x < cleric_button.right and cleric_button.top < y < cleric_button.bottom:
        clear_screen()
        cleric_menu()
        window.onLeftClick(unit_menu_click)
        window.offLeftClick(how_to_play_menu_click)


# Defines the controls menu
def controls_menu():
    global back_button, controls_menu_image
    controls_menu_image = window.image(0, 0, "Controls Menu.gif")
    back_button = window.rectangle(20, 20, 360, 160)
    back_button.border(0)


# Defines the rules menu
def rules_menu():
    global back_button, rules_menu_image
    rules_menu_image = window.image(0, 0, "Rules Menu.gif")
    back_button = window.rectangle(20, 20, 360, 160)
    back_button.border(0)


# Defines the Warrior information menu
def warrior_menu():
    global back_button, warrior_menu_image
    warrior_menu_image = window.image(0, 0, "Warrior Menu.gif")
    back_button = window.rectangle(20, 20, 360, 160)
    back_button.border(0)


# Defines the Rogue information menu
def rogue_menu():
    global back_button, rogue_menu_image
    rogue_menu_image = window.image(0, 0, "Rogue Menu.gif")
    back_button = window.rectangle(20, 20, 360, 160)
    back_button.border(0)


# Defines the Mage information menu
def mage_menu():
    global back_button, mage_menu_image
    mage_menu_image = window.image(0, 0, "Mage Menu.gif")
    back_button = window.rectangle(20, 20, 360, 160)
    back_button.border(0)


# Defines the Cleric information menu
def cleric_menu():
    global back_button, cleric_menu_image
    cleric_menu_image = window.image(0, 0, "Cleric Menu.gif")
    back_button = window.rectangle(20, 20, 360, 160)
    back_button.border(0)


# Defines the click function for all the unit information pages
def unit_menu_click(x, y):
    if back_button.left < x < back_button.right and back_button.top < y < back_button.bottom:
        clear_screen()
        how_to_play_menu()
        window.onLeftClick(how_to_play_menu_click)
        window.offLeftClick(unit_menu_click)


# The entire game logic is defined within this function
def game_logic():
    # Variables for game window
    gap = 100
    border = 3
    # Variables for nonlocal binding
    text_count = 0
    move_count, move_max = 0, 0
    damage = 0,
    highlight_right, highlight_left, highlight_top, highlight_bottom = 0, 0, 0, 0
    message = 0
    red_dead, blue_dead = 0, 0
    red_turn, blue_turn = 0, 0
    red_turn_count, blue_turn_count = 0, 0
    # Ability variables for nonlocal binding
    mend, hasten = 0, 0
    scheme = False
    critical_strike = False
    choice = 0

    # Establishes who goes first, 1 = red, 2 = blue
    turn_order = random.randint(1, 2)
    if turn_order == 1:
        player_1 = "Red"
        player_2 = "Blue"
    if turn_order == 2:
        player_1 = "Blue"
        player_2 = "Red"

    # Setting the initial number of dead units on both teams to 0
    red_dead, blue_dead = 0, 0

    # Makes the lines and sets the grass pictures to construct the playing field. Each grid space is 100 X 100 pixels
    outer_border = window.rectangle(0, 0, w, h)
    outer_border.border(border + 2)

    for y in range(100, h, gap):
        for x in range(0, w, gap):
            grass = window.image(x, y, "grass.gif")

    for x in range(0, w + 1, gap):
        x_grid = window.line((x, 100), (x, h))
        x_grid.border(border)

    for y in range(gap, h + 1, gap):
        y_grid = window.line((0, y), (w, y))
        y_grid.border(border)

    # Sets the text box and pauses the program for the intro text
    screen_heading = window.image(0, 1, "Game Screen Heading.gif")
    pause_program = True


    # Defines the text that appears when game is first started
    def starting_text():

        if text_count == 1:
            header_text("Press the Escape key to view the help menu at any time.\nPress backspace after to remove the menu. Press Enter key.", 0)
        if text_count == 2:
            header_text("Press the space bar at any time to view each units' HP.\nPress backspace after to remove the HP. Press Enter.", 0)
        if text_count == 3:
            header_text(str(player_1) + " will move first!\nPress the Enter key to start, then click to select a friendly unit.", 0)


    # Whenever text is typed with header_text(message),
    # that message will appear in header and pause the game until Enter is pressed.
    def header_text(text, option):
        nonlocal message, pause_program
        pause_program = True

        message = window.text(20, 20, text)
        message.format("Georgia Bold", 18)

        if option == 0:
            window.onKeyPress(remove_text)
            message.group("removable_text")

        if option == 1:
            message.group("temp_text")


    # This function is directly related with header_text, removes text and unpauses the game
    def remove_text(key):
        nonlocal pause_program, text_count

        if key == "Return":
            window.remove(message)
            text_count += 1
            starting_text()


            for attack_ability in window.all("attack_ability"):
                window.remove(attack_ability)

            if text_count >= 4:
                pause_program = False


    # Removes any text grouped in group "temp_text"
    def remove_temp_text():
        for text in window.all("temp_text"):
                window.remove(text)


    # Sets the first text, other text within function starting_text will follow afterward
    header_text("Welcome to Falchion, a game of strategy.\nPress the Enter key to continue.", 0)

    # Sets the x and y coordinates for each unit
    war_r_1_x, war_r_1_y = 300, 200
    war_r_2_x, war_r_2_y = 400, 200
    war_b_1_x, war_b_1_y = 300, 600
    war_b_2_x, war_b_2_y = 400, 600
    rog_r_1_x, rog_r_1_y = 200, 100
    rog_r_2_x, rog_r_2_y = 500, 100
    rog_b_1_x, rog_b_1_y = 200, 700
    rog_b_2_x, rog_b_2_y = 500, 700
    mag_r_1_x, mag_r_1_y = 0, 200
    mag_r_2_x, mag_r_2_y = 700, 200
    mag_b_1_x, mag_b_1_y = 0, 600
    mag_b_2_x, mag_b_2_y = 700, 600
    cle_r_1_x, cle_r_1_y = 300, 100
    cle_r_2_x, cle_r_2_y = 400, 100
    cle_b_1_x, cle_b_1_y = 300, 700
    cle_b_2_x, cle_b_2_y = 400, 700

    # Defines all units on the board, and groups them in unit, team, and class. war_r_1 is an example.
    # Also defines Movement for each class, war = 2, rogue = 3, mage = 2, cleric = 3.

    # Warrior units
    war_r_1 = window.image(war_r_1_x, war_r_1_y, "Warrior_2.gif")
    war_r_2 = window.image(war_r_2_x, war_r_2_y, "Warrior_2.gif")
    war_b_1 = window.image(war_b_1_x, war_b_1_y, "Warrior_1.gif")
    war_b_2 = window.image(war_b_2_x, war_b_2_y, "Warrior_1.gif")

    # Rogue Units
    rog_r_1 = window.image(rog_r_1_x, rog_r_1_y, "Rogue_2.gif")
    rog_r_2 = window.image(rog_r_2_x, rog_r_2_y, "Rogue_2.gif")
    rog_b_1 = window.image(rog_b_1_x, rog_b_1_y, "Rogue_1.gif")
    rog_b_2 = window.image(rog_b_2_x, rog_b_2_y, "Rogue_1.gif")


    # Mage Units
    mag_r_1 = window.image(mag_r_1_x, mag_r_1_y, "Mage_2.gif")
    mag_r_2 = window.image(mag_r_2_x, mag_r_2_y, "Mage_2.gif")
    mag_b_1 = window.image(mag_b_1_x, mag_b_1_y, "Mage_1.gif")
    mag_b_2 = window.image(mag_b_2_x, mag_b_2_y, "Mage_1.gif")

    # Cleric Units
    cle_r_1 = window.image(cle_r_1_x, cle_r_1_y, "Cleric_2.gif")
    cle_r_2 = window.image(cle_r_2_x, cle_r_2_y, "Cleric_2.gif")
    cle_b_1 = window.image(cle_b_1_x, cle_b_1_y, "Cleric_1.gif")
    cle_b_2 = window.image(cle_b_2_x, cle_b_2_y, "Cleric_1.gif")

    war_list = [war_r_1, war_r_2, war_b_1, war_b_2]
    rog_list = [rog_r_1, rog_r_2, rog_b_1, rog_b_2]
    mag_list = [mag_r_1, mag_r_2, mag_b_1, mag_b_2]
    cle_list = [cle_r_1, cle_r_2, cle_b_1, cle_b_2]
    red_list = [war_r_1, war_r_2, rog_r_1, rog_r_2, mag_r_1, mag_r_2, cle_r_1, cle_r_2]
    blue_list = [war_b_1, war_b_2, rog_b_1, rog_b_2, mag_b_1, mag_b_2, cle_b_1, cle_b_2]

    # Unit grouping
    for war in war_list:
        war.group("war")
        war.group("unit")
    for rog in rog_list:
        rog.group("rog")
        rog.group("unit")
    for mag in mag_list:
        mag.group("mag")
        mag.group("unit")
    for cle in cle_list:
        cle.group("cle")
        cle.group("unit")
    for red in red_list:
        red.group("red")
    for blue in blue_list:
        blue.group("blue")

    # Sets the initial HP for all units on the board. war_r_1.hp is an example.
    def unit_hp():
        war_r_1.hp, war_r_2.hp, war_b_1.hp, war_b_2.hp = 150, 150, 150, 150
        rog_r_1.hp, rog_r_2.hp, rog_b_1.hp, rog_b_2.hp = 70, 70, 70, 70
        mag_r_1.hp, mag_r_2.hp, mag_b_1.hp, mag_b_2.hp = 100, 100, 100, 100
        cle_r_1.hp, cle_r_2.hp, cle_b_1.hp, cle_b_2.hp = 85, 85, 85, 85
    unit_hp()


    # Displays a text value and image for each unit with HP over 0 and groups it in hp_display
    # Happens when space is pressed, removes objects when backspace is pressed
    def display_health(key):

        def add_heading_and_format(x, y, hp):
            if hp > 0:
                heading = window.image(x + 2, y + 2, "HP_Box.gif")
                text = window.text(x + 12, y + 8, hp)
                text.format("Georgia Bold", 16)
                heading.group("hp_display")
                text.group("hp_display")
        # When space key is pressed, HP values are shown and move_unit function is turned off
        if key == "space":
            add_heading_and_format(war_r_1.x, war_r_1.y, war_r_1.hp)
            add_heading_and_format(war_r_2.x, war_r_2.y, war_r_2.hp)
            add_heading_and_format(war_b_1.x, war_b_1.y, war_b_1.hp)
            add_heading_and_format(war_b_2.x, war_b_2.y, war_b_2.hp)
            add_heading_and_format(rog_r_1.x, rog_r_1.y, rog_r_1.hp)
            add_heading_and_format(rog_r_2.x, rog_r_2.y, rog_r_2.hp)
            add_heading_and_format(rog_b_1.x, rog_b_1.y, rog_b_1.hp)
            add_heading_and_format(rog_b_2.x, rog_b_2.y, rog_b_2.hp)
            add_heading_and_format(mag_r_1.x, mag_r_1.y, mag_r_1.hp)
            add_heading_and_format(mag_r_2.x, mag_r_2.y, mag_r_2.hp)
            add_heading_and_format(mag_b_1.x, mag_b_1.y, mag_b_1.hp)
            add_heading_and_format(mag_b_2.x, mag_b_2.y, mag_b_2.hp)
            add_heading_and_format(cle_r_1.x, cle_r_1.y, cle_r_1.hp)
            add_heading_and_format(cle_r_2.x, cle_r_2.y, cle_r_2.hp)
            add_heading_and_format(cle_b_1.x, cle_b_1.y, cle_b_1.hp)
            add_heading_and_format(cle_b_2.x, cle_b_2.y, cle_b_2.hp)

        # When backspace key is pressed, HP values are removed and move_unit function is turned on
        if key == "BackSpace":
            for hp_display in window.all("hp_display"):
                window.remove(hp_display)


    def help_menu(key):
        if key == "Escape":
            help_menu = window.image(0, 0, "Help Menu.gif")
            help_menu.group("help_menu")
            window.onKeyPress(close_help_menu)
            window.offKeyPress(display_health)


    def close_help_menu(key):
        if key == "BackSpace":
            for menu in window.all("help_menu"):
                window.remove(menu)
            window.offKeyPress(close_help_menu)
            window.onKeyPress(display_health)
            window.onKeyPress(help_menu)


    def select_red(x, y):
        nonlocal red_turn, red_turn_count
        nonlocal move_count, move_max
        move_count = 0
        move_buff = 0

        if not pause_program:

            for unit in window.all("unit"):
                unit.ungroup("selected")

            for unit in window.all("unit"):
                if unit.left < x < unit.right and unit.top < y < unit.bottom and unit in red_list:
                    unit.group("selected")


                    # Every turn the turn count alternates from 1 to 2. This is to control abilities.
                    red_turn_count += 1
                    if red_turn_count % 2 == 0:
                        red_turn = 2
                    else:
                        red_turn = 1

                    for unit in window.all("selected"):
                        if red_turn == 2:
                            if unit in window.all("red_hasten_selected_1"):
                                unit.group("hasten_buffed")
                        if red_turn == 1:
                            if unit in window.all("red_hasten_selected_2"):
                                unit.group("hasten_buffed")

                    surround_count = 0
                    for non_unit in window.all("unit"):
                        # Checks all sides, if all 4 are full, select function resets
                        if non_unit.x + 100 == unit.x and non_unit.y == unit.y:
                            surround_count += 1
                        if non_unit.x - 100 == unit.x and non_unit.y == unit.y:
                            surround_count += 1
                        if non_unit.x == unit.x and non_unit.y == unit.y + 100:
                            surround_count += 1
                        if non_unit.x == unit.x and non_unit.y == unit.y - 100:
                            surround_count += 1
                    if unit.x == 0 or unit.x == 700:
                        surround_count += 1
                    if unit.y == 100 or unit.y == 700:
                        surround_count += 1

                    # If the unit can move, the rest of the function will carry out.
                    if surround_count != 4:


                        for unit in window.all("selected"):
                            selected_unit_highlight = window.rectangle(unit.x + 3, unit.y + 3, 94, 94)
                            selected_unit_highlight.border(3, (87, 7, 7))
                            selected_unit_highlight.group("selected_unit_highlight")

                        window.offLeftClick(select_red)


                        for unit in window.all("selected"):
                            if unit in window.all("hasten_buffed"):
                                move_buff = 1

                        if unit in war_list:
                            move_max = 2
                            if move_buff == 1:
                                hasten_buff()
                            header_text("Warrior selected. Movement: " + str(move_max) + " tiles. Attack: 30-40.\nPress Enter to continue, then move with the arrow keys.", 0)
                        if unit in rog_list:
                            move_max = 3
                            if move_buff == 1:
                                hasten_buff()
                            header_text("Rogue selected. Movement: " + str(move_max) + " tiles. Attack: 45-55 (30% +10).\nPress Enter to continue, then move with the arrow keys.", 0)
                        if unit in mag_list:
                            move_max = 2
                            if move_buff == 1:
                                hasten_buff()
                            header_text("Mage selected. Movement: " + str(move_max) + " tiles. Attack: 35-45.\nPress Enter to continue, then move with the arrow keys.", 0)
                        if unit in cle_list:
                            move_max = 3
                            if move_buff == 1:
                                hasten_buff()
                            header_text("Cleric selected. Movement: " + str(move_max) + " tiles. Attack: 15-20.\nPress Enter to continue, then move with the arrow keys", 0)

                        if red_turn == 1:
                            for unit in window.all("red_hasten_selected_1"):
                                unit.ungroup("red_hasten_selected_1")
                                unit.ungroup("hasten_buffed")

                        if red_turn == 2:
                            for unit in window.all("red_hasten_selected_2"):
                                unit.ungroup("red_hasten_selected_2")
                                unit.ungroup("hasten_buffed")

                        window.onKeyPress(move_unit)

                    # If the unit cannot move, the lower message will be displayed, and the click function restarted
                    else:
                        header_text("This unit has no available movement options.\nPress Enter, then select a movable Red unit.", 0)
                        window.offLeftClick(select_red)
                        window.onLeftClick(select_red)


    def select_blue(x, y):
        nonlocal blue_turn, blue_turn_count
        nonlocal move_count, move_max
        move_count = 0
        move_buff = 0

        if not pause_program:

            for unit in window.all("unit"):
                unit.ungroup("selected")

            for unit in window.all("unit"):
                if unit.left < x < unit.right and unit.top < y < unit.bottom and unit in blue_list:
                    unit.group("selected")

                    # Every turn the turn count alternates from 1 to 2. This is to control abilities.
                    blue_turn_count += 1
                    if blue_turn_count % 2 == 0:
                        blue_turn = 2
                    else:
                        blue_turn = 1

                    for unit in window.all("selected"):
                        if blue_turn == 2:
                            if unit in window.all("blue_hasten_selected_1"):
                                unit.group("hasten_buffed")
                        if blue_turn == 1:
                            if unit in window.all("blue_hasten_selected_2"):
                                unit.group("hasten_buffed")

                    surround_count = 0
                    for non_unit in window.all("unit"):
                        # Checks all sides, if all 4 are full, select function resets
                        if non_unit.x + 100 == unit.x and non_unit.y == unit.y:
                            surround_count += 1
                        if non_unit.x - 100 == unit.x and non_unit.y == unit.y:
                            surround_count += 1
                        if non_unit.x == unit.x and non_unit.y == unit.y + 100:
                            surround_count += 1
                        if non_unit.x == unit.x and non_unit.y == unit.y - 100:
                            surround_count += 1
                    if unit.x == 0 or unit.x == 700:
                        surround_count += 1
                    if unit.y == 100 or unit.y == 700:
                        surround_count += 1

                    # If the unit can move, the rest of the function will carry out.
                    if surround_count != 4:

                        for unit in window.all("selected"):
                            selected_unit_highlight = window.rectangle(unit.x + 3, unit.y + 3, 94, 94)
                            selected_unit_highlight.border(3, (11, 30, 83))
                            selected_unit_highlight.group("selected_unit_highlight")

                        window.offLeftClick(select_blue)

                        for unit in window.all("selected"):
                            if unit in window.all("hasten_buffed"):
                                move_buff = 1

                        if unit in war_list:
                            move_max = 2
                            if move_buff == 1:
                                hasten_buff()
                            header_text("Warrior selected. Movement: " + str(move_max) + " tiles. Attack: 30-40.\nPress Enter to continue, then move with the arrow keys.", 0)
                        if unit in rog_list:
                            move_max = 3
                            if move_buff == 1:
                                hasten_buff()
                            header_text("Rogue selected. Movement: " + str(move_max) + " tiles. Attack: 45-55 (30% +10).\nPress Enter to continue, then move with the arrow keys.", 0)
                        if unit in mag_list:
                            move_max = 2
                            if move_buff == 1:
                                hasten_buff()
                            header_text("Mage selected. Movement: " + str(move_max) + " tiles. Attack: 35-45.\nPress Enter to continue, then move with the arrow keys.", 0)
                        if unit in cle_list:
                            move_max = 3
                            if move_buff == 1:
                                hasten_buff()
                            header_text("Cleric selected. Movement: " + str(move_max) + " tiles. Attack: 15-20.\nPress Enter to continue, then move with the arrow keys", 0)


                        if blue_turn == 1:
                            for unit in window.all("blue_hasten_selected_1"):
                                unit.ungroup("blue_hasten_selected_1")
                                unit.ungroup("hasten_buffed")

                        if blue_turn == 2:
                            for unit in window.all("blue_hasten_selected_2"):
                                unit.ungroup("blue_hasten_selected_2")
                                unit.ungroup("hasten_buffed")

                        window.onKeyPress(move_unit)

                    # If the unit cannot move, the lower message will be displayed, and the click function restarted
                    else:
                        header_text("This unit has no available movement options.\nPress Enter, then select a movable Blue unit.", 0)
                        window.offLeftClick(select_blue)
                        window.onLeftClick(select_blue)


    # Keystroke function that moves the selected unit by 100 pixels. Turned off when the HP display is on
    def move_unit(key):
        nonlocal move_count

        if not pause_program:

            for unit in window.all("selected"):
                count = 0
                if key == "Right":
                    if unit.x < 700:
                        for object in window.all("unit"):
                            if object.x == unit.x + 100 and object.y == unit.y:
                                count += 1
                        if count == 0:

                            for icon in window.all("with_icon"):
                                if unit.x + 69 == icon.x and unit.y + 2 == icon.y:
                                    icon.move(100, 0)

                            unit.move(100, 0)
                            for selected_unit_highlight in window.all("selected_unit_highlight"):
                                selected_unit_highlight.move(100, 0)
                            move_count += 1

                if key == "Left":
                    if unit.x > 0:
                        for object in window.all("unit"):
                            if object.x == unit.x - 100 and object.y == unit.y:
                                count += 1
                        if count == 0:

                            for icon in window.all("with_icon"):
                                if unit.x + 69 == icon.x and unit.y + 2 == icon.y:
                                    icon.move(-100, 0)

                            unit.move(-100, 0)
                            for selected_unit_highlight in window.all("selected_unit_highlight"):
                                selected_unit_highlight.move(-100, 0)
                            move_count += 1

                if key == "Up":
                    if unit.y > 100:
                        for object in window.all("unit"):
                            if object.y == unit.y - 100 and object.x == unit.x:
                                count += 1
                        if count == 0:

                            for icon in window.all("with_icon"):
                                if unit.x + 69 == icon.x and unit.y + 2 == icon.y:
                                    icon.move(0, -100)

                            unit.move(0, -100)
                            for selected_unit_highlight in window.all("selected_unit_highlight"):
                                selected_unit_highlight.move(0, -100)
                            move_count += 1

                if key == "Down":
                    if unit.y < 700:
                        for object in window.all("unit"):
                            if object.y == unit.y + 100 and object.x == unit.x:
                                count += 1
                        if count == 0:

                            for icon in window.all("with_icon"):
                                if unit.x + 69 == icon.x and unit.y + 2 == icon.y:
                                    icon.move(0, 100)

                            unit.move(0, 100)
                            for selected_unit_highlight in window.all("selected_unit_highlight"):
                                selected_unit_highlight.move(0, 100)
                            move_count += 1

                if move_count == move_max:
                    window.offKeyPress(move_unit)
                    attack_unit()


    # Determines which class the unit is in, and prompts to attack or pass turn by pressing "a" or "w".
    def attack_unit():
        nonlocal damage, critical_strike, scheme
        damage = 0
        critical_strike = False
        scheme = False
        for unit in window.all("selected"):

            if unit in war_list:
                header_text("To attack, press A. Your attack will hit every adjacent unit.\nTo use Bolster, press D. To pass your turn, press W.", 1)
                window.offKeyPress(remove_text)
                illuminate()
                window.onKeyPress(war_attack)

            if unit in rog_list:
                header_text("To attack, press A. To use Scheme, press D.\nTo pass your turn, press W.", 1)
                window.offKeyPress(remove_text)
                illuminate()
                window.onKeyPress(rog_attack)

            if unit in mag_list:
                header_text("To attack, press A. To use Hasten, press D.\nTo pass your turn, press W.", 1)
                window.offKeyPress(remove_text)
                illuminate()
                window.onKeyPress(mag_attack)

            if unit in cle_list:
                header_text("To attack, press A. To use Mend, press D.\nTo pass your turn, press W.", 1)
                window.offKeyPress(remove_text)
                illuminate()
                window.onKeyPress(cle_attack)


    # Highlights the attack range grid spaces for a selected unit. 2 spaces in the case of mage
    # Groups the highlighted grid spaces in group "highlight", can be used to overlap and deal damage to units
    def illuminate():
        nonlocal highlight_bottom, highlight_top, highlight_left, highlight_right

        for unit in window.all("selected"):
            if unit in window.all("mag"):
                highlight_right = window.rectangle(unit.x + 203, unit.y + 3, 94, 94)
                highlight_left = window.rectangle(unit.x - 197, unit. y + 3, 94, 94)
                highlight_bottom = window.rectangle(unit.x + 3, unit.y + 203, 94, 94)
                if unit.y != 200:
                    highlight_top = window.rectangle(unit.x + 3, unit.y - 197, 94, 94)
                    highlight_top.group("highlight")
                    highlight_top.border(3, "yellow")
                else:
                    highlight_top = window.rectangle(800, 800, 100, 100)

            else:
                highlight_right = window.rectangle(unit.x + 103, unit.y + 3, 94, 94)
                highlight_left = window.rectangle(unit.x - 97, unit.y + 3, 94, 94)
                highlight_bottom = window.rectangle(unit.x + 3, unit.y + 103, 94, 94)
                if unit.y != 100:
                    highlight_top = window.rectangle(unit.x + 3, unit.y - 97, 94, 94)
                    highlight_top.group("highlight")
                    highlight_top.border(3, "yellow")
                else:
                    highlight_top = window.rectangle(800, 800, 100, 100)

            highlight_right.group("highlight")
            highlight_right.border(3, "yellow")
            highlight_left.group("highlight")
            highlight_left.border(3, "yellow")
            highlight_bottom.group("highlight")
            highlight_bottom.border(3, "yellow")


    # Removes highlighted grid spaces
    def deluminate():
        for highlight in window.all("highlight"):
            window.remove(highlight)
            highlight.ungroup("highlight")
        for selected_unit_highlight in window.all("selected_unit_highlight"):
            window.remove(selected_unit_highlight)
            selected_unit_highlight.ungroup("selected_unit_highlight")


    def war_attack(key):
        nonlocal choice, damage
        if key == "a":
            choice = 1
            halve_damage = False
            remove_temp_text()

            for grid in window.all("highlight"):
                for hit_unit in window.all("unit"):
                    if hit_unit.overlaps(grid):

                        for bolster_icon in window.all("bolster_buffed"):
                            if hit_unit.x + 69 == bolster_icon.x and hit_unit.y + 2 == bolster_icon.y:
                                halve_damage = True

                        if halve_damage:
                            damage = int((random.randint(30, 40)) / 2)
                            hit_unit.hp -= damage
                        else:
                            damage = random.randint(30, 40)
                            hit_unit.hp -= damage

                        remove_unit()
            attack_ability()
            deluminate()
            window.offKeyPress(war_attack)
            end_turn()
            game_over()

        if key == "w":
            choice = 2
            remove_temp_text()
            window.offKeyPress(war_attack)

            deluminate()
            end_turn()

        if key == "d":
            choice = 3
            remove_temp_text()
            for unit in window.all("selected"):
                if unit in red_list:
                    unit_color = 1
                if unit in blue_list:
                    unit_color = 2
            for grid in window.all("highlight"):
                for hit_unit in window.all("unit"):
                    if hit_unit.overlaps(grid):
                        if hit_unit in red_list:
                            if unit_color == 1:
                                if red_turn == 1:
                                    hit_unit.group("red_bolster_1")
                                if red_turn == 2:
                                    hit_unit.group("red_bolster_2")

                        if hit_unit in blue_list:
                            if unit_color == 2:
                                if blue_turn == 1:
                                    hit_unit.group("blue_bolster_1")
                                if blue_turn == 2:
                                    hit_unit.group("blue_bolster_2")

            window.offKeyPress(war_attack)
            ability_bolster()
            deluminate()
            end_turn()


    def ability_bolster():

        for hit_unit in window.all("red_bolster_1"):

            bolster = window.image(hit_unit.x + 1, hit_unit.y, "Bolster.gif")
            bolster.group("attack_ability")
            bolster_icon = window.image(hit_unit.x + 69, hit_unit.y + 2, "Bolster Icon.gif")
            bolster_icon.group("red_bolster_1_icon")
            bolster_icon.group("with_icon")
            bolster_icon.group("bolster_buffed")

        for hit_unit in window.all("red_bolster_2"):

            bolster = window.image(hit_unit.x + 1, hit_unit.y, "Bolster.gif")
            bolster.group("attack_ability")
            bolster_icon = window.image(hit_unit.x + 69, hit_unit.y + 2, "Bolster Icon.gif")
            bolster_icon.group("red_bolster_2_icon")
            bolster_icon.group("with_icon")
            bolster_icon.group("bolster_buffed")

        for hit_unit in window.all("blue_bolster_1"):

            bolster = window.image(hit_unit.x + 1, hit_unit.y, "Bolster.gif")
            bolster.group("attack_ability")
            bolster_icon = window.image(hit_unit.x + 69, hit_unit.y + 2, "Bolster Icon.gif")
            bolster_icon.group("blue_bolster_1_icon")
            bolster_icon.group("with_icon")
            bolster_icon.group("bolster_buffed")

        for hit_unit in window.all("blue_bolster_2"):

            bolster = window.image(hit_unit.x + 1, hit_unit.y, "Bolster.gif")
            bolster.group("attack_ability")
            bolster_icon = window.image(hit_unit.x + 69, hit_unit.y + 2, "Bolster Icon.gif")
            bolster_icon.group("blue_bolster_2_icon")
            bolster_icon.group("with_icon")
            bolster_icon.group("bolster_buffed")


    def remove_bolster():

        for unit in window.all("selected"):
            if unit in red_list:
                if red_turn == 1:
                    for icon in window.all("red_bolster_2_icon"):
                        window.remove(icon)
                        icon.ungroup("red_bolster_2_icon")

                if red_turn == 2:
                    for icon in window.all("red_bolster_1_icon"):
                        window.remove(icon)
                        icon.ungroup("red_bolster_1_icon")

            if unit in blue_list:
                if blue_turn == 1:
                    for icon in window.all("blue_bolster_2_icon"):
                        window.remove(icon)
                        icon.ungroup("blue_bolster_2_icon")

                if blue_turn == 2:
                    for icon in window.all("blue_bolster_1_icon"):
                        window.remove(icon)
                        icon.ungroup("blue_bolster_1_icon")


        for unit in window.all("red_bolster_1"):
          unit.ungroup("red_bolster_1")
        for unit in window.all("red_bolster_2"):
            unit.ungroup("red_bolster_2")
        for unit in window.all("blue_bolster_1"):
            unit.ungroup("blue_bolster_1")
        for unit in window.all("blue_bolster_2"):
            unit.ungroup("blue_bolster_2")


    def rog_attack(key):
        nonlocal choice, scheme, critical_strike
        if key == "a":

            choice = 1
            remove_temp_text()

            window.onKeyPress(attack_direction)
            header_text("Select a direction to attack.\nUse the arrow keys to choose a tile.", 1)

            for unit in window.all("selected"):
                for scheme_icon in window.all("red_scheme_1_icon"):
                    if unit.overlaps(scheme_icon):
                        scheme = True
            for unit in window.all("selected"):
                for scheme_icon in window.all("red_scheme_2_icon"):
                    if unit.overlaps(scheme_icon):
                        scheme = True
            for unit in window.all("selected"):
                for scheme_icon in window.all("blue_scheme_1_icon"):
                    if unit.overlaps(scheme_icon):
                        scheme = True
            for unit in window.all("selected"):
                for scheme_icon in window.all("blue_scheme_2_icon"):
                    if unit.overlaps(scheme_icon):
                        scheme = True

            if not scheme:
                crit = random.randint(1, 100)
                if crit <= 30:
                    critical_strike = True
                else:
                    critical_strike = False

            window.offKeyPress(rog_attack)

        if key == "w":
            choice = 2
            remove_temp_text()
            window.offKeyPress(rog_attack)
            deluminate()
            end_turn()


        if key == "d":
            choice = 3
            remove_temp_text()
            for unit in window.all("selected"):

                if unit in red_list:
                        if red_turn == 1:
                            unit.group("red_scheme_1")
                        if red_turn == 2:
                            unit.group("red_scheme_2")

                if unit in blue_list:

                        if blue_turn == 1:
                            unit.group("blue_scheme_1")
                        if blue_turn == 2:
                            unit.group("blue_scheme_2")
            ability_scheme()
            window.offKeyPress(rog_attack)
            deluminate()
            end_turn()


    def ability_scheme():

        for unit in window.all("red_scheme_1"):
            scheme = window.image(unit.x + 1, unit.y, "Scheme.gif")
            scheme.group("attack_ability")
            scheme_icon = window.image(unit.x + 69, unit.y + 2, "Scheme Icon.gif")
            scheme_icon.group("red_scheme_1_icon")
            scheme_icon.group("with_icon")

        for unit in window.all("red_scheme_2"):
            scheme = window.image(unit.x + 1, unit.y, "Scheme.gif")
            scheme.group("attack_ability")
            scheme_icon = window.image(unit.x + 69, unit.y + 2, "Scheme Icon.gif")
            scheme_icon.group("red_scheme_2_icon")
            scheme_icon.group("with_icon")

        for unit in window.all("blue_scheme_1"):
            scheme = window.image(unit.x + 1, unit.y, "Scheme.gif")
            scheme.group("attack_ability")
            scheme_icon = window.image(unit.x + 69, unit.y + 2, "Scheme Icon.gif")
            scheme_icon.group("blue_scheme_1_icon")
            scheme_icon.group("with_icon")

        for unit in window.all("blue_scheme_2"):
            scheme = window.image(unit.x + 1, unit.y, "Scheme.gif")
            scheme.group("attack_ability")
            scheme_icon = window.image(unit.x + 69, unit.y + 2, "Scheme Icon.gif")
            scheme_icon.group("blue_scheme_2_icon")
            scheme_icon.group("with_icon")


    def remove_scheme():

        for unit in window.all("selected"):
            if unit in red_list:
                if red_turn == 1:
                    for icon in window.all("red_scheme_2_icon"):
                        window.remove(icon)
                        icon.ungroup("red_scheme_2_icon")

                if red_turn == 2:
                    for icon in window.all("red_scheme_1_icon"):
                        window.remove(icon)
                        icon.ungroup("red_scheme_1_icon")

            if unit in blue_list:
                if blue_turn == 1:
                    for icon in window.all("blue_scheme_2_icon"):
                        window.remove(icon)
                        icon.ungroup("blue_scheme_2_icon")

                if blue_turn == 2:
                    for icon in window.all("blue_scheme_1_icon"):
                        window.remove(icon)
                        icon.ungroup("blue_scheme_1_icon")

        for unit in window.all("red_scheme_1"):
          unit.ungroup("red_scheme_1")
        for unit in window.all("red_scheme_2"):
            unit.ungroup("red_scheme_2")
        for unit in window.all("blue_scheme_1"):
            unit.ungroup("blue_scheme_1")
        for unit in window.all("blue_scheme_2"):
            unit.ungroup("blue_scheme_2")


    def rog_attack_2():
        nonlocal damage
        halve_damage = False

        for grid in window.all("highlight_target"):
            for hit_unit in window.all("unit"):
                if hit_unit.overlaps(grid):


                    for bolster_icon in window.all("bolster_buffed"):
                        if hit_unit.x + 69 == bolster_icon.x and hit_unit.y + 2 == bolster_icon.y:
                            halve_damage = True

                    if halve_damage:
                        if scheme:
                            damage = int((random.randint(45, 55) + 15) / 2)
                            hit_unit.hp -= damage
                        else:
                            if critical_strike:
                                damage = int((random.randint(45, 55) + 10) / 2)
                                hit_unit.hp -= damage
                            else:
                                damage = int(random.randint(45, 55) / 2)
                                hit_unit.hp -= damage

                    else:
                        if scheme:
                            damage = random.randint(45, 55) + 15
                            hit_unit.hp -= damage
                        else:
                            if critical_strike:
                                damage = int(random.randint(45, 55) + 10)
                                hit_unit.hp -= damage
                            else:
                                damage = int(random.randint(45, 55))
                                hit_unit.hp -= damage

                    remove_unit()
        deluminate()
        window.offKeyPress(rog_attack)
        end_turn()
        game_over()


    def mag_attack(key):
        nonlocal choice, hasten
        if key == "a":
            choice = 1
            remove_temp_text()

            window.onKeyPress(attack_direction)
            header_text("Select a direction to attack.\nUse the arrow keys to choose a tile.", 1)
            window.offKeyPress(mag_attack)

        if key == "w":
            choice = 2
            remove_temp_text()
            window.offKeyPress(mag_attack)
            deluminate()
            end_turn()

        if key == "d":
            choice = 3
            remove_temp_text()
            for unit in window.all("selected"):
                if unit in red_list:
                    unit_color = 1
                if unit in blue_list:
                    unit_color = 2
            for grid in window.all("highlight"):
                for hit_unit in window.all("unit"):
                    if hit_unit.overlaps(grid):
                        if hit_unit in red_list:
                            if unit_color == 1:
                                if red_turn == 1:
                                    hit_unit.group("red_hasten_1")
                                if red_turn == 2:
                                    hit_unit.group("red_hasten_2")

                        if hit_unit in blue_list:
                            if unit_color == 2:
                                if blue_turn == 1:
                                    hit_unit.group("blue_hasten_1")
                                if blue_turn == 2:
                                    hit_unit.group("blue_hasten_2")

            window.offKeyPress(mag_attack)
            ability_hasten()
            deluminate()
            end_turn()


    def mag_attack_2():
        nonlocal damage
        halve_damage = False
        for grid in window.all("highlight_target"):
            for hit_unit in window.all("unit"):
                if hit_unit.overlaps(grid):

                    for bolster_icon in window.all("bolster_buffed"):
                        if hit_unit.x + 69 == bolster_icon.x and hit_unit.y + 2 == bolster_icon.y:
                            halve_damage = True

                    if halve_damage:
                        damage = int((random.randint(35, 45)) / 2)
                        hit_unit.hp -= damage
                    else:
                        damage = random.randint(35, 45)
                        hit_unit.hp -= damage
                    remove_unit()
        deluminate()

        window.offKeyPress(mag_attack)
        end_turn()
        game_over()


    def ability_hasten():
        for hit_unit in window.all("red_hasten_1"):
            hit_unit.group("red_hasten_selected_1")
            hasten = window.image(hit_unit.x + 1, hit_unit.y, "Hasten.gif")
            hasten.group("attack_ability")
            hasten_icon = window.image(hit_unit.x + 69, hit_unit.y + 2, "Hasten Icon.gif")
            hasten_icon.group("red_hasten_1_icon")
            hasten_icon.group("with_icon")

        for hit_unit in window.all("red_hasten_2"):
            hit_unit.group("red_hasten_selected_2")
            hasten = window.image(hit_unit.x + 1, hit_unit.y, "Hasten.gif")
            hasten.group("attack_ability")
            hasten_icon = window.image(hit_unit.x + 69, hit_unit.y + 2, "Hasten Icon.gif")
            hasten_icon.group("red_hasten_2_icon")
            hasten_icon.group("with_icon")

        for hit_unit in window.all("blue_hasten_1"):
            hit_unit.group("blue_hasten_selected_1")
            hasten = window.image(hit_unit.x + 1, hit_unit.y, "Hasten.gif")
            hasten.group("attack_ability")
            hasten_icon = window.image(hit_unit.x + 69, hit_unit.y + 2, "Hasten Icon.gif")
            hasten_icon.group("blue_hasten_1_icon")
            hasten_icon.group("with_icon")

        for hit_unit in window.all("blue_hasten_2"):
            hit_unit.group("blue_hasten_selected_2")
            hasten = window.image(hit_unit.x + 1, hit_unit.y, "Hasten.gif")
            hasten.group("attack_ability")
            hasten_icon = window.image(hit_unit.x + 69, hit_unit.y + 2, "Hasten Icon.gif")
            hasten_icon.group("blue_hasten_2_icon")
            hasten_icon.group("with_icon")


    def remove_hasten():


        for unit in window.all("selected"):
            if unit in red_list:
                if red_turn == 1:
                    for icon in window.all("red_hasten_2_icon"):
                        window.remove(icon)
                        icon.ungroup("red_hasten_2_icon")

                if red_turn == 2:
                    for icon in window.all("red_hasten_1_icon"):
                        window.remove(icon)
                        icon.ungroup("red_hasten_1_icon")

            if unit in blue_list:
                if blue_turn == 1:
                    for icon in window.all("blue_hasten_2_icon"):
                        window.remove(icon)
                        icon.ungroup("blue_hasten_2_icon")

                if blue_turn == 2:
                    for icon in window.all("blue_hasten_1_icon"):
                        window.remove(icon)
                        icon.ungroup("blue_hasten_1_icon")


        for unit in window.all("red_hasten_1"):
          unit.ungroup("red_hasten_1")
        for unit in window.all("red_hasten_2"):
            unit.ungroup("red_hasten_2")
        for unit in window.all("blue_hasten_1"):
            unit.ungroup("blue_hasten_1")
        for unit in window.all("blue_hasten_2"):
            unit.ungroup("blue_hasten_2")


    def hasten_buff():
        nonlocal move_max

        for unit in window.all("selected"):
            if unit in window.all("hasten_buffed"):
                move_max += 1


    def cle_attack(key):
        nonlocal choice, mend
        if key == "a":
            choice = 1
            remove_temp_text()
            window.onKeyPress(attack_direction)
            header_text("Select a direction to attack.\nUse the arrow keys to choose a tile.", 1)
            window.offKeyPress(cle_attack)

        if key == "w":
            choice = 2
            remove_temp_text()
            window.offKeyPress(cle_attack)
            deluminate()
            end_turn()

        if key == "d":
            choice = 3
            remove_temp_text()
            window.onKeyPress(attack_direction)
            header_text("Select a direction in which to use Mend.\nUse the arrow keys to choose a tile.", 1)
            mend = True
            window.offKeyPress(cle_attack)


    def cle_attack_2():
        nonlocal damage
        halve_damage = False
        for grid in window.all("highlight_target"):
            for hit_unit in window.all("unit"):
                if hit_unit.overlaps(grid):
                    if not mend:
                        for bolster_icon in window.all("bolster_buffed"):
                            if hit_unit.x + 69 == bolster_icon.x and hit_unit.y + 2 == bolster_icon.y:
                                halve_damage = True

                        if halve_damage:
                            damage = int((random.randint(15, 20)) / 2)
                            hit_unit.hp -= damage
                        else:
                            damage = random.randint(15, 20)
                            hit_unit.hp -= damage

                    if mend:
                        hit_unit.hp += 30
                        if hit_unit in war_list:
                            if hit_unit.hp > 150:
                                hit_unit.hp = 150
                        if hit_unit in rog_list:
                            if hit_unit.hp > 70:
                                hit_unit.hp = 70
                        if hit_unit in mag_list:
                            if hit_unit.hp > 100:
                                hit_unit.hp = 100
                        if hit_unit in cle_list:
                            if hit_unit.hp > 85:
                                hit_unit.hp = 85

                    remove_unit()
        deluminate()

        window.offKeyPress(cle_attack)
        end_turn()
        game_over()

        # Like the red x, will fill the space a unit attacks with the Attack Swords.gif image for 3 seconds.


    def attack_ability():
        for grid in window.all("highlight_target"):

            if mend:
                attack_ability = window.image(grid.x - 2, grid.y - 3, "Mend.gif")
                attack_ability.group("attack_ability")

            else:
                attack_ability = window.image(grid.x - 2, grid.y - 2, "Attack Swords.gif")
                attack_ability.group("attack_ability")

        for unit in window.all("selected"):
            if unit in war_list:
                for grid in window.all("highlight"):
                    attack_ability = window.image(grid.x - 2, grid.y - 2, "Attack Swords.gif")
                    attack_ability.group("attack_ability")


    def attack_direction(key):

        for highlight in window.all("highlight"):

            if key == "Right":
                highlight_right.group("highlight_target")
                attack_ability()
                remove_temp_text()
                for unit in window.all("selected"):
                    if unit in rog_list:
                        rog_attack_2()
                    if unit in mag_list:
                        mag_attack_2()
                    if unit in cle_list:
                        cle_attack_2()
                window.offKeyPress(attack_direction)

            if key == "Left":
                highlight_left.group("highlight_target")
                attack_ability()
                remove_temp_text()
                for unit in window.all("selected"):
                    if unit in rog_list:
                        rog_attack_2()
                    if unit in mag_list:
                        mag_attack_2()
                    if unit in cle_list:
                        cle_attack_2()
                window.offKeyPress(attack_direction)

            if key == "Down":
                highlight_bottom.group("highlight_target")
                attack_ability()
                remove_temp_text()
                for unit in window.all("selected"):
                    if unit in rog_list:
                        rog_attack_2()
                    if unit in mag_list:
                        mag_attack_2()
                    if unit in cle_list:
                        cle_attack_2()
                window.offKeyPress(attack_direction)

            if key == "Up":
                highlight_top.group("highlight_target")
                attack_ability()
                remove_temp_text()
                for unit in window.all("selected"):
                    if unit in rog_list:
                        rog_attack_2()
                    if unit in mag_list:
                        mag_attack_2()
                    if unit in cle_list:
                        cle_attack_2()
                window.offKeyPress(attack_direction)


    # Function that removes the unit after an event happens.
    # Also displays a red x, every 0-health unit and x is cleared after 3 seconds
    def remove_unit():
        nonlocal red_dead, blue_dead
        for unit in window.all("unit"):
            if unit.hp <= 0:
                if unit in red_list:
                    red_dead += 1
                if unit in blue_list:
                    blue_dead += 1
                for icon in window.all("with_icon"):
                    if unit.x + 69 == icon and unit.y + 2 == icon:
                        window.remove(icon)

                red_x = window.image(unit.x, unit.y, "Red_X.gif")
                red_x.group("red_x")
                window.remove(unit)

                def remove_unit_timer():
                    for red_x in window.all("red_x"):

                        window.remove(red_x)
                    window.offTimer(remove_unit_timer)

                window.onTimer(3000, remove_unit_timer)


    # Displays text and ends the turn of either Red or Blue, prompting them to switch.
    def end_turn():
        nonlocal choice, mend
        mend = False

        for unit in window.all("selected"):
            if unit in window.all("hasten_buffed"):
                unit.ungroup("hasten_buffed")

        remove_hasten()
        remove_bolster()
        remove_scheme()

        for unit in window.all("selected"):
            if choice == 1:
                if unit in red_list:
                    if critical_strike:
                        header_text("Critical strike! " + str(damage) + " Damage dealt! It is now Blue's turn.\nPress Enter, then click to select a Blue unit.", 1)
                    else:
                        if not scheme:
                            header_text(str(damage) + " Damage dealt! It is now Blue's turn.\nPress Enter, then click to select a Blue unit.", 1)
                        else:
                            header_text("Schemed strike! " + str(damage) + " Damage dealt! It is now Blue's turn.\nPress Enter, then click to select a Blue unit.", 1)
                    stalemate(blue)
                    window.onKeyPress(remove_text)
                    window.onLeftClick(select_blue)

                if unit in blue_list:
                    if critical_strike:
                        header_text("Critical strike! " + str(damage) + " Damage dealt! It is now Red's turn.\nPress Enter, then click to select a Red unit.", 1)
                    else:
                        if not scheme:
                            header_text(str(damage) + " Damage dealt! It is now Red's turn.\nPress Enter, then click to select a Red unit.", 1)
                        else:
                            header_text("Schemed strike! " + str(damage) + " Damage dealt! It is now Red's turn.\nPress Enter, then click to select a Red unit.", 1)
                    stalemate(red)
                    window.onKeyPress(remove_text)
                    window.onLeftClick(select_red)

            if choice == 2:
                if unit in red_list:
                    header_text("Turn passed. It is now Blue's turn.\nPress Enter, then click to select a Blue unit.", 1)
                    stalemate(blue)
                    window.onKeyPress(remove_text)
                    window.onLeftClick(select_blue)

                if unit in blue_list:
                    header_text("Turn passed. It is now Red's turn.\nPress Enter, then click to select a Red unit.", 1)
                    stalemate(red)
                    window.onKeyPress(remove_text)
                    window.onLeftClick(select_red)

            if choice == 3:
                if unit in war_list:
                    if unit in red_list:
                        header_text("Bolster used! It is now Blue's turn.\nPress Enter, then click to select a Blue unit.", 1)
                        stalemate(blue)
                        window.onKeyPress(remove_text)
                        window.onLeftClick(select_blue)

                    if unit in blue_list:
                        header_text("Bolster used! It is now Red's turn.\nPress Enter, then click to select a Red unit.", 1)
                        stalemate(red)
                        window.onKeyPress(remove_text)
                        window.onLeftClick(select_red)

                if unit in rog_list:
                    if unit in red_list:
                        header_text("Scheme used! It is now Blue's turn.\nPress Enter, then click to select a Blue unit.", 1)
                        stalemate(blue)
                        window.onKeyPress(remove_text)
                        window.onLeftClick(select_blue)

                    if unit in blue_list:
                        header_text("Scheme used! It is now Red's turn.\nPress Enter, then click to select a Red unit.", 1)
                        stalemate(red)
                        window.onKeyPress(remove_text)
                        window.onLeftClick(select_red)

                if unit in mag_list:
                    if unit in red_list:
                        header_text("Hasten used! It is now Blue's turn.\nPress Enter, then click to select a Blue unit.", 1)
                        stalemate(blue)
                        window.onKeyPress(remove_text)
                        window.onLeftClick(select_blue)

                    if unit in blue_list:
                        header_text("Hasten used! It is now Red's turn.\nPress Enter, then click to select a Red unit.", 1)
                        stalemate(red)
                        window.onKeyPress(remove_text)
                        window.onLeftClick(select_red)

                if unit in cle_list:
                    if unit in red_list:
                        header_text("Mend used! It is now Blue's turn.\nPress Enter, then click to select a Blue unit.", 1)
                        stalemate(blue)
                        window.onKeyPress(remove_text)
                        window.onLeftClick(select_blue)

                    if unit in blue_list:
                        header_text("Mend used! It is now Red's turn.\nPress Enter, then click to select a Red unit.", 1)
                        stalemate(red)
                        window.onKeyPress(remove_text)
                        window.onLeftClick(select_red)


    # If all units on one team are dead, this functioned is called.
    def game_over():

        if red_dead == 8:
            blue_wins = window.image(0, 150, "Winning Text Blue.gif")
            thanks = window.image(0, 0, "Game Screen Heading Thanks.gif")
            window.onKeyPress(go_main_menu)


        if blue_dead == 8:
            red_wins = window.image(0, 150, "Winning Text Red.gif")
            thanks = window.image(0, 0, "Game Screen Heading Thanks.gif")
            window.onKeyPress(go_main_menu)


    # This function runs after after the end of every turn to check if at least one unit has a viable move option
    def stalemate(color):
        red_unit_immobile, blue_unit_immobile = 0, 0
        red_unit_count, blue_unit_count = 0, 0

        # Checks how many red units are alive, then checks how many can't move. If both are equal, it's a stalemate.
        if color == red:
            for red_unit in window.all("red"):
                red_unit_count += 1
                red_unit.obstruct = 0
                wall_count = 0

                if red_unit.x == 0:
                        wall_count += 1
                if red_unit.x == 700:
                        wall_count += 1
                if red_unit.y == 100:
                        wall_count += 1
                if red_unit.y == 700:
                        wall_count += 1
                red_unit.obstruct += wall_count

                for unit in window.all("unit"):

                    if red_unit.x - 100 == unit.x and red_unit.y == unit.y:
                        red_unit.obstruct += 1
                    if red_unit.x + 100 == unit.x and red_unit.y == unit.y:
                        red_unit.obstruct += 1
                    if red_unit.y - 100 == unit.y and red_unit.x == unit.x:
                        red_unit.obstruct += 1
                    if red_unit.y + 100 == unit.y and red_unit.x == unit.x:
                        red_unit.obstruct += 1

            for red_unit in window.all("red"):
                if red_unit.obstruct == 4:
                    red_unit_immobile += 1

            if red_unit_immobile == red_unit_count:

                for object in window.all():
                    window.remove(object)

                stalemate = window.image(0, 150, "Stalemate.gif")
                thanks = window.image(0, 0, "Game Screen Heading Thanks.gif")
                window.onKeyPress(go_main_menu)

        # Checks how many blue units are alive, then checks how many can't move. If both are equal, it's a stalemate.
        if color == blue:
            for blue_unit in window.all("blue"):
                blue_unit_count += 1
                blue_unit.obstruct = 0
                wall_count = 0

                if blue_unit.x == 0:
                        wall_count += 1
                if blue_unit.x == 700:
                        wall_count += 1
                if blue_unit.y == 100:
                        wall_count += 1
                if blue_unit.y == 700:
                        wall_count += 1
                blue_unit.obstruct += wall_count

                for unit in window.all("unit"):

                    if blue_unit.x - 100 == unit.x and blue_unit.y == unit.y:
                        blue_unit.obstruct += 1
                    if blue_unit.x + 100 == unit.x and blue_unit.y == unit.y:
                        blue_unit.obstruct += 1
                    if blue_unit.y - 100 == unit.y and blue_unit.x == unit.x:
                        blue_unit.obstruct += 1
                    if blue_unit.y + 100 == unit.y and blue_unit.x == unit.x:
                        blue_unit.obstruct += 1

            for blue_unit in window.all("blue"):
                if blue_unit.obstruct == 4:
                    blue_unit_immobile += 1

            if blue_unit_immobile == blue_unit_count:

                for object in window.all():
                    window.remove(object)

                stalemate = window.image(0, 150, "Stalemate.gif")
                thanks = window.image(0, 0, "Game Screen Heading Thanks.gif")
                window.onKeyPress(go_main_menu)


    # Clears the screen and takes the player back to the main menu when Enter is pressed
    def go_main_menu(key):
        nonlocal pause_program
        pause_program = True
        if key == "Return":
            clear_screen()
            main_menu()
            window.onLeftClick(main_menu_click)


    # Turns on the keystroke function which displays health at any time by pressing the space bar
    # as well as the the help menu which is turned on and off by pressing the escape key.
    window.onKeyPress(display_health)
    window.onKeyPress(help_menu)

    # Random turn order. If 1, Red goes first. If 2, Blue goes first.
    if turn_order == 1:
        window.onLeftClick(select_red)
    if turn_order == 2:
        window.onLeftClick(select_blue)

    # THIS IS THE END OF THE GAME LOGIC FUNCTION


# Starts the initial menu and click function. Starts as the game loads
main_menu()

# Turns on the left click function for the main menu. Starts as the game loads.
window.onLeftClick(main_menu_click)

# Opens the window with name "Falchion"
window.open("Falchion")
