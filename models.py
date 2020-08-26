class User:
    def __init__(self, name, fullname, id=None):
        self.id = id
        self.name = name
        self.fullname = fullname


class Address:
    def __init__(self, user_id, email_address, id=None):
        self.id = id
        self.user_id = user_id
        self.email_address = email_address