from flask import Flask, render_template, request, redirect, url_for
from data_handler import write_csv, read_csv, append_csv

app = Flask(__name__)


@app.route("/story/", methods=["GET", "POST"])
@app.route("/story/<int:story_ID>", methods=["GET", "POST"])
def story_maker(story_ID=3000):
    """Handles the requests for adding/updating stories."""

    requested_data = None
    select_options = None

    requested_data = read_csv("static/data.csv")
    select_options = ["Planning", "TODO", "In Progress", "Review", "Done"]

    if request.method == "POST":
        html_names = ["title", "story", "crit", "business", "estimation", "stat"]
        content = [request.form[data] for data in html_names]

        if story_ID > 2500:
            append_csv("static/data.csv", content)
        else:
            requested_data[story_ID-1] = content
            write_csv("static/data.csv", requested_data)

        return redirect(url_for("list_page"))

    return render_template("form.html", fill=requested_data, result=story_ID-1,
                           select_options=select_options, story_ID=story_ID)


@app.route("/")
@app.route("/list")
@app.route("/list/<int:story_ID>", methods=["GET", "POST"])
def list_page(story_ID=None):
    """Lists out the stories - POST method deletes the chosen one."""

    requested_data = read_csv("static/data.csv")
    if request.method == "POST":
        requested_data.pop(story_ID)
        write_csv("static/data.csv", requested_data)

    return render_template("list.html", file=enumerate(requested_data))


@app.errorhandler(500)
def invalid_ID(error):
    return render_template("500.html")

if __name__ == "__main__":
    app.run()
