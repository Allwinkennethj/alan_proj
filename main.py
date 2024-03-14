from factory import create_app
from config import db
from users.model import User_Details

app=create_app()

if __name__=="__main__":
    with app.app_context():
        # db.drop_all()
        db.create_all()
    app.run(debug=True,host='0.0.0.0')