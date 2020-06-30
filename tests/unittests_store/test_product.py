import unittest
import sys


from my_package.store.product import Product


class TestProduct(unittest.TestCase):

    # The steps:

    # t = TestProduct()
    # t.setUp()
    # t.test_discount_correct_answer()
    # t.tearDown()

    # t = TestProduct()
    # t.setUp()
    # t.test_discount_valid_type()
    # t.tearDown()

    def setUp(self):
        # You can write it only one time, instead of writing it in each test method
        self.product = Product(price=99.9)

    def tearDown(self):
        del self.product

    def test_discount_correct_answer(self):
        self.assertEqual(self.product.discount(10), 89.91)
        self.assertAlmostEqual(self.product.discount(10), 89.9, places=1)
        self.assertAlmostEqual(self.product.discount(10), 50, delta=40)
        # Test rare value: You can change the value because setUp method is invoked in each test method.
        self.product.price = 1000000
        self.assertEqual(self.product.discount(10), 900000)

    def test_discount_valid_type(self):
        self.assertRaises(TypeError, self.product.discount, '10')

    def test_common_functions(self):
        # Another examples:
        # https://kapeli.com/cheat_sheets/Python_unittest_Assertions.docset/Contents/Resources/Documents/index
        pass

    # Skipping tests
    # More examples:
    # https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(sys.platform.startswith("win"), "Not working on operating system of Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass


