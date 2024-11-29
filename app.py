from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Webpage</title>
    </head>
    <body style="font-family: Arial, sans-serif; margin: 20px;">
        <h1>Welcome to My Flask Webpage</h1>
        <p>This webpage was created using the Flask framework in Python and deployed on DigitalOcean using their App Platform.</p>

        <h2>How I Built This Page</h2>
        <ol>
            <li>Installed Flask using <code>pip install flask</code>.</li>
            <li>Created a Python file (<code>app.py</code>) with Flask code to define routes.</li>
            <li>Created a <code>requirements.txt</code> file for deployment.</li>
            <li>Pushed the project to a GitHub repository.</li>
            <li>Deployed the project to DigitalOcean App Platform directly from GitHub.</li>
        </ol>

        <h2>Challenges and Solutions</h2>
        <p><b>Challenge:</b> Understanding how to connect GitHub to DigitalOcean.<br>
        <b>Solution:</b> Followed the documentation on DigitalOcean to set up the deployment.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
