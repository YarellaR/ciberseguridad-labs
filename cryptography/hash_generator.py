import hashlib

def generate_hash(text):
    print("\n[+] Generando hashes...\n")

    md5_hash = hashlib.md5(text.encode()).hexdigest()
    sha1_hash = hashlib.sha1(text.encode()).hexdigest()
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()

    print(f"Texto: {text}\n")
    print(f"MD5:    {md5_hash}")
    print(f"SHA1:   {sha1_hash}")
    print(f"SHA256: {sha256_hash}")

    input("\nPresiona Enter para volver al menú...")
