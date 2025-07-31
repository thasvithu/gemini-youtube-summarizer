import streamlit as st
from dotenv import load_dotenv

load_dotenv() ## Load environment variables from .env file
import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        
        transcript = ""
        for i in transcript_text:
            transcript +=  " " + i['text']
        return transcript
    
    except Exception as e:
        raise e

prompt = """
You are an expert YouTube video summarizer. Your task is to read the full transcript of a video and generate a clear, concise summary of the main ideas and key points. 

Please provide the summary in no more than 250 words. The transcript will be appended below:
"""


def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt+transcript_text)
    return response.text


st.title("YouTube Video Summarizer")
youtube_link = st.text_input("Enter YouTube Video URL")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg", use_column_width=True)
    
if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript_details(youtube_link)
    
    if transcript_text:
        with st.spinner("Generating detailed notes..."):
            summary = generate_gemini_content(transcript_text, prompt)
            st.markdown("## Detailed Notes")
            st.write(summary)
