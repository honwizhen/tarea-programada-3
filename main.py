# main.py

from stack_arithmetic import ArithmeticUnit


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("   UNIDAD ARITMÉTICA BASADA EN PILA")
    print("="*50)
    print("1. Introducir elemento")
    print("2. Imprimir estado de la Pila")
    print("3. Salir")
    print("-"*50)


def main():
    """Función principal del programa"""
    unidad = ArithmeticUnit()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            print("\n--- INTRODUCIR ELEMENTO ---")
            print("Puede ingresar números o operaciones (+, -, *, /)")
            entrada = input("> ")
            
            # Procesar la entrada
            exito, mensaje = unidad.process_input(entrada)
            
            # Mostrar resultado
            print(mensaje)
            print("\n" + unidad.get_stack_state())
            
        elif opcion == "2":
            print("\n--- ESTADO DE LA PILA ---")
            print(unidad.get_stack_state())
            
        elif opcion == "3":
            print("\n¡Hasta luego!")
            break
            
        else:
            print("\n❌ Error: opción no válida. Por favor seleccione 1, 2 o 3.")


if __name__ == "__main__":
    main()