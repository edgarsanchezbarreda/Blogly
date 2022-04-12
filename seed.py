from models import User, db
from app import app

# drops any current tables, then creates them again.
db.drop_all()
db.create_all()

# If a table isnt empty than we empty it.
User.query.delete()