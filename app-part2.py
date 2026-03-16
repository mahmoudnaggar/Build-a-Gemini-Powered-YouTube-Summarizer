import os
import uuid
from flask import Flask, render_template, request
from google import genai
from google.genai import types
import pdfplumber
from youtube_transcript_api import YouTubeTranscriptApi
import markdown
app = Flask(__name__)

PROJECT_ID = "REPLACE_WITH_YOUR_ID"
UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

client = genai.Client(
    vertexai=True,
    project=PROJECT_ID,
    location="us-central1",
)

@app.route("/")
def index():
    return render_template("index.html")


def extract_video_id(url):

    if "watch?v=" in url:
        return url.split("watch?v=")[1].split("&")[0]

    if "youtu.be/" in url:
        return url.split("youtu.be/")[1]

    return url


def get_youtube_transcript(url):

    video_id = extract_video_id(url)

    api = YouTubeTranscriptApi()

    transcript_list = api.list(video_id)

    transcript = transcript_list.find_transcript(['en','en-US','ar'])

    fetched = transcript.fetch()

    text = " ".join([item.text for item in fetched])

    return text


def extract_pdf_text(path):

    text = ""

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    return text


def ask_gemini(content, question, mode, model):

    if mode == "summary":

        prompt = f"""
        Summarize the following content clearly.

        Content:
        {content}
        """

    elif mode == "keypoints":

        prompt = f"""
        Extract the most important key points.

        Content:
        {content}
        """

    elif mode == "chat":

        prompt = f"""
        Based on the following content answer the question.

        Content:
        {content}

        Question:
        {question}
        """

    else:

        prompt = content

    response = client.models.generate_content(
        model=model,
        contents=[types.Part.from_text(text=prompt)]
    )

    return response.text


@app.route("/analyze", methods=["POST"])
def analyze():

    youtube_link = request.form.get("youtube_link")
    question = request.form.get("question")
    mode = request.form.get("mode")
    model = "gemini-2.0-flash"

    uploaded_file = request.files.get("file")

    content = ""

    try:

        if youtube_link:
            content = get_youtube_transcript(youtube_link)

        elif uploaded_file and uploaded_file.filename != "":

            ext = uploaded_file.filename.split(".")[-1].lower()

            filename = str(uuid.uuid4()) + "." + ext

            path = os.path.join(UPLOAD_FOLDER, filename)

            uploaded_file.save(path)

            if ext == "pdf":

                content = extract_pdf_text(path)

            elif ext in ["mp4","mov","avi","mkv"]:

                content = f"This is a video file named {uploaded_file.filename}. Analyze the video."

            os.remove(path)

        if not content:
            return "Please provide YouTube link or upload file."

        result = ask_gemini(content, question, mode, model)

        html = markdown.markdown(result)

        return html
    except Exception as e:

        return str(e)


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 8080))

    app.run(host="0.0.0.0", port=port)
