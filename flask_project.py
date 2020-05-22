from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        "author": "Sandra Maria",
        "title": "How post on blog v1",
        "content": "Explanation",
        "date_posted": "May 22, 2020"
    },
    {
        "author": "Paulo Schar",
        "title": "Posting in my blog",
        "content": "Second post",
        "date_posted": "May 21, 2020"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
