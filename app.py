from utils.course_recommender import recommend_courses
from utils.company_recommender import recommend_companies
from flask import Flask, render_template, request
import PyPDF2

from utils.preprocess import preprocess_text
from utils.skill_extractor import extract_skills
from utils.gap_analysis import analyze_gap
from utils.predictor import predict_job
from utils.resume_validator import is_resume

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("upload.html")

@app.route('/analyze', methods=['POST'])
def analyze():

    if 'resume' not in request.files:
        return render_template("upload.html", error="No file uploaded.")

    file = request.files['resume']

    if file.filename == "":
        return render_template("upload.html", error="Please select a file.")

    try:
        reader = PyPDF2.PdfReader(file)
        text = ""

        for page in reader.pages:
            text += page.extract_text()

    except:
        return render_template("upload.html", error="Invalid file format. Upload PDF resume.")

    if not is_resume(text):
        return render_template("upload.html",
                               error="Invalid document. Please upload a resume.")

    tokens = preprocess_text(text)

    skills = extract_skills(tokens)

    role = "Data Analyst"

    match, missing = analyze_gap(skills, role)
    courses = recommend_courses(missing)
    companies = recommend_companies(skills)

    test_score = 80
    projects = 2
    experience = 1

    probability = predict_job(match, test_score, projects, experience)

    return render_template(
        "dashboard.html",
        skills=skills,
        match=match,
        missing_skills=missing,
        job_probability=probability,
        courses=courses,
        companies=companies
    )

if __name__ == "__main__":
    app.run(debug=True)