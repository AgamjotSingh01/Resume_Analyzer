import re
import pandas as pd

def extract_skills(resume_text):
    """Extracts skills from resume text using regex matching."""
    skills_pattern = r'\b(Java|Python|SQL|Machine Learning|React|Node\.js|Flask|Django|TensorFlow|NLP|Data Science|C\+\+|AWS|Azure|Kubernetes)\b'
    found_skills = re.findall(skills_pattern, resume_text, re.IGNORECASE)
    return list(set(found_skills))

if __name__ == "__main__":
    df = pd.read_csv("datasets/cleaned_resumes.csv")

    df['skills'] = df['clean_text'].apply(extract_skills)
    df.to_csv("datasets/resumes_with_skills.csv", index=False)

    print("✅ Resume skill extraction completed!")
