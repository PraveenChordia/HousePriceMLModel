import server
#import util

if __name__ == 'main':
    server.load_saved_artifacts()
    server.app.run()
