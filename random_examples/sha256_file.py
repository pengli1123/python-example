import hashlib
import argparse
import pathlib

def sha256_checksum(filename):
    """Calculates the SHA-256 hash of a file."""

    hasher = hashlib.sha256()
    with open(filename, 'rb') as file:
        while True:
            chunk = file.read(4096)  # Read the file in chunks
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="Script that calculate sha256 hash of a file"
        )
    parser.add_argument("--file", required=True, type=pathlib.Path)

    args = parser.parse_args()

    filename = args.file
    checksum = sha256_checksum(filename)
    print(f"SHA-256")
    print(f"file:     {filename}")
    print(f"checksum: {checksum}")
