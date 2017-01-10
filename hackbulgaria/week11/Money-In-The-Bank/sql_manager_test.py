from sys import path
from os import remove
import unittest
import hashlib
from sql_manager import *
from validators import PasswordError

path.append("..")


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        create_clients_table()
        register('Tester', '1Test@smth')

    def tearDown(self):
        cursor.execute('DROP TABLE clients')

    @classmethod
    def tearDownClass(cls):
        remove("bank.db")

    def test_register(self):
        register('Dinko', 'abcd1@ABC')
        hashed_pass = hashlib.sha512('abcd1@ABC'.encode()).hexdigest()
        cursor.execute('SELECT Count(*)  FROM clients WHERE username = (?) AND password = (?)', ('Dinko', hashed_pass))
        users_count = cursor.fetchone()

        self.assertEqual(users_count[0], 1)
        
        with self.assertRaises(PasswordError):
            register('Pesho', 'Pesho@123')

    def test_login(self):
        logged_user = login('Tester', '1Test@smth')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_wrong_password(self):
        logged_user = login('Tester', '123567')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = login('Tester', '1Test@smth')
        new_message = "podaivinototam"
        change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = login('Tester', '1Test@smth')
        new_password = "2Test#smth"
        change_pass(logged_user, new_password)

        logged_user_new_password = login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

if __name__ == '__main__':
    unittest.main()
    
    
