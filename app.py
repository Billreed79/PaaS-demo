from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <html>
        <head><title>Azure PaaS Demo</title></head>
        <body>
            <h1>Welcome to Azure PaaS Deployment!</h1>
            <p>This is a simple Flask web app running on Azure App Service.</p>
	    <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2w2Ymp0ODY2Zjg1eWI5MmJmaTJ3eTlkdG1ydHN3emJuYjZ3N2xjYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hU3JLML7wx0RqJM6ym/giphy.gif">
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
