    # worst code ever devised to open a text file, very mean
    python:
        # thank you google for giving me the command to open stuff i hat epython https://www.geeksforgeeks.org/python/find-path-to-the-given-file-using-python/
        from pathlib import Path
    # This assigns the path to a variable so it can be joined with the known path next
    $ directory = Path.home() 
    $ firsttextpath = "\\Downloads\\Unsafe\\game\\notepad\\firsttext.txt"
    python:
        import time
        import os
        firsttext= (str(directory) + str(firsttextpath))
        # yippee stack overflow. This is attempting to open it, finally
        osCommandString = ("notepad.exe" + " " + str(firsttext))
        os.system(osCommandString)
        os.system("taskkill /f /im  C:\Windows\system32\.exe") # come back later, figure out how to close command prompt