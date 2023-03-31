# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

label start:
    jump hall
# This is the start of the Exploration Sub FSM.

label hall:
    scene bg hall with fade

    menu hall_menu:
        "Exit the hall":
            jump east_2f_corridor

label east_2f_corridor:
    scene bg east 2nd floor corridor with fade

    menu east_2f_corridor_menu:

        "Enter the hall":
            jump hall

        "Go to the north lounge":
            jump north_2f_lounge

        "Go to the south lounge":
            jump south_2f_lounge

label north_2f_lounge:
    scene bg north 2nd floor lounge with fade

    menu north_2f_lounge_menu:

        "Go to the east corridor":
            jump east_2f_corridor

        "Go to the north corridor":
            jump north_2f_corridor

        "Go down to the first floor":
            jump north_1f_lounge

        "Go up to the third floor":
            jump north_3f_lounge

label south_2f_lounge:
    scene bg south 2nd floor lounge with fade

    menu south_2f_lounge_menu:

        "Go to the east corridor":
            jump east_2f_corridor

        "Go to the south corridor":
            jump south_2f_corridor

        "Go down to the first floor":
            jump south_1f_lounge

        "Go up to the third floor":
            jump south_3f_lounge

label north_2f_corridor:
    scene bg north 2nd floor corridor with fade

    menu north_2f_corridor_menu:

        "Go to the north lounge":
            jump north_2f_lounge

        "Enter TU office":
            jump tu

label tu:
    scene bg tu with fade

    menu tu_menu:

        "Exit TU office":
            jump north_2f_corridor

label south_2f_corridor:
    scene bg south 2nd floor corridor with fade

    menu south_2f_corridor_menu:

        "Go to the south lounge":
            jump south_2f_lounge

label north_1f_lounge:
    scene bg north 1st floor lounge with fade

    menu north_1f_lounge_menu:

        "Go up to the second floor":
            jump north_2f_lounge

        "Go to the north corridor":
            jump north_1f_corridor

        "Go to the east corridor":
            jump east_1f_corridor

label south_1f_lounge:
    scene bg south 1st floor lounge with fade

    menu south_1f_lounge_menu:

        "Go up to the second floor":
            jump south_2f_lounge

        "Go to the south corridor":
            jump south_1f_corridor

        "Go to the east corridor":
            jump east_1f_corridor

label north_1f_corridor:
    scene bg north 1st floor corridor with fade

    menu north_1f_corridor_menu:

        "Go to the north lounge":
            jump north_1f_lounge

        "Go to the mosque":
            jump mosque

label mosque:
    scene bg mosque with fade

    menu mosque_menu:

        "Exit the mosque":
            jump north_1f_corridor

label south_1f_corridor:
    scene bg south 1st floor corridor with fade

    menu south_1f_corridor_menu:

        "Go to the south lounge":
            jump south_1f_lounge

        "Go to PIKTI office":
            jump pikti

        "Go to Lab Pascasarjana":
            jump lab_pascasarjana

label pikti:
    scene bg pikti with fade

    menu pikti_menu:

        "Exit PIKTI office":
            jump south_1f_corridor

label lab_pascasarjana:
    scene bg pasca with fade

    menu lab_pascasarjana_menu:

        "Exit Lab Pascasarjana":
            jump south_1f_corridor

label east_1f_corridor:
    scene bg east 1st floor corridor with fade

    menu east_1f_corridor_menu:

        "Go to the north lounge":
            jump north_1f_lounge

        "Go to the south lounge":
            jump south_1f_lounge

label north_3f_lounge:
    scene bg north 3rd floor lounge with fade

    menu north_3f_lounge_menu:

        "Go down to the second floor":
            jump north_2f_lounge

        "Go to the north corridor":
            jump north_3f_corridor

        "Go to the east corridor":
            jump east_3f_corridor

        "Go to HMTC office":
            jump hmtc

label south_3f_lounge:
    scene bg south 3rd floor lounge with fade

    menu south_3f_lounge_menu:

        "Go down to the second floor":
            jump south_2f_lounge

        "Go to the south corridor":
            jump south_3f_corridor

        "Go to the east corridor":
            jump east_3f_corridor

label hmtc:
    scene bg hmtc with fade

    menu hmtc_menu:

        "Exit HMTC office":
            jump north_3f_lounge

label north_3f_corridor:
    scene bg north 3rd floor corridor with fade

    menu north_3f_corridor_menu:

        "Go to the north lounge":
            jump north_3f_lounge

        "Enter LP1 lab":
            jump lp1

        "Enter KCV lab":
            jump kcv

        "Enter KBJ lab":
            jump kbj

        "Enter RPL lab":
            jump rpl

label lp1:
    scene bg lp1 with fade

    menu lp1_menu:

        "Exit LP1 lab":
            jump north_3f_corridor

label kcv:
    scene bg kcv with fade

    menu kcv_menu:

        "Exit KCV lab":
            jump north_3f_corridor

label kbj:
    scene bg kbj with fade

    menu kbj_menu:

        "Exit KBJ lab":
            jump north_3f_corridor

label rpl:
    scene bg rpl with fade

    menu rpl_menu:

        "Exit RPL lab":
            jump north_3f_corridor

label south_3f_corridor:
    scene bg south 3rd floor corridor with fade

    menu south_3f_corridor_menu:

        "Go to the south lounge":
            jump south_3f_lounge

        "Enter LP2 lab":
            jump lp2

        "Enter Alpro lab":
            jump alpro

        "Enter MI lab":
            jump mi

label lp2:
    scene bg lp2 with fade

    menu lp2_menu:

        "Exit LP2 lab":
            jump south_3f_corridor

label alpro:
    scene bg alpro with fade

    menu alpro_menu:

        "Exit Alpro lab":
            jump south_3f_corridor

label mi:
    scene bg mi with fade

    menu mi_menu:

        "Exit MI lab":
            jump south_3f_corridor

label east_3f_corridor:
    scene bg east 3rd floor corridor with fade

    menu east_3f_corridor_menu:

        "Go to the north lounge":
            jump north_3f_lounge

        "Go to the south lounge":
            jump south_3f_lounge

        "Enter AJK lab":
            jump ajk

        "Enter IGS lab":
            jump igs

label ajk:
    scene bg ajk with fade

    menu ajk_menu:

        "Exit AJK lab":
            jump east_3f_corridor

label igs:
    scene bg igs with fade

    menu igs_menu:

        "Exit IGS lab":
            jump east_3f_corridor