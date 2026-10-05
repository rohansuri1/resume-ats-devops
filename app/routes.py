from flask import Blueprint, render_template, request
from pypdf import PdfReader

from app.analyzer import analyze_resume


main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        resume = request.files.get("resume")
        job_description = request.form.get("job_description", "")

        if resume and resume.filename:

            reader = PdfReader(resume)

            resume_text = ""

            for page in reader.pages:
                resume_text += page.extract_text() or ""

            result = analyze_resume(
                resume_text,
                job_description
            )

    return render_template(
        "index.html",
        result=result
    )