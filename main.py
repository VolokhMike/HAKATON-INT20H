import os

from app.routes import app


app.run(port=30000, debug=os.environ.get("FLASK_DEBUG") == "1")
