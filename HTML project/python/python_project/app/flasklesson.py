from app import app
print("palak")

@app.route('/')
@app.route('/firstpage')
def firstpage():
	print("here")
	pass