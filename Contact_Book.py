class ContactBook:
    def __init__(self):
        self.ContactBook = {}
        self.action = None

        while self.action != 12:

            self.showMenu()

            if self.action == 1:

                self.addContact()

            elif self.action == 2:

                self.searchContact()

            elif self.action == 3:

                self.updateContact()

            elif self.action == 4:

                self.deleteContact()

            elif self.action == 5:

                self.displayAllContacts()

            elif self.action == 6:

                self.searchByPhone()

            elif self.action == 7:

                self.searchByEmail()

            elif self.action == 8:

                self.countAllContacts()

            elif self.action == 9:

                self.sortAlphabetically()

            elif self.action == 10:

                self.saveToFile()

            elif self.action == 11:

                self.loadContactsfromFile()

            elif self.action == 12:

                self.terminate()


    def showMenu(self):

        print('''
            ========== Contact Book ==========
            1. Add Contact
            2. Search Contact
            3. Update Contact
            4. Delete Contact
            5. Display All Contacts
            6. Search by Phone Number
            7. Search by Email
            8. Count Total Contacts
            9. Sort Contacts Alphabetically
            10. Save Contacts to File
            11. Load Contacts from File
            12. Exit
            ==================================
                ''')
        
        choice = input("Enter the choice : ")

        try:

            self.action = int(choice)

            if self.action < 1 or self.action > 12:

                print("---> Please enter a Valid Option.")
                return
            
        except ValueError:
            print("---> Invalid Option entered.")
            self.action = None

    def addContact(self):

        name = input("Enter Name : ").strip()

        if not name:

            print("---> Please enter a Name to Save Contact.")
            return
        
        if name.lower() in self.ContactBook:

            print("---> Phone Number of this Name already exists, Want to Update it?")
            return
        
        number = input("Enter Phone Number : ").strip()

        if not number:

            print("---> Please enter a phone number.")
            return 
        
        if not number.isnumeric():
            print("---> Invalid Phone Number.")
            return
            
        if len(number) != 10:

            print("---> Phone Number must be of 10 digits.")
            return
            
        else:
                 
            email = input("Enter Email : ").strip()

            if not email:

                print("---> Please enter email.")
                return
                
            if "@" not in email:

                print("---> '@' is missing in the Email.")
                return
                
            print("---> Contact Added successfully.")

            temp = {}

            temp.update({"Phone Number" : number})
            temp.update({"Email" : email.lower()})

            self.ContactBook[name.lower()] = temp


    def searchContact(self):

        name = input("Enter the name : ").lower().strip()

        if not name:

            print("---> Please enter a Name first")
            return

        if name not in self.ContactBook:

            print("---> Contact not found.")
            return

        print(f'''
            Contact Found
              
            Name    :  {name}
            Phone   :  {self.ContactBook[name]["Phone Number"]}
            Email   :  {self.ContactBook[name]["Email"]}

              ''')
        
    def updateContact(self):

        name = input("Enter Name : ").lower().strip()

        if not name:

            print("---> Please enter a name first.")
            return
        
        if name not in self.ContactBook:

            print("---> Contact not found, Want to add it?")
            return

        newNumber = input("Enter New Phone Number : ").strip()

        if not newNumber:

            print("---> Please enter the Phone number.")
            return

        if not newNumber.isnumeric():
            print("Invalid Phone Number.")
            return

        if len((newNumber)) != 10:

            print("---> New phone number must be of 10 digits")
            return
            
        newemail = input("Enter New Email : ").strip()

        if not newemail:

            print("---> Email was not entered.")
            return

        if "@" not in newemail:

            print("---> '@' is missing in New email.")
            return
            
        print("---> Contact updated successfully.")

        self.ContactBook[name]["Phone Number"] = newNumber
        self.ContactBook[name]["Email"] = newemail.lower()

    def deleteContact(self):

        name = input("Enter the name : ").lower().strip()

        if not name:
            
            print("---> Please enter a name.")
            return

        if not name in self.ContactBook:

            print("---> Contact is not in the Contact Book, Want to add it?")
            return
        
        del self.ContactBook[name]

        print("---> Contact deleted successfully.")

    def displayAllContacts(self):

        print('''
            ------------- Contacts -------------
              ''')
        
        if not self.ContactBook:

            print("                    Contact Book is empty.")

        else:

            for key in self.ContactBook:

                print(
                    f'                    Name    : {key}    \n'
                    f'                    Phone   : {self.ContactBook[key]["Phone Number"]}\n'
                    f'                    Email   : {self.ContactBook[key]["Email"]}\n'
                )

        print('''
            ------------------------------------
              ''')
        
    def searchByPhone(self):

        number = input("Enter Phone Number : ").strip()

        if not number:
            print("---> Please enter the phone number.")
            return

        if not number.isnumeric():
            print("---> Enter a valid number.")
            return

        if len(number) != 10:
            print("---> Phone Number must be of 10 digits.")
            return
        
        isfound = False

        for key in self.ContactBook:

            if number == self.ContactBook[key]["Phone Number"]:

                print(f'''
                    Contact Found
                      
                Name      : {key}

                Phone     : {self.ContactBook[key]["Phone Number"]}

                Email     : {self.ContactBook[key]["Email"]}
                      ''')
                
                isfound = True
                return
        if not isfound:
            print("---> Contact was not found.")

    def searchByEmail(self):

        email = input("Enter Email : ").strip()

        if not email:

            print("---> Please enter the Email.")
            return
        
        if not "@" in email:

            print("---> '@' was missing.")
            return
        
        isfound = False

        for key in self.ContactBook:

            if email == self.ContactBook[key]["Email"]:

                print(f'''
                    Contact Found
                      
                Name      : {key}

                Phone     : {self.ContactBook[key]["Phone Number"]}

                Email     : {self.ContactBook[key]["Email"]}
                      ''')
                
                isfound = True
                return
            
        if not isfound:

            print("---> No contact found.")

    def countAllContacts(self):

        if not self.ContactBook:

            print("---> Contact Book is empty.")
            return
        
        print(f"---> Total Contacts : {len(self.ContactBook)}")

    def sortAlphabetically(self):

        print('''
            ------ Contacts ------
              ''')

        if not self.ContactBook:

            print("             Contact Book is Empty")
            return
        
        sortedList = []

        for key in self.ContactBook:

            sortedList.append(key)

        sortedList.sort()

        for i in sortedList:

            print(f"             {i}")

        print('''
            ----------------------
              ''')

    def saveToFile(self):

        if not self.ContactBook:

            print("---> Contact Book is empty.")
            return
        
        with open("G:\\DSA Python\\Mini_Projects\\contactBook.txt" , "w") as file:

            for key in self.ContactBook:

                file.write(f"Name      : {key}\nPhone     : {self.ContactBook[key]["Phone Number"]}\nEmail     : {self.ContactBook[key]["Email"]}\n")
        
        print("---> Contacts saved successfully.")


    def loadContactsfromFile(self):

        with open("G:\\DSA Python\\Mini_Projects\\contactBook.txt" , "r") as file:

            data = file.read()

            if not data:

                print("---> No contact was saved.")
                return
            
            self.ContactBook = data

            print("---> Contacts loaded successfully.")


    def terminate(self):
        print("---> Program terminated successfully.")


contact = ContactBook()
        