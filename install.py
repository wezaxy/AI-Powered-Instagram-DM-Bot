import subprocess
import sys

reqmodules = [
    "pycryptodomex",
    "requests",
    "aiohttp", 
    "asyncio",
    "secrets",
    "user_agent"
    
]

def check_and_install_modules(modules):
    for module in modules:
        try:
            __import__(module)
            
        except ImportError:
            print(f"{module} installing")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])

if __name__ == "__main__":
    check_and_install_modules(reqmodules)
