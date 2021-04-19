from waitress import serve
import app

print("Running!")
print("Press CTRL+C to exit")
serve(app.app, listen="127.0.0.1:8080")
