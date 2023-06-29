from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Calculus Mentor',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 4,00,00'
}, {
  'id': 2,
  'title': 'Subject Matter Expert',
  'location': 'Kolkata, India',
  'salary': 'Rs. 25,00,00'
}, {
  'id': 3,
  'title': 'Coordinate Geometry Expert',
  'location': 'Remote'
}, {
  'id': 4,
  'title': 'Frontend Developer',
  'location': 'Hyderabad, India',
  'salary': '1150,000'
}]


@app.route('/')
def hello_mathify():
  return render_template('home.html', jobs=JOBS, company_name='Mathify')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
