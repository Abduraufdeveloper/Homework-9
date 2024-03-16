class Author:
    def __init__(self,Title):
        self.Author = Author
        self.Title = Title
    def get_title(self):
        self.Title = "Harry Potter"
    def get_author(self):
        self.Author = "Joan Rowling"
class Author_2:
    def __init__(self,Title):
        self.Author = Author
        self.Title = Title
    def get_title(self):
        self.Title = "Pride and Prejudice"
    def get_author(self):
        self.Author = "Jane Austen"

class Author_3:
    def __init__(self,Title):
        self.Author = Author
        self.Title = Title
    def get_title(self):
        self.Title = "Hamlet"
    def get_author(self):
        self.Author = "William Shakespeare"

a = input(" HH , P , WP 3 tasidan birni kiriting :")
if a == "HH" :
    print( "Author = ",Author.get_author)
    print("Title = " , Author.get_title)
elif a == "P":
    print("Author = ", Author_2.get_author)
    print("Title = ",Author_2.get_title)
elif a == "WP":
    print("Author = " ,Author_3.get_author)
    print("Title = " ,Author_3.get_title)