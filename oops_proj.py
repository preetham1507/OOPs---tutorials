class chatbook:
    def __init__(self):
        self.username = ''
        self.password = '' 
        self.Loggedin = 'False'
        self.menu()

    def menu(self):
        user_input = input("""welcome to chatbook, hoiw would you like to proceed?
                                   1. press 1. to signup
                                   2. press 2 to signin
                                   3. press 3 to write a post
                                   4. press 4 to message a friend
                                   5. press any other key to exit   -   """)
        
        if user_input=="1":
            self.signup()
             
        elif user_input=="2":
            self.signin()

        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
        else:
            exit()

    def signup(self):
        email = input("enter your user email - ")
        pwd = input("setup you password - ")
        self.username = email
        self.password = pwd
        print("You have signed-up successfully")
        print('\n')
        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print("Please signup, press 1")

        else:
            email = input("enter your user email - ")
            pwd = input("setup you password - ")
            if self.username == email and self.password==pwd:
                print("You are signed in")
                self.loggedin=True

            else:
                print("You input correct credentials")

            print('\n')
            self.menu()

    def postings(self):
        if self.Loggedin:
            txt = input("Please input the text - ")
            print(f"Your content is posted - {txt}")
        
        else:
            print('You need to sign in first') 



obj = chatbook()