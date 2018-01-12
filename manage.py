from app import create_app, db
from flask_script import Manager, Server
from app.model import Comments,User,Meals,Category,Search
from  flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

# Creating app instances
app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

# Migration
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Meals = Meals, Comments = Comments, Category = Category, Search = Search)


if __name__ == '__main__':
    manager.run()
