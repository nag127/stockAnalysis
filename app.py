from flask import Flask, render_template, request, redirect, url_for
from crew.run_crew import run_crew_with_symbol
import os
import markdown


app = Flask(__name__)

def read_markdown_as_html(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        return markdown.markdown(content, extensions=["tables", "fenced_code"])
    return "<p>No content found.</p>"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        
        run_crew_with_symbol(symbol)

        # Read converted HTML from markdown files
        analysis_html = read_markdown_as_html("output/Analysis.md")
        recommendation_html = read_markdown_as_html("output/Recommendation.md")

        return render_template("results.html",
                               symbol=symbol,
                               analysis=analysis_html,
                               recommendation=recommendation_html)

    return render_template("index.html")



if __name__ == '__main__':
    os.makedirs("output", exist_ok=True)
    app.run(debug=True)






