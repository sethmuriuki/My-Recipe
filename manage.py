from app import create_app
from flask_script import Manager, Server
from app.model import Comments,User
from  flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

# Creating app instances
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

#Migration
# migrate = Migrate(app,db)
# manager.add_command('db',MigrateCommand)

# @manager.shell
# def make_shell_context():
#     return dict(app = app, db = db, Category = Category, User = User, Recipe = Recipe, Comments = Comments)


if __name__ == '__main__':
    manager.run()
