from pathlib import Path

required_files = [
    "README.md",
    ".github/workflows/bad-ci.yml",
    ".github/workflows/good-ci.yml",
    ".github/workflows/vault-ci.yml",
    "app.py",
    "tests/test_app.py",
    "requirements.txt",
    "Dockerfile",
    "vault/docker-compose.yml",
    "vault/seed_and_read_demo.sh",
]

missing = [name for name in required_files if not Path(name).exists()]

if missing:
    print("Missing files:")
    for name in missing:
        print("-", name)
    raise SystemExit(1)

print("Project structure is valid.")
print("Bad CI/CD, good CI/CD and Vault example are present.")
