import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    """Cleans and preprocesses text data."""
    if pd.isnull(text):
        return ""
    
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    return " ".join(tokens)

def preprocess_dataset(file_path):
    """Loads job dataset, cleans descriptions, and prepares for ML."""
    df = pd.read_csv(file_path)

    # Drop unnecessary columns
    drop_cols = ["pay_period", "views", "company_id", "applies", "remote_allowed",
                  "application_url", "expiry", "closed_time",
                 "listed_time", "posting_domain", "sponsored"]
    
    df = df.drop(columns=[col for col in drop_cols if col in df.columns], errors="ignore")

    # Fill missing values
    df["company_name"] = df["company_name"].fillna("Unknown")
    df["location"] = df["location"].fillna("Unknown")
    df["formatted_experience_level"] = df["formatted_experience_level"].fillna("Unknown")
    df["skills_desc"] = df["skills_desc"].fillna("No skills provided")
    df["job_posting_url"] = df["job_posting_url"].fillna("No url's available")

    # Fill numerical missing values
    for col in ["max_salary", "min_salary", "med_salary", "normalized_salary"]:
        df[col] = df[col].fillna(df[col].median())

    # Combine job description and skills
    df["combined_description"] = df["description"].fillna("") + " " + df["skills_desc"].fillna("")

    # Apply text preprocessing
    df["clean_text"] = df["combined_description"].apply(clean_text)

    return df
