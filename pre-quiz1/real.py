class Media:
    def __init__(self, title: str, rating: float):
        self.__title = title
        self.__rating = rating
        
    def get_title(self) -> str:
        return self.__title
    
    def get_rating(self) -> float:
        return self.__rating
    
    def __str__(self):
        return f"Media: {self.get_title():.1f} {self.get_rating():.1f}"
    
    def __eq__(self, other):
        if isinstance(other,self.__title):
            return True
        
class Book(Media):
    def __init__(self, title: str, rating: float, author: str):
        super().__init__(title, rating)
        self.__author = author
        
    def __str__(self): 
        return f"Book: {self.get_title()} {self.get_rating()} by {self.__author}"
    
class Movie(Media):
    def __init__(self, title, rating, duration: int):
        super().__init__(title, rating)
        self.__duration = duration
        
    def __str__(self): 
        return f"Movie: {self.get_title} {self.get_title} - {self.__duration}mins"
    
library = []
while True:
    cmd = input("Command: ")
    if cmd == "DONE":
        break
    elif cmd == ("ADD"):
        type = input("Type (Book/Movie): ")
        library.append(type)
        if type == ("book"):
            type = Book
            library.append(type)
            
            title = input("Title: ")
            library.append(title)
            
            rating = float(input("Rating: "))
            if rating < 0 or rating > 10:
                print("Invalid rating")
            library.append(rating)
            
            author = input("Author: ")
            library.append(author)
            
        elif type == ("movie"):
            type = Movie
            
            title = input("Title: ")
            library.append(title)
            
            rating = float(input("Rating: "))
            if rating < 0 or rating > 10:
                print("Invalid rating")
            library.append(rating)
            
            duration = float(input("Duration: "))
            library.append(duration)
            
    elif cmd == ("DEL"):
        to_del = input("Title to delete: ")
        try:
            for temp_object in library:
                if temp_object == "to_del":
                    library.remove(temp_object)
        except:
            print("Item not found")
            
m = Media(title,rating)
b = Book(author)
mv = Movie(duration)
print("-----Library Report-----")
print(library)