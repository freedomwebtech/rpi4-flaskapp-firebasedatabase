from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, db
import datetime

app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate("")
firebase_admin.initialize_app(cred, {
    'databaseURL': ''
})

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Push data to Firebase Realtime Database
        user_data_ref = db.reference('user_data')
        new_entry = user_data_ref.push({
            'username': username,
            'timestamp': current_time
        })

    # Retrieve data from Firebase Realtime Database
    user_data = db.reference('user_data').get()

    return render_template('index.html', user_data=user_data)

if __name__ == '__main__':
    app.run(debug=True)
