from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Load the home page

@app.route('/book', methods=['POST'])
def book_ride():
    # Get form data from the user
    name = request.form['name']
    pickup_location = request.form['pickup_location']
    drop_location = request.form['drop_location']
    ride_time = request.form['ride_time']

    # Pass the form data to the confirmation page
    return render_template('confirm.html', name=name, pickup_location=pickup_location, drop_location=drop_location, ride_time=ride_time)

if __name__ == '__main__':
    app.run(debug=True)
