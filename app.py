from server import app
import util

if __name__ == 'main':
    util.load_saved_artifacts()
    app.run()
