from src.core.config import settings

def run():
    print("Smoke test passed!")
    print("App name:", settings.APP_NAME)

if __name__ == "__main__":
    run()
