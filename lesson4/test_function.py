import unittest
import function


class TestChat(unittest.TestCase):
    def setUp(self):
        self.s = function.get_server_socket('localhost', 7777)
        self.c = function.get_client_socket('localhost', 7777)
        self.sender = self.s.accept()[0]

        function.send_data(self.c, {'test': 'test'})

    def tearDown(self):
        self.c.close()
        self.s.close()

    def test_get_data(self):
        self.assertEqual(function.get_data(self.sender), {'test': 'test'})

    def test_send_data(self):
        with self.assertRaises(TypeError):
            function.send_data()


if __name__ == '__main__':
    unittest.main()