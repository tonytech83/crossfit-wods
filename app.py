import os

from flask import Flask, render_template

from utils.helpers import get_data_dir, prepare_file_content

app = Flask(
    __name__,
    static_url_path="/static",
    static_folder="static",
    template_folder="templates",
)


@app.route("/")
def index():
    data = get_data_dir()

    return render_template("index.html", data=data)


@app.route("/data/<filename>")
def serve_data(filename):
    # Load the content of the requested file
    content = prepare_file_content(filename)

    # Compute prev/next filenames in date order
    data_files = get_data_dir()
    names = [item["filename"] for item in data_files]
    try:
        idx = names.index(filename)
    except ValueError:
        idx = None

    prev_file = names[idx - 1] if idx is not None and idx > 0 else None
    next_file = names[idx + 1] if idx is not None and idx < len(names) - 1 else None

    return render_template(
        "data_template.html",
        filename=filename,
        content=content,
        prev_file=prev_file,
        next_file=next_file,
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting server on port {port}")
    app.run(host="0.0.0.0", port=port)
