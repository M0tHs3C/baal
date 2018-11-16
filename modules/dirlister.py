import os

def run(**args):

    print "[*] in dirlistermodule."
    files = os.listdir(".")

    return str(files)