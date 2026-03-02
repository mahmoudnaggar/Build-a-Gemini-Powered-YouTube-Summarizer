<!--markdownlint-disable MD024 MD033 MD036 MD041 -->
<walkthrough-metadata>
  <meta name="title" content="Build a Gemini-Powered YouTube Summarizer" />
  <meta name="description" content="Build and deploy a YouTube video summarizer using Gemini API, Vertex AI, Flask, and Cloud Run." />
  <meta name="keywords" content="Gemini, Vertex AI, Cloud Run, Flask, Google Cloud, GenAI" />
</walkthrough-metadata>

# Build a Gemini-Powered YouTube Summarizer

## Let's get started

![Tutorial header image](https://codelabs.developers.google.com/static/devsite/codelabs/build-youtube-summarizer/img/13a0825947f9892b_856.png)

In this lab, you will build a web application that summarizes YouTube videos using **Gemini on Vertex AI**, then deploy it to **Cloud Run**.

<walkthrough-tutorial-difficulty difficulty="3"></walkthrough-tutorial-difficulty>

Estimated time:
<walkthrough-tutorial-duration duration="75"></walkthrough-tutorial-duration>

To get started, click **Start**.

---

# Step 1: Project Setup

Make sure you have an active Google Cloud project with billing enabled.

<walkthrough-project-setup billing="true"></walkthrough-project-setup>

Verify authentication:

```bash
gcloud auth list
```
```bash
gcloud config list project
```
Make sure that the following APIs are enabled, use the following command to set it:
- Vertex AI API
- Cloud Run Admin API
- Cloud Build API
- Cloud Resource Manager API

```bash 
gcloud services enable aiplatform.googleapis.com \
                           run.googleapis.com \
                           cloudbuild.googleapis.com \
                           cloudresourcemanager.googleapis.com
```
What you'll learn

- How to create a Gemini-powered back-end API using Flask API library
- How to build a GenAI app link the front-end and back-end together
- How to deploy the developed GenAI application on Cloud Run


## Create a Python Flask App on Cloud Run 

