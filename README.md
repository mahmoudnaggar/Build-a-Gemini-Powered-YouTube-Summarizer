# 🎥 YouTube Summarizer with Gemini AI

Welcome to this project! In this workshop, we will build a web application that summarizes YouTube videos using the **Google Gemini API** and **Python Flask**. 🚀 

This project is designed for beginners to learn the fundamentals of Cloud computing and Generative AI.

---

## 🛠 Tech Stack
* **Backend:** Python (Flask) 🐍
* **AI Model:** Google Gemini API (via Vertex AI) 🤖
* **Deployment:** Google Cloud Run ☁️
* **Environment:** Google Cloud Shell Editor 💻

---

## 🚀 Getting Started

### Prerequisites
Before you begin, ensure you have:
1. **Google Cloud Project:** An active account with billing enabled.
2. **Cloud Shell:** Open the Cloud Shell Editor in your browser.
3. **Curiosity:** A mindset ready to learn new technologies! 🧠

🚀 **Prerequisites**

To ensure the project environment is correctly configured, you must enable the required Google Cloud APIs. Run the following command in your terminal:

```bash
gcloud services enable aiplatform.googleapis.com \
                           run.googleapis.com \
                           cloudbuild.googleapis.com \
                           cloudresourcemanager.googleapis.com
```

> 💡 **Pro-tip:** Before running the command, double-check that your CLI is authenticated and pointed to the correct project using:
>
> ```bash
> gcloud config set project [PROJECT_ID]
> ```

## 📚 What You'll Learn

- How to create a Gemini-powered back-end API using the Flask API library  
- How to build a GenAI app and link the front-end and back-end together  
- How to deploy the developed GenAI application on Cloud Run  


## Build the back-end
you will need to add Google Gen AI SDK library to requirements.txt file. It should looks like this:


```bash Flask==2.3.3
requests==2.31.0
debugpy # Required for debugging.
google-genai==1.2.0
```
## Create a virtual environment by typing in the terminal and wait for it to install sucessfully

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Deploy the Web Application
```bash 
gcloud run deploy --source .
```
