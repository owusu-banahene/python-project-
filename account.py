class Account:
    def check_password_length(self, password:str):
        if len(password) > 8:
            return True
        else:
            return False


if __name__ == '__main__':
    account = Account()
    print(f'The password length is {account.check_password_length("offtoschool")}')
