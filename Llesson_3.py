





class CustomUser:
    def __init__(self, first_name, last_name, email, password, age, gender, phone, secret_key):
        if isinstance(first_name, str):
            self.first = first_name
        else:
            raise Exception('First name is string')
        if isinstance(last_name, str):
            self.last = last_name
        else:
            raise Exception('Last name is string')
        if isinstance(email, str):
            self.email = email
        else:
            raise Exception('Email is string')
        if isinstance(password, str):
            self.password = password
        else:
            raise Exception('Password is string')
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('Age is integer')
        if isinstance(gender, str):
            self.gender = gender
        else:
            raise ValueError('Gender is string')
        if isinstance(phone, str):
            self.phone = phone
        else:
            raise ValueError('Phone is string')
        if isinstance(secret_key, str):
            self.secret = secret_key
        else:
            raise ValueError('Secret key is string')

    def __str__(self):
        return f'First-name: {self.first}\n' \
               f'Last-name: {self.last}\n' \
               f'Email: {self.email}\n' \
               f'Password: {self.password}\n' \
               f'Age: {self.age}\n' \
               f'Gender: {self.gender}\n' \
               f'Phone: {self.phone}\n' \
               f'Secret key: {self.secret}\n'


user_1 = CustomUser('Homer', 'Simpson', 'Homer@gmail.ru', '123', 30, 'male', '0789654123', 'Bishop')
print(user_1)


class Admin(CustomUser):
    def __init__(self, first_name, last_name, email, password, age, gender, phone, secret_key):
        super(Admin, self).__init__(first_name, last_name, email, password, age, gender, phone, secret_key)

    def admin_panel_login(self, password_login):
        if password_login == self.password:
            print('All info')


    def __str__(self):
        return super(Admin, self).__str__()









class VIPClient(CustomUser):
    def __init__(self, first_name, last_name, email, password, age, gender, phone, secret_key):
        super(VIPClient, self).__init__(first_name, last_name, email, password, age, gender, phone, secret_key)

    def __str__(self):
        return super(VIPClient, self).__str__()




class SuperUser(Admin, VIPClient):
    def __init__(self, first_name, last_name, email, password, age, gender, phone, secret_key):
        super(SuperUser, self).__init__(first_name, last_name, email, password, age, gender, phone, secret_key)

    def __str__(self):
        return super(SuperUser, self).__str__()
