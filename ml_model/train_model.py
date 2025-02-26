import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from preprocess import preprocess_dataset

# Load and preprocess job descriptions
df = preprocess_dataset("datasets/job_description.csv")

# Vectorize job descriptions using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
job_vectors = vectorizer.fit_transform(df["clean_text"])

# Save vectorizer and job vectors
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
pickle.dump(job_vectors, open("job_vectors.pkl", "wb"))

# Save job metadata (job_id, title, company_name)
job_data = df[["job_id", "title", "company_name","job_posting_url","formatted_work_type","work_type"]].to_dict(orient="records")
pickle.dump(job_data, open("job_data.pkl", "wb"))

print("✅ Model training complete! Files saved in /model/")
