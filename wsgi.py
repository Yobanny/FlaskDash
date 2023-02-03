from flask_app import init_flask
"""Application entry point."""



app = init_flask()
 
if __name__ == "__main__":
    app.run()