import unittest

# for testing sublime command
class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        print("setUp first sum")

    def tearDown(self):
        print("tearDown")

    def test_hello_world(self):
        self.assertTrue(True, "new hello world")


# class TestFunctions(TestCase):
#
#     def test_foo(self):
#         x = helloworld.foo(1)
#         self.assertEqual(x, 2)

if __name__ == "__main__":
    unittest.main()
