# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."
    # worst code ever devised to open a text file, very mean
    python:
        # thank you google for giving me the command to open stuff i hat epython https://www.geeksforgeeks.org/python/find-path-to-the-given-file-using-python/
        from pathlib import Path
        print(Path.home())
    # This assigns the path to a variable so it can be joined with the known path next
    $ directory = Path.home() 
    $ firsttextpath = "\\Downloads\\Unsafe\\game\\notepad\\firsttext.txt"
    python:
        firsttext= (str(directory) + str(firsttextpath))
        print(firsttext)
        # yippee stack overflow. This is attempting to open it, finally
        osCommandString = ("notepad.exe" + " " + str(firsttext))
        print(osCommandString)
        os.system(osCommandString)

    
    
    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
