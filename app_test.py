import unittest
from app import app

class BasicTestCase(unittest.TestCase):

    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'<title>flaskalicious</title>\n</head>\n<body>\n   <h1>welcome to flaskalicious</h1>\n</body>\n</html>' in response.data)
    
    def test_not_found(self):
        tester = app.test_client(self)
        response = tester.get('a', content_type='html/text')
        self.assertEqual(response.status_code, 404)
        self.assertTrue(b'was not found' in response.data)

if __name__ == '__main__':
    unittest.main()