"""
Manages db table creation etc
TODO move this.
"""
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app
from models import db
from config import Config


app.config.from_object(Config)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
