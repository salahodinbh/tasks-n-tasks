from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask.cli import AppGroup

from application import create_app
from taskapi.models import db, Task, Question, Choice

# Crea la aplicación
app = create_app()

# Configura Flask-Migrate
migrate = Migrate(app, db)

# Crea un grupo de comandos para las migraciones
migrate_cli = AppGroup('db')

@migrate_cli.command('upgrade')
def upgrade():
    """Aplica las migraciones."""
    with app.app_context():
        MigrateCommand.upgrade()

@migrate_cli.command('downgrade')
def downgrade():
    """Revierte las migraciones."""
    with app.app_context():
        MigrateCommand.downgrade()

@migrate_cli.command('history')
def history():
    """Muestra el historial de migraciones."""
    with app.app_context():
        MigrateCommand.history()

@migrate_cli.command('current')
def current():
    """Muestra la versión actual de la base de datos."""
    with app.app_context():
        MigrateCommand.current()

# Registra el grupo de comandos en la aplicación
app.cli.add_command(migrate_cli)

# Configura el contexto del shell
@app.shell_context_processor
def shell_ctx():
    return dict(app=app,
                db=db,
                Task=Task,
                Question=Question,
                Choice=Choice)

if __name__ == '__main__':
    app.run()