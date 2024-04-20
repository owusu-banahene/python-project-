import unittest
import account

class Test(unittest.TestCase):
    accountInfo = account.Account()
    def test_check_password_length(self):
        print('Checking the possible passwords')
        password_list = ['abeautifulday', 'astrictboss', 'alovelyhouse']
        for password in password_list:
            print(f'Checking the password {password}')
            self.assertTrue(self.accountInfo.check_password_length(password))


if __name__ == '__main__':
    unittest.main()
