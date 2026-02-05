def analyze_log(file_path):
    failed_attempts = 0

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if "failed" in line.lower() or "error" in line.lower():
                    failed_attempts += 1

        print(f"\n[+] Archivo analizado: {file_path}")
        print(f"[!] Errores o intentos fallidos detectados: {failed_attempts}")

    except FileNotFoundError:
        print("[ERROR] Archivo no encontrado.")
    except Exception as e:
        print(f"[ERROR] {e}")

    input("\nPresiona Enter para volver al menú...")
