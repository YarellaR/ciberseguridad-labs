import requests

def check_headers(url):
    try:
        print(f"\n[+] Analizando headers de seguridad en: {url}\n")

        response = requests.get(url, timeout=5)

        security_headers = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Referrer-Policy",
            "Permissions-Policy"
        ]

        for h in security_headers:
            if h in response.headers:
                print(f"[OK] {h}: {response.headers[h]}")
            else:
                print(f"[MISSING] {h}")

    except Exception as e:
        print(f"[ERROR] {e}")

    input("\nPresiona Enter para volver al menú...")
