from app import create_app
from app.routes import add_url
#run site 
if __name__ == '__main__':
    app = create_app()
    app=add_url(app)
    app.run()

