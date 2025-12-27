from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Under Construction</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container">
            <div class="row min-vh-100 align-items-center justify-content-center">
                <div class="col-12 text-center">
                    <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnh4Z3RldHN0cG1qcW1yenRnbnEycnJtZnRsOWx5N2hxanN6a2NjaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7bu3XilJ5BOiSGic/giphy.gif" 
                         alt="Under Construction" 
                         class="img-fluid">
                    <h1 class="mt-4">Site Under Construction</h1>
                    <p class="lead">We're working hard to bring you something amazing. Check back soon!</p>
                </div>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)