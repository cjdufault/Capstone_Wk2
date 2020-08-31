from dataclasses import dataclass


@dataclass
class Student:
    """ 
    Much less typing to do here. It also allows you to explicitly define the 
    types of fields, which is really nice to have.
    """
    name: str
    college_id: int
    gpa: float
    

def main():
    alice = Student("Alice", 12345, 4.0)
    bob = Student("Bob", 54321, 3.0)
    
    print(alice.name)
    print(alice.college_id)
    print(alice.gpa)
    
    print(bob.name)
    print(bob.college_id)
    print(bob.gpa)
    
    
    """
    The default __str__ method for dataclasses puts the name of the class in
    the string, which may or may not be what you want it to do. You can always
    override it, though.
    """
    print(alice)
    print(bob)
    

if __name__ == "__main__":
    main()
