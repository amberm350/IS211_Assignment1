class book(): 
    title = ""
    author = ""
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display(self):
        print (self.title + ", written by "+ self.author)

B1 = book("Of Mice and Men","John Steinbeck")
B2 = book("To Kill a Mockingbird","Harper Lee")

B1.display()
B2.display()