# 🎥 YouTube Video Summarizer with Google Gemini Pro

A clean, professional Streamlit app that **extracts YouTube video transcripts** and **summarizes them into concise key points** using the powerful **Google Gemini Pro** language model.

---

## 🔗 Live Demo

👉 [Try the App on Streamlit](https://gemini-youtube-summarizer-fn5qutzcseadegfxrnxwl8.streamlit.app/)

---

## ✨ Features

- 📺 **Paste any YouTube video URL** and extract its transcript automatically  
- 🧠 **Summarized with Google Gemini Pro** (`gemini-1.5-flash`)  
- 📌 Returns **5–8 concise takeaways** from the video  
- 🖼️ **Displays video thumbnail** preview  
- 🎨 **Modern and polished UI** using Streamlit  
- 📱 Responsive and user-friendly layout  
- ✅ Handles missing or disabled transcripts gracefully  
- 👨‍💻 Footer with developer credit and links  

---

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/thasvithu/youtube-video-summarizer.git
   cd youtube-video-summarizer
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**

   Create a `.env` file in the root directory and add your [Google Gemini API Key](https://ai.google.dev/):

   ```env
   GOOGLE_API_KEY=your_google_gemini_api_key
   ```

---

## 🚀 Usage

Run the app locally:

```bash
streamlit run app.py
```

1. Enter a valid YouTube video URL  
2. Click **“Generate Summary”**  
3. Read a neatly formatted list of summarized key points

---

## 📂 Project Structure

```
📁 youtube-video-summarizer/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Required Python packages
├── .env                  # (your API key, not committed)
└── README.md             # This file
```

---

## 🧰 Built With

- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://ai.google.dev/)
- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

---

## ⚠️ Notes

- The YouTube video must have **transcripts/subtitles enabled**  
- Only supports publicly available videos with English transcripts  
- This app uses **Google Gemini Pro's "gemini-1.5-flash"** model under the hood  

---

## 🧑‍💻 Author

**Vithusan.V**  
Built with ❤️ and Gemini.

🔗 [GitHub](https://github.com/thasvithu)  
🔗 [LinkedIn](https://linkedin.com/in/thasvithu)

---

## 🪪 License

This project is licensed under the MIT License.

---

## 🤝 Contributions

Feel free to open issues or pull requests to suggest improvements or report bugs. Your feedback is welcome!

---

## 📜 Disclaimer

This project is for **educational/demo purposes only**.  
Please use responsibly and ensure compliance with YouTube and Google API usage policies.
