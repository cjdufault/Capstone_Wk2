class Author:
    def __init__(self, author_name):
        self.author_name = author_name
        self.books = []
    
    def publish(self, book_name):
        if book_name.strip() not in self.books:
            self.books.append(book_name)
        else:
            print(f"The book \"{book_name}\" by {self.author_name} already exists. \"{book_name}\" was not added.")
    
    def __str__(self):
        output_str = self.author_name + ":"
        
        # add each book w/ a newline and tab in front of it to output_str
        for book in self.books:
            output_str += "\n\t" + book
        
        return output_str
    

def main():
    austen = Author("Jane Austen")
    
    austen.publish("Pride and Prejudice")
    austen.publish("Emma")
    austen.publish("Emma ") # duplicate with a space to test rejection of duplicate names
    austen.publish("Northanger Abbey")
    austen.publish("Persuasion")
    austen.publish("Sense and Sensibility")
    austen.publish("Mansfield Park")
    austen.publish("Sanditon and the Watsons")
    
    expected_str = "Jane Austen:\n\tPride and Prejudice\n\tEmma\n\tNorthanger Abbey\n\tPersuasion\n\tSense and Sensibility\n\tMansfield Park\n\tSanditon and the Watsons"
    actual_str = str(austen)
    
    try:
        assert expected_str == actual_str, f"__str__ method failed: Actual string didn't match expected string.\nActual string --\n{actual_str}\nExpected string --\n{expected_str}"
        print("__str__ method passed")
        
        assert "Emma " not in austen.books, f"publish method failed: Did not reject a duplicate book."
        print("publish method passed")
    except AssertionError as msg:
        print(msg)
    

if __name__ == "__main__":
    main()
