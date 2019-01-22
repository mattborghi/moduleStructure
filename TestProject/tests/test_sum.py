import unittest
from TestProject.Decoder.Main import Suma

# for testing sublime command
class TestSum(unittest.TestCase):
    def setUp(self):
        print("setUp suma")
        self.a = Suma()

    def tearDown(self):
        print("tearDown")

    def test_suma(self):
        res = self.a.sumando(2, 3)
        self.assertEqual(res, 5, "new hello world")


if __name__ == "__main__":
    unittest.main()
    print("It worked")
