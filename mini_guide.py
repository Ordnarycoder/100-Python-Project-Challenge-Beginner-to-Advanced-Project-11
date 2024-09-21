class Mini_guide:
    def __init__(self):
        self.users = {}

    def add_person(self, name, phone_number, e_posta):
        self.users[name] = {"phone number": phone_number, "e-posta": e_posta}

    def delete_person(self, name):
        if name in self.users:
            self.users.pop(name)
        else:
            print(f"{name} not found in the guide")
    
    def show_person(self):
        print(self.users)

ali = Mini_guide()

ali.add_person("Ali", 533, "ali@gmail.com")

ali.add_person("Mehmet", 534, "mehmet@gmail.com")

ali.show_person()
