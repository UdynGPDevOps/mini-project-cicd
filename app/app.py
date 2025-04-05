from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Mini Project: DevOps CI/CD Demo</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f7f7f7;
                    margin: 0;
                    padding: 0;
                }
                .container {
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 30px;
                    background-color: white;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    border-radius: 10px;
                }
                h1 {
                    color: #007bff;
                }
                ul {
                    line-height: 1.8;
                }
                footer {
                    margin-top: 30px;
                    font-size: 0.9em;
                    color: #666;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 DevOps CI/CD Mini Project</h1>
                <p>This project demonstrates a complete CI/CD pipeline using:-</p>
                <ul>
                    <li>GitLab for version control and triggers</li>
                    <li>Jenkins for automation and pipeline orchestration</li>
                    <li>Docker for containerization</li>
                    <li>JFrog Artifactory for image storage</li>
                    <li>Flask as the sample web application</li>
                </ul>
                <p>💡 This project is part of my DevOps internship at Medtronic.</p>
                <footer>Made by Udayan Gupta</footer>
            </div>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
