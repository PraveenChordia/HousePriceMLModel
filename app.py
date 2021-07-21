from server import app
import util

if __name__ == 'app':
    util.load_saved_artifacts()
    app.run()
