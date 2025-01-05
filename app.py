import os
from flask import Flask, render_template

from utils.helpers import get_data_dir, prepare_file_content

app = Flask(
    __name__,
    static_url_path="/static",
    static_folder="static",
    template_folder="templates",
)


@app.route('/')
def index():
    data = get_data_dir()

    return render_template('index.html', data=data)


@app.route('/data/<filename>')
def serve_data(filename):
    # Load the content of the requested file
    content = prepare_file_content(filename)

    return render_template('data_template.html', filename=filename, content=content)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting server on port {port}")
    app.run(host="0.0.0.0", port=port)
