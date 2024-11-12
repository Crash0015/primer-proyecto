# app.py

from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    code = '''
    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return "Hello, World from Python!"
    
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
    ```
    '''
    html_content = f"""
    <html>
        <body style="font-family: Arial, sans-serif; text-align: center; padding: 20px;">
            <h1>Hello, World from Python!</h1>
            <h2>Code:</h2>
            <pre style="text-align: left; background-color: #f4f4f4; padding: 15px; border-radius: 5px;">{code}</pre>
        </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
