# 🚀 Resume-Job Matching System  

An intelligent job recommendation system that matches resumes with relevant job listings using **NLP** and **Machine Learning**.

![Tech Stack](https://img.shields.io/badge/Tech%20Stack-React%20%7C%20Flask%20%7C%20Machine%20Learning%20%7C%20Pandas-blue)  
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

---

## 🎯 Project Overview  
This project leverages **Natural Language Processing (NLP) and Machine Learning** to analyze resumes, extract key skills, and recommend job listings based on relevance. The **Flask API** processes the resume text, cleans it, and compares it against a database of job descriptions to find the **best matches**.

### 🔥 Features  
- 📝 **Resume Processing** – Cleans and preprocesses the resume text.  
- 🎯 **Job Matching** – Recommends the most relevant jobs using **cosine similarity**.  
- 📌 **Skill Extraction** – Identifies key skills from resumes.  
- 🚀 **REST API** – Built using Flask for seamless integration.  
- 💻 **Frontend with React** – A simple UI for uploading resumes.  

---

## 🛠️ Tech Stack  
- **Frontend**: React.js  
- **Backend**: Flask (Python)  
- **Machine Learning**: NLP, TF-IDF, Cosine Similarity  
- **Database**: CSV (Job Descriptions)  
- **Libraries Used**: `pandas`, `nltk`, `sklearn`, `pickle`, `Flask`  

---

## 🚀 Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/resume-job-matcher.git
cd resume-job-matcher
```

### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 3️⃣ Train the Model (First-Time Setup)  
```bash
python ml_model/train_model.py
```

### 4️⃣ Start the Flask API  
```bash
cd api
python app.py
```

### 5️⃣ Run the Frontend (Optional)  
```bash
cd frontend
npm install
npm start
```

---

## 📡 API Endpoints  

### 📝 **Process Resume**  
```http
POST /process_resume
```
**Request:**  
```json
{
  "resume_text": "I am a Python developer with experience in Machine Learning and Flask."
}
```
**Response:**  
```json
{
  "cleaned_resume": "python developer experience machine learning flask"
}
```

### 🎯 **Match Jobs**  
```http
POST /match_jobs
```
**Request:**  
```json
{
  "resume_text": "I am a software engineer with expertise in Python and NLP."
}
```
**Response:**  
```json
{
  "job_matches": [
    {
      "title": "Machine Learning Engineer",
      "company": "Google",
      "description": "Looking for an ML Engineer with experience in NLP and Python.",
      "apply_url": "https://careers.google.com/job123"
    }
  ]
}
```

---

## 🤝 Contributing  
Contributions are welcome! If you'd like to contribute, follow these steps:  
1. Fork the repository  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Commit your changes (`git commit -m "Added a new feature"`)  
4. Push to the branch (`git push origin feature-branch`)  
5. Open a Pull Request  

---

## 📜 License  
This project is licensed under the **MIT License**.  

---

## 📧 Contact  
For any queries, feel free to reach out:  
📩 Email: agamjotmonga424@gmail.com 
👨‍💻 GitHub: [AgamjotSingh01](https://github.com/AgamjotSingh01)  

---

🌟 **If you like this project, don't forget to star ⭐ the repo!**
