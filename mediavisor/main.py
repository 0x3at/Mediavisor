from config import DevelopmentConfiguration

from app import create_app
settings = DevelopmentConfiguration()
if __name__ == '__main__':
    app = create_app(settings)
    app.run()

    