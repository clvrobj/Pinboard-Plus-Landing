import os

from project import app as application

application.config.from_object(os.environ['APP_SETTINGS'])

if __name__ == "__main__":
    application.run()
