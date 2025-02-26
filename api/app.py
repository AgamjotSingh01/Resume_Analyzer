import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, request, jsonify
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from ml_model.preprocess import clean_text
from ml_model.job_matcher import match_jobs


nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')

app = Flask(__name__)


# ========== Job Matching API ==========
@app.route("/match_jobs", methods=["POST"])
def job_match():
    data = request.get_json()
    resume_text = data.get("resume_text", "")

    if not resume_text:
        return jsonify({"error": "No resume text provided"}), 400

    cleaned_resume = clean_text(resume_text)  # Cleaned text is used internally
    job_matches = match_jobs(cleaned_resume)  # Passes cleaned text to job matcher

    return jsonify({"job_matches": job_matches})


# ========== Start Server ==========
if __name__ == "__main__":
    app.run(debug=True)
