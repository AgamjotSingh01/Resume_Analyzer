import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from .preprocess import clean_text


# Load saved models
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
job_vectors = pickle.load(open("job_vectors.pkl", "rb"))
job_data = pickle.load(open("job_data.pkl", "rb"))

print("🔍 Sample Job Data:", job_data[:5])

def match_jobs(resume_text, top_n=5):
    """Finds top job matches for a given resume."""
    cleaned_resume = clean_text(resume_text)
    resume_vector = vectorizer.transform([cleaned_resume])
    
    # Compute cosine similarity
    similarity_scores = cosine_similarity(resume_vector, job_vectors).flatten()

    # Get top matches
    top_indices = np.argsort(similarity_scores)[-top_n:][::-1]

    top_jobs = [
        {
            "title": job_data[i]["title"],
            "company": job_data[i]["company_name"],
            "work_type": job_data[i].get("formatted_work_type", "No description available."),
            "apply_url": job_data[i].get("job_posting_url", "N/A")
        }
        for i in top_indices
    ]

    return top_jobs
