# def dec(main):
#     def wrapper(*arg):
#         print("Decorator call")
#         return main(*arg)
#     return wrapper

# @dec
# def login_method(arg):
#     if arg == "main":
#         print("Login success")
#     else:

#         print("Login not allowed")

# login_method("main1")

# sub_li = list(filter(lambda x:x%2 ==0, list(range(10))))
# print(sub_li)

# sub_li = list(map(lambda x:x%2 ==0, list(range(10))))
# print(sub_li)

# from functools import reduce
# sub_li = reduce(lambda x, y:x+y if x%2 ==0 else x, list(range(10)))
# print(sub_li)

# Run-time vs compile time

# ------------------------------------------------------------------------------------ #
# Classes
# Objects
# Methods
# Lists
# Dictionaries
# Loops
# Conditional statements
# Functions
# User input
# book_id, title, author, available_copies
# ------------------------------------------------------------------------------------ #
class book():
    def __init__(self):
        # self.book_id = book_id
        # self.title = title
        # self.author = author
        # self.available_copies = available_copies
        pass
    def add_book(self, book_id, title, author, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available_copies = available_copies
        book_dict = {}
        book_dict[self.book_id] =  {
            "title" : self.title,
            "author" :self.author,
            "available_copies" :self.available_copies
            }
        return book_dict

    def view_books(self, book_dict): 
        for i in book_dict.keys():
            print("Title = ",book_dict[i]["title"])
            print("Author = ",book_dict[i]["author"])
            print("Available copies = ",book_dict[i]["available_copies"])

    def search_book(self, search_by, search_query):
        self.search_by = search_by
        self.search_query = search_query  
        print("Book details:")
        for i in list(book_dict.values()):
            if i[f"{self.search_by}"] == self.search_query:
                print("Title = ", i["title"])
                print("Author = ", i["title"])
                print("Available copies = ", i["available_copies"])
    def get_book_id(self, book_dict, title):
        self.book_dict = book_dict
        self.title = title
        for i in self.book_dict.keys():
            if self.book_dict[i]["title"] == self.title:
                return i
    def get_book_inventory_count(self, book_dict, book_id):
        self.book_dict = book_dict
        self.book_id= book_id
        for i in self.book_dict.keys():
            if i == self.book_id:
                return self.book_dict[i]["available_copies"]
            
    def update_book_inventory(self, book_dict, book_id, action):
        self.book_dict = book_dict
        self.book_id= book_id
        self.action = action
        for i in self.book_dict.keys():
            if i == self.book_id:
                book_dict[i]["available_copies"] = book_dict[i]["available_copies"]+1 if self.action == "return" else book_dict[i]["available_copies"]-1
                break
        return book_dict
    def get_book_name(self, book_dict, book_id):
        self.book_dict = book_dict
        self.book_id = book_id
        for i in self.book_dict.keys():
            if  i == self.book_id:
                print(self.book_dict[i]["title"])

# ------------------------------------------------------------------------------------ #
# member_id, name
class member():
    def add_member(self, member_id, member_name):
        member_dict = {}
        self.member_name = member_name
        self.member_id = member_id
        member_dict[self.member_id] =  {
            "name" : self.member_name
            }
        return member_dict

    def view_members(self, member_dict):
        j = 0  
        for i in list(member_dict.keys()):
            j +=1
            print(j,": ",member_dict[i]["name"])

    def get_member_id(self, member_dict, member_name):
        self.member_dict = member_dict
        self.member_name = member_name
        for i in self.member_dict.keys():
            if self.member_dict[i]["name"] == self.member_name:
                return i
    
# ------------------------------------------------------------------------------------ #

# Issue book 
    # book exists flag
    # member exist flag
    # book_copies > 0
    # after issue call book_copies -=1
# Return book
    # book exist flag
    # return call book_copies +=1

class book_depository(book):
    def book_depo(self, book_depo_id, book_id, member_id, action):
        book_depo_dict = {}
        self.book_depo_id = book_depo_id 
        self.book_id = book_id
        self.member_id = member_id
        self.action = action 
        book_depo_dict[self.book_depo_id] =  {
            "book_id" : self.book_id,
            "member_id" : self.member_id,
            "action": "Returned" if self.action == "return" else "Issued"
            }
        return book_depo_dict
    def book_depo_history_by_member(self, book_depo_dict, member_id, book_dict):
        self.book_depo_dict = book_depo_dict
        self.member_id = member_id
        self.book_dict = book_dict 
        for i in self.book_depo_dict.keys():
            if self.book_depo_dict[i]["member_id"] == self.member_id:
                self.get_book_name(self.book_dict, self.book_depo_dict[i]["book_id"])
                print(self.book_depo_dict[i]["action"])
        
    
# ------------------------------------------------------------------------------------ #
obj_book = book()
book_dict = {1: {"title" : "Archers voice",
            "author" :"Mia",
            "available_copies" :3
            },
            2: {"title" : "A song to drown river",
            "author" :"Zheng",
            "available_copies" :4
            },}
book_id = 0
obj_member = member()
member_dict = {1: {
            "name" : "Brad"
            },
            2: {
            "name" : "John"
            }}
member_id = 0
obj_book_depo = book_depository()
book_depo_dict = {1: {
                    "book_id" : 1, "member_id" : 1, "action": "Issued" 
                },
                2: {
                    "book_id" : 2, "member_id" : 1, "action": "Returned" 
                }}
book_depo_id = 0
print("""
      Welcome to library
      Here you could add a book or a member at a certain time
      If needed you could search any book in inventory and same goes for a member
      """)
print("""
      Choose options:
      1. Add a new book to inventory
      2. Search a book in inventory
      3. View all books in inventory
      4. Add a new member 
      5. See all members
      6. Issue a book to a member
      7. Add the returned book to inventory
      8. Get book depository history
      9. To exit the system\n""")
option = 0
while option != 9:
    option = int(input("Enter your option: "))

    match option:
        case 1:
            print("Adding a new book to inventory")
            title = input("Enter the book name: ")
            author = input("Enter the author of the book: ")
            num_copies = int(input("Enter the quantity of books to be added: "))
            book_dict.update(obj_book.add_book(book_id+1, title, author, num_copies))
            print("Book has been addded to inventory")
        case 2:
            print("Searching a book in inventory")
            print("""Enter the option for searching
                1. By title
                2. By Author""")
            search_by = "title" if int(input("Enter your option: ")) == 1 else "author"
            search_query = input("Enter the name: ")
            obj_book.search_book(search_by, search_query)
        case 3: 
            print("Book List:")
            obj_book.view_books(book_dict)
        case 4:
            print("Adding a new member")
            member_name = input("Enter the member name: ")
            member_dict.update(obj_member.add_member(member_id+1, member_name))
        case 5: 
            print("Member list:")
            obj_member.view_members(member_dict)
        case 6:
            print("Issuing a book to a member")
            member_name = input("Enter the member name: ")
            book_name = input("Enter the book name: ")
            member_id = obj_member.get_member_id(member_dict, member_name)
            book_id = obj_book.get_book_id(book_dict, book_name)
            book_inventory_count  = obj_book.get_book_inventory_count(book_dict, book_id)
            if member_id is None or member_id == 0 or book_id == 0 or book_id is None:
                print("Please check entered information")
                pass
            elif book_inventory_count == 0:
                print("Out of inventory")
                pass
            else:
                book_depo_dict.update(obj_book_depo.book_depo(book_depo_id+1, book_id, member_id, "issued"))
                book_dict = obj_book.update_book_inventory(book_dict, book_id, "issued")
        case 7:
            print("Returning a book")
            member_name = input("Enter the member name")
            book_name = input("Enter the book name")
            member_id = obj_member.get_member_id(member_dict, member_name)
            book_id = obj_book.get_book_id(book_dict, book_name)
            book_inventory_count  = obj_book.get_book_inventory_count(book_dict, book_id)
            if member_id is None or member_id == 0 or book_id == 0 or book_id is None:
                print("Please check entered information")
                pass
            elif book_inventory_count == 0:
                print("Out of inventory")
                pass
            else:
                book_depo_dict.update(obj_book_depo.book_depo(book_depo_id+1, book_id, member_id, "return"))
                book_dict = obj_book.update_book_inventory(book_dict, book_id, "return")
        case 8:
            member_name = input("Enter name of the member:")
            member_id = obj_member.get_member_id(member_dict, member_name)
            if member_id is None or member_id == 0:
                print("Please check entered information")
                pass
            obj_book_depo.book_depo_history_by_member(book_depo_dict, member_id, book_dict)
        case 9:
            print("Exiting the system")
            
        case _:
            print("Invalid option try again")

