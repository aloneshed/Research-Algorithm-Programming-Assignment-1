import unittest
import assignment_1

# support function for question 1
# -------------------------------
def f(a: int, b: float, c: int):
    return a + b + c


def g(a: int, b: float, c: int, d: float):
    return (a + b + c) * d


def j(a: int, b: float, c):
    return a * b * c

# -------------------------------


class TestAssignment1(unittest.TestCase):

    # Test question 1
    # -------------------------------

    def test_safe_call1(self):
        result = assignment_1.safe_call(f, a=5, b=7.0, c=3)
        self.assertEqual(result, 15.0)

    def test_safe_call2(self):
        result = assignment_1.safe_call(f, a=10, b=1.0, c=10)
        self.assertEqual(result, 21.0)

    def test_safe_call3(self):
        result = assignment_1.safe_call(g, a=5, b=7.0, c=3, d=2.0)
        self.assertEqual(result, 30.0)

    def test_safe_call4(self):
        result = assignment_1.safe_call(g, a=5, c=3, b=7.0, d=3.0)
        self.assertEqual(result, 45.0)

    # test function that have 1 argument without annotation
    def test_safe_call5(self):
        result = assignment_1.safe_call(j, a=10, b=3.0, c=2)
        self.assertEqual(result, 60.0)

    # c is without annotation in j so it can get any type
    def test_safe_call6(self):
        result = assignment_1.safe_call(j, a=10, b=3.0, c=3.0)
        self.assertEqual(result, 90.0)

    # test cases passing wrong type of annotation and expect an Raiserror
    def test_safe_call7(self):
        with self.assertRaises(TypeError):
            assignment_1.safe_call(f, a=5, b=7, c=3)
            assignment_1.safe_call(f, a=5.0, b=7.0, c=3)
            assignment_1.safe_call(f, a=10, b='abc', c=6)
            assignment_1.safe_call(g, a=5, b=7, c=3, d=10)
            assignment_1.safe_call(g, a=5.0, b=7.0, c=3, d=5)
            assignment_1.safe_call(g, a=10, b='abc', c=6, d='a')
            assignment_1.safe_call(j, a=5, b=7, c=3)
            assignment_1.safe_call(g, a=5.0, b=7.0, c=5)
            assignment_1.safe_call(g, a=10, b='abc', c=6)

    # -------------------------------
    # end of test question 1

    # Test question 3
    # -------------------------------
    def test_find_root1(self):
        result = assignment_1.find_root(lambda x: x**2-4, 1, 3)
        self.assertAlmostEqual(result, 2.0, 6)

    def test_find_root2(self):
        result = assignment_1.find_root(lambda x: x ** 3 - x ** 2 - 1, 1, 3)
        self.assertAlmostEqual(result, 1.4655714135075728)

    def test_find_root(self):
        result = assignment_1.find_root(lambda x: x**2-25, 1, 10)
        self.assertAlmostEqual(result, 5.0)

    def test_find_root(self):
        result = assignment_1.find_root(lambda x: x ** 2 - 49, 1, 10)
        self.assertAlmostEqual(result, 7.0)



if __name__ == '__main__':
    unittest.main()
