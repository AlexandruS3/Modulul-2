class App:
    name = "Javelin"
    version = "FGM-148"
    author = "Martin <Martin@mail.md>"
    year = 1996
    rating = 5

def appInfo():
    app = App()
    print(f"Name: {app.name}")
    print(f"Version: {app.version}")
    print(f"Author: {app.author}")
    print(f"Year: {app.year}")
    print(f"Rating: {app.rating}")

appInfo()