import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [1,2,3,4]

@app.get("/contact", response_class=HTMLResponse)
def get_list():
    return """
    <html>
        <head>
            <title>Contact Us</title>
        </head>
        <body>
            <h1>Contact Information</h1>
            <p>Email: contact@example.com</p>
        </body>
    </html>
    """




def run():
    store.get_categories()

if __name__ == "__main__":
    run()
    