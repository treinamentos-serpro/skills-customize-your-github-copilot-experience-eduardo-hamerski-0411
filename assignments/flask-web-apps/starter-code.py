from flask import Flask, redirect, render_template_string, request, url_for

app = Flask(__name__)

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "Frankenstein", "author": "Mary Shelley"},
]
next_book_id = 3

PAGE_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Book Catalog</title>
</head>
<body>
    <h1>Book Catalog</h1>
    <!-- Add the book list and forms here. -->
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Read and validate the form fields, then add a book.
        return redirect(url_for("index"))

    return render_template_string(PAGE_TEMPLATE, books=books)


@app.route("/books/<int:book_id>/delete", methods=["POST"])
def delete_book(book_id):
    # Remove the book with this ID if it exists.
    return redirect(url_for("index"))
