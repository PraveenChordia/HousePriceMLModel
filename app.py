from server import app
import util
print(__name__)
if __name__ != 'main':
    print(__name__, "in main")
    util.load_saved_artifacts()
    app.run()
