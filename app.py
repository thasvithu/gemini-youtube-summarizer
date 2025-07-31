import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def extract_transcript_details(youtube_video_url):
    try:
        if "v=" in youtube_video_url:
            video_id = youtube_video_url.split("v=")[1].split("&")[0]
        else:
            raise ValueError("Invalid YouTube URL. It should contain 'v='.")

        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(video_id)

        transcript_text = " ".join([snippet.text for snippet in fetched_transcript])
        return transcript_text, video_id

    except TranscriptsDisabled:
        st.error("❌ Transcripts are disabled for this video.")
    except NoTranscriptFound:
        st.error("❌ No transcript found for this video.")
    except Exception:
        st.error(
            """
            ⚠️ **Could not retrieve transcript for this video.**

            This issue is likely because **YouTube is blocking transcript requests from cloud servers like Streamlit**. 
            This can happen due to:

            - Too many requests from the same IP.
            - The app is hosted on a cloud platform (like Streamlit, GCP, AWS), which YouTube restricts.

            **Solutions:**
            - Run this app locally on your computer to avoid IP blocks.
            - Or try a different video with subtitles enabled.
            """
        )
    return None, None

PROMPT_TEMPLATE = """
You are an expert YouTube video summarizer. Read the full transcript below and generate a concise summary highlighting the key points and main ideas.

Format the summary as a numbered list of 5 to 8 important takeaways, each 1-2 sentences long. Use clear and simple language.

Transcript:
"""

def generate_gemini_summary(transcript_text):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(PROMPT_TEMPLATE + transcript_text)
        return response.text
    except Exception as e:
        st.error(f"Error generating summary: {e}")
        return None

def main():
    st.set_page_config(page_title="YouTube Video Summarizer", page_icon="🎥", layout="wide")

    # Custom CSS
    st.markdown(
        """
        <style>
            .main-header {
                font-size: 2.8rem;
                font-weight: 700;
                color: #4A90E2;
                margin-bottom: 0.3rem;
            }
            .subtitle {
                font-size: 1.2rem;
                color: #555;
                margin-bottom: 2rem;
            }
            .stButton>button {
                background-color: #4A90E2;
                color: white;
                border-radius: 8px;
                padding: 10px 24px;
                font-size: 1.1rem;
                font-weight: 600;
            }
            .stButton>button:hover {
                background-color: #357ABD;
                color: #FFF;
            }
            .video-card {
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                border-radius: 12px;
                padding: 15px;
                background-color: #fff;
                margin-bottom: 1.5rem;
            }
            .summary-box {
                background-color: #F0F4FF;
                padding: 20px;
                border-radius: 12px;
                font-size: 1rem;
                line-height: 1.6;
                white-space: pre-wrap;
            }
            .summary-box::-webkit-scrollbar {
                width: 8px;
            }
            .summary-box::-webkit-scrollbar-thumb {
                background-color: #4A90E2;
                border-radius: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sidebar
    with st.sidebar:
        st.header("🔎 About")
        st.write(
            """
            This app transcribes YouTube videos and generates clear, concise summaries powered by **Google Gemini Pro**.
            
            **Steps to use:**
            1. Paste a valid YouTube video URL.
            2. Click **Generate Summary**.
            3. Wait for the magic 🪄!
            """
        )
        st.markdown("---")
        st.markdown(
            '<div style="text-align:center; font-size:14px;">'
            'Built with ❤️ by <strong>Vithusan.V</strong><br>'
            '✅ <a href="https://github.com/thasvithu" target="_blank">GitHub</a> | '
            '<a href="https://linkedin.com/in/thasvithu" target="_blank">LinkedIn</a>'
            '</div>',
            unsafe_allow_html=True
        )

    # Main UI
    st.markdown('<div class="main-header">YouTube Video Summarizer</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Paste a YouTube video link to get a summarized version of its transcript.</div>', unsafe_allow_html=True)

    youtube_url = st.text_input("YouTube Video URL", placeholder="https://www.youtube.com/watch?v=XXXXXXX")

    if youtube_url and "v=" in youtube_url:
        try:
            video_id = youtube_url.split("v=")[1].split("&")[0]
            with st.container():
                st.markdown('<div class="video-card">', unsafe_allow_html=True)
                st.image(f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg", use_column_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
        except:
            st.warning("Could not load video thumbnail.")

    if st.button("Generate Summary"):
        if not youtube_url or "v=" not in youtube_url:
            st.warning("Please enter a valid YouTube video URL containing 'v='.")
        else:
            with st.spinner("Fetching transcript and generating summary..."):
                transcript, video_id = extract_transcript_details(youtube_url)
                if transcript:
                    summary = generate_gemini_summary(transcript)
                    if summary:
                        st.success("Summary generated successfully! ✅")
                        st.markdown('<div class="summary-box">', unsafe_allow_html=True)
                        st.write(summary)
                        st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.warning("Could not retrieve transcript. Please try running the app locally or try another video.")

    # Footer
    st.markdown("---")
    st.markdown(
        '<div style="text-align:center; font-size:12px; color:#888;">'
        'Built with ❤️ by Vithusan.V | '
        '<a href="https://github.com/thasvithu" target="_blank">GitHub</a> | '
        '<a href="https://linkedin.com/in/thasvithu" target="_blank">LinkedIn</a>'
        '</div>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
