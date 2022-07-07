import webbrowser  
import sqlite3        
  
db = sqlite3.connect("favorites.db")
  
c = db.cursor()
  
c.execute("""CREATE TABLE IF NOT EXISTS favorites
        (title TEXT, url TEXT)""")

def get_data():
    """
    Used to extract data from our database
    """
      
    c.execute('''SELECT * FROM favorites''')
    results = c.fetchall()
    return results
  
  
def get_favourite(titl):
    """
    Used to extract the favorite website
    """
      
    c.execute('''SELECT * FROM favorites WHERE title=?''',
              (titl, ))
    return c.fetchone()
  
def add_favourite(titl, url):
    """
    Used to add a new favorite website
    """
      
    c.execute("""INSERT INTO favorites (title, url) VALUES (?, ?)""",
              (titl, url))
    db.commit()
  
def remove_favourite(titl):
    """
    Used to remove a favorite website from the database
    """
      
    c.execute('''DELETE FROM favorites WHERE title=?''',
              (titl, ))
    db.commit()
  
while True:
    print()

    print("Type v to visit a favorite site,", end=" ")
    print("ls for the list of favourites,", end=" ")
    print("add to add a new item,", end=" ")
    print("del to delete,", end=" ")
    print("q to quit:", end=" ")
  
    userResponse = input("")
  
    if userResponse.lower() == "v":
        shortcut = input("Enter the website's shortcut: ")
        record = get_favourite(shortcut)
  
        try:
            webbrowser.open(record[1])
  
        except TypeError:
            print("This shortcut has been types incorrectly or doesn't exist.")
  
    elif userResponse.lower() == "ls":
        print(get_data())
  
    elif userResponse.lower() == "add":
        destination = input(
            "Enter the website URL for the shortcut (Eg; https://dummy.com): ")
  
        shortcut = input("Enter the shortcut you prefer for the URL: ")
  
        add_favourite(shortcut, destination)
  
    elif userResponse.lower() == "del":
        
        shortcut = input(
            "Enter the shortcut for the URL you want to remove: ")
        remove_favourite(shortcut)
        print("Removed Successfully!")
  
    elif userResponse.lower() == "q":
        break
  
    else:
        print("This command doesn't exist or has been typed incorrectly.")