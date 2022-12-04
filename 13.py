from xmlrpc.client import ServerProxy

with ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as client:
    # Bert is not evil!
    print(client.phone("Bert"))
