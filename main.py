from network.port_scanner import scan_ports
from web.header_checker import check_headers
from cryptography.hash_generator import generate_hash
from logs.log_analyzer import analyze_log

def menu():
    while True:
        print("\n=== CYBERSECURITY TOOLKIT ===")
        print("1. Port Scanner")
        print("2. Web Security Header Checker")
        print("3. Hash Generator")
        print("4. Log Analyzer")
        print("5. Salir")

        option = input("\nElige una opción: ")

        if option == "1":
            target = input("Ingrese IP o dominio: ")
            start_port = int(input("Puerto inicial: "))
            end_port = int(input("Puerto final: "))
            scan_ports(target, start_port, end_port)
        
        elif option == "2":
            print("entre a opcion 2")
            url = input("Ingrese URL (ej: http://example.com): ")
            check_headers(url)

        elif option == "3":
            text = input("Ingrese texto para generar hash: ")
            generate_hash(text)

        elif option == "4":
            file_path = input("Ingrese ruta del archivo log: ")
            analyze_log(file_path)

        elif option == "5":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intenta otra vez.")

if __name__ == "__main__":
    menu()
