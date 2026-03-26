# stack_arithmetic.py

class Stack:
    """Stack implementation for arithmetic operations"""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Push an item onto the stack"""
        self.items.append(item)
    
    def pop(self):
        """Pop an item from the stack"""
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        """View the top item without removing it"""
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)
    
    def get_all(self):
        """Return a copy of all items in the stack"""
        return self.items.copy()
    
    def clear(self):
        """Clear all items from the stack"""
        self.items.clear()


class ArithmeticUnit:
    """Arithmetic unit that operates on a stack"""
    
    def __init__(self):
        self.stack = Stack()
        self.operations = {
            '+': self._add,
            '-': self._subtract,
            '*': self._multiply,
            '/': self._divide
        }
    
    def _add(self, a, b):
        """Add two numbers"""
        return a + b
    
    def _subtract(self, a, b):
        """Subtract b from a"""
        return a - b
    
    def _multiply(self, a, b):
        """Multiply two numbers"""
        return a * b
    
    def _divide(self, a, b):
        """Divide a by b"""
        if b == 0:
            raise ZeroDivisionError("Error: división entre cero")
        return a / b
    
    def process_input(self, user_input):
        """
        Process user input (number or operation)
        Returns: (success, message)
        """
        # Trim whitespace
        user_input = user_input.strip()
        
        if not user_input:
            return False, "Error: entrada vacía"
        
        # Try to convert to number (integer or float)
        try:
            # Check if it's an integer
            if '.' in user_input:
                num = float(user_input)
            else:
                num = int(user_input)
            self.stack.push(num)
            return True, f"Número {num} agregado a la pila"
        except ValueError:
            # Not a number, check if it's an operation
            if user_input in self.operations:
                return self._execute_operation(user_input)
            else:
                return False, f"Error: entrada no válida '{user_input}'. Debe ser un número o una operación (+, -, *, /)"
    
    def _execute_operation(self, operation):
        """Execute an arithmetic operation"""
        # Check if there are at least two elements
        if self.stack.size() < 2:
            return False, "Error: elementos insuficientes en la pila para operar"
        
        # Pop the two top elements
        b = self.stack.pop()
        a = self.stack.pop()
        
        try:
            # Execute the operation
            result = self.operations[operation](a, b)
            self.stack.push(result)
            return True, f"Operación {operation} ejecutada: {a} {operation} {b} = {result}"
        except ZeroDivisionError as e:
            # Push back the original values if operation fails
            self.stack.push(a)
            self.stack.push(b)
            return False, str(e)
    
    def get_stack_state(self):
        """Get the current state of the stack"""
        if self.stack.is_empty():
            return "Pila vacía"
        return f"Pila: {self.stack.get_all()}"
    
    def clear_stack(self):
        """Clear the stack"""
        self.stack.clear()


def main():
    """Main program with user interface"""
    arithmetic_unit = ArithmeticUnit()
    
    while True:
        print("\n" + "="*50)
        print("UNIDAD ARITMÉTICA BASADA EN PILA")
        print("="*50)
        print("1. Introducir elemento")
        print("2. Imprimir estado de la Pila")
        print("3. Salir")
        print("-"*50)
        
        option = input("Seleccione una opción: ").strip()
        
        if option == "1":
            print("\n--- Introducir elemento ---")
            print("Puede ingresar números o operaciones (+, -, *, /)")
            user_input = input("Ingrese elemento: ")
            success, message = arithmetic_unit.process_input(user_input)
            print(message)
            print("\n" + arithmetic_unit.get_stack_state())
            
        elif option == "2":
            print("\n--- Estado de la Pila ---")
            print(arithmetic_unit.get_stack_state())
            
        elif option == "3":
            print("\n¡Hasta luego!")
            break
            
        else:
            print("\nError: opción no válida")


if __name__ == "__main__":
    main()