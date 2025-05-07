import unittest
from main import modulo

class TestModulo(unittest.TestCase):
    def test_modulo(self):
        # Тест на положительные числа
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(15, 5), 0)
        self.assertEqual(modulo(17, 4), 1)

        # Тест на отрицательные числа
        self.assertEqual(modulo(-10, 3), 2)
        self.assertEqual(modulo(10, -3), -2)
        self.assertEqual(modulo(-10, -3), -1)

        # Тест на деление на 1
        self.assertEqual(modulo(10, 1), 0)
        self.assertEqual(modulo(-10, 1), 0)

        # Тест на деление на само себя
        self.assertEqual(modulo(10, 10), 0)
        self.assertEqual(modulo(-10, -10), 0)

    def test_modulo_zero_division(self):
        # Тест на деление на ноль
        with self.assertRaises(ZeroDivisionError):
            modulo(10, 0)

if __name__ == '__main__':
    unittest.main()
