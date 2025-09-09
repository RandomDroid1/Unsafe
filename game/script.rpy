# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

#start with a video of

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."
    # worst code ever devised to open a text file, very mean
    init python:
        gui.init(1920, 1080)
        config.physical_width=1280
        config.physical_height=720
    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
