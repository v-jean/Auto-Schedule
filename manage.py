from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import appFactory, db
from app.models import *
import os

app = appFactory(os.environ.get("CONFIG") or "default")

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()