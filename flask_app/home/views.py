from flask import Blueprint ,render_template


home_bp = Blueprint('home_bp', __name__)

@home_bp.route("/")
def home():
    return render_template("home.html") 



# @home_bp.route('/portfolio')
# def view_portfolio():
#     return render_template('portfolio.html')