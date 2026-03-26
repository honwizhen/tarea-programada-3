# test_stack_arithmetic.py

import unittest
from stack_arithmetic import Stack, ArithmeticUnit


class TestStack(unittest.TestCase):
    """Test cases for Stack class"""
    
    def setUp(self):
        self.stack = Stack()
    
    def test_push_and_pop(self):
        self.stack.push(5)
        self.stack.push(10)
        self.assertEqual(self.stack.pop(), 10)
        self.assertEqual(self.stack.pop(), 5)
    
    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
    
    def test_peek(self):
        self.stack.push(5)
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)
        self.assertEqual(self.stack.size(), 2)  # peek doesn't remove
    
    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.size(), 3)
    
    def test_clear(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.clear()
        self.assertTrue(self.stack.is_empty())
    
    def test_pop_empty(self):
        self.assertIsNone(self.stack.pop())


class TestArithmeticUnit(unittest.TestCase):
    """Test cases for ArithmeticUnit class"""
    
    def setUp(self):
        self.unit = ArithmeticUnit()
    
    # Sum tests
    def test_addition(self):
        self.unit.process_input("5")
        self.unit.process_input("3")
        success, message = self.unit.process_input("+")
        self.assertTrue(success)
        self.assertEqual(self.unit.stack.peek(), 8)
    
    # Subtraction tests
    def test_subtraction(self):
        self.unit.process_input("10")
        self.unit.process_input("4")
        success, message = self.unit.process_input("-")
        self.assertTrue(success)
        self.assertEqual(self.unit.stack.peek(), 6)
    
    def test_subtraction_order(self):
        """Test that subtraction order is correct (first - second)"""
        self.unit.process_input("20")
        self.unit.process_input("8")
        self.unit.process_input("-")
        self.assertEqual(self.unit.stack.peek(), 12)  # 20 - 8 = 12
    
    # Multiplication tests
    def test_multiplication(self):
        self.unit.process_input("7")
        self.unit.process_input("6")
        success, message = self.unit.process_input("*")
        self.assertTrue(success)
        self.assertEqual(self.unit.stack.peek(), 42)
    
    # Division tests
    def test_division(self):
        self.unit.process_input("15")
        self.unit.process_input("3")
        success, message = self.unit.process_input("/")
        self.assertTrue(success)
        self.assertEqual(self.unit.stack.peek(), 5)
    
    def test_division_by_zero(self):
        self.unit.process_input("10")
        self.unit.process_input("0")
        success, message = self.unit.process_input("/")
        self.assertFalse(success)
        self.assertEqual(message, "Error: división entre cero")
        # Stack should remain unchanged
        self.assertEqual(self.unit.stack.get_all(), [10, 0])
    
    # Multiple consecutive operations
    def test_multiple_operations(self):
        # (5 + 3) * 2 = 16
        self.unit.process_input("5")
        self.unit.process_input("3")
        self.unit.process_input("+")
        self.unit.process_input("2")
        self.unit.process_input("*")
        self.assertEqual(self.unit.stack.peek(), 16)
    
    # Error tests: insufficient elements
    def test_insufficient_elements_empty_stack(self):
        success, message = self.unit.process_input("+")
        self.assertFalse(success)
        self.assertEqual(message, "Error: elementos insuficientes en la pila para operar")
    
    def test_insufficient_elements_one_element(self):
        self.unit.process_input("5")
        success, message = self.unit.process_input("+")
        self.assertFalse(success)
        self.assertEqual(message, "Error: elementos insuficientes en la pila para operar")
        self.assertEqual(self.unit.stack.get_all(), [5])
    
    # Error tests: invalid input
    def test_invalid_input_string(self):
        success, message = self.unit.process_input("abc")
        self.assertFalse(success)
        self.assertTrue("entrada no válida" in message)
    
    def test_invalid_operation(self):
        success, message = self.unit.process_input("%")
        self.assertFalse(success)
        self.assertTrue("entrada no válida" in message)
    
    def test_empty_input(self):
        success, message = self.unit.process_input("")
        self.assertFalse(success)
        self.assertEqual(message, "Error: entrada vacía")
    
    # Test decimal numbers
    def test_decimal_numbers(self):
        self.unit.process_input("3.5")
        self.unit.process_input("2.5")
        self.unit.process_input("+")
        self.assertEqual(self.unit.stack.peek(), 6.0)
    
    def test_mixed_numbers(self):
        self.unit.process_input("10")
        self.unit.process_input("3.5")
        self.unit.process_input("-")
        self.assertEqual(self.unit.stack.peek(), 6.5)
    
    # Test stack state display
    def test_stack_state_empty(self):
        self.assertEqual(self.unit.get_stack_state(), "Pila vacía")
    
    def test_stack_state_with_elements(self):
        self.unit.process_input("5")
        self.unit.process_input("10")
        self.assertEqual(self.unit.get_stack_state(), "Pila: [5, 10]")
    
    # Test clear stack
    def test_clear_stack(self):
        self.unit.process_input("5")
        self.unit.process_input("10")
        self.unit.clear_stack()
        self.assertTrue(self.unit.stack.is_empty())
    
    # Test that results are pushed correctly
    def test_result_pushed_after_operation(self):
        self.unit.process_input("8")
        self.unit.process_input("2")
        self.unit.process_input("/")
        self.assertEqual(self.unit.stack.size(), 1)
        self.assertEqual(self.unit.stack.peek(), 4)
    
    # Test consecutive operations
    def test_consecutive_operations(self):
        # 10 5 + 2 * = (10 + 5) * 2 = 30
        self.unit.process_input("10")
        self.unit.process_input("5")
        self.unit.process_input("+")
        self.assertEqual(self.unit.stack.peek(), 15)
        self.unit.process_input("2")
        self.unit.process_input("*")
        self.assertEqual(self.unit.stack.peek(), 30)
    
    # Test negative numbers
    def test_negative_numbers(self):
        self.unit.process_input("-5")
        self.unit.process_input("3")
        self.unit.process_input("+")
        self.assertEqual(self.unit.stack.peek(), -2)


def run_tests():
    """Run all tests with verbose output"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestStack))
    suite.addTests(loader.loadTestsFromTestCase(TestArithmeticUnit))
    
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == "__main__":
    run_tests()