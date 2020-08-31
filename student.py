from dataclasses import dataclass


@dataclass
class Student:
    name: str
    college_id: int
    gpa: float
    

def main():
    alice = Student("Alice", 12345, 4.0)
    bob = Student("Bob", 54321, 3.0)
    
    print(alice.name)
    print(bob.college_id)
    
    print(alice)
    print(bob)
    

if __name__ == "__main__":
    main()
