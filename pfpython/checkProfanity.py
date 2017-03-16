import urllib

def text(file):
    file = open("insert location of file here.txt")
    contents = file.read()
    file.close()
    checkProfanity(contents)

def checkProfanity(text_to_check):
    connection = urllib.urlopen("Insert website" + contents)
    output = connection.read()
    connection.close()
    if "true" in output():
        print("dems fightin words in there.")
    if "false" in output():
        print("no fightin words in there.")
    else:
        print("Can't tell if fightin words in there.")

