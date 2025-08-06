## 🧠 Agentic LangChain + Groq Chatbot
A fast and intelligent conversational AI chatbot built with Streamlit, LangChain, and Groq. Experience ultra-fast LLM inference using models like Llama and Gemma, manage conversation memory, toggle themes, and personalize your chat experience!

# 🚀 Features
State-of-the-art: Powered by Groq’s blazing-fast inference and LangChain’s robust LLM orchestration.

Model choices: Easily switch between LLaMA and Gemma models from the sidebar.

Dark/Light modes: Toggle modern themes for personal taste.

Session memory: Maintain chat history for seamless multi-turn interactions.

Custom API keys: Bring your own Groq API key securely.

Easy interface: Clean, intuitive Streamlit UI.

# 🛠️ Installation
Clone this repository

bash
git clone https://github.com/your-username/genai-groq-chatbot.git
cd genai-groq-chatbot
Create a virtual environment

bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install dependencies

bash
pip install -r requirements.txt
Set up environment variables

Copy or edit the file.env provided with your own API keys, or set these directly in your environment.

At a minimum, GROQ_API_KEY is needed (get it from Groq Console).

# 🔑 Environment File Example (file.env)

text

OpenAI_API_KEY = "..."         

GOOGLE_API_KEY = "..."   

GROQ_API_KEY = "..."       

🏃♀️ Running The App
Launch the Streamlit app:

bash
streamlit run qachatbot.py
Your browser will open up to the app interface. Enter your Groq API key in the sidebar, select your preferred model and theme, and start chatting!

# 📁 Project Structure

text

├── qachatbot.py        # Main Streamlit app

├── file.env            # Your local API keys

├── requirements.txt    # Python dependencies

└── README.md           # Project instructions
🤝 Credits
Streamlit

LangChain

Groq

Meta LLaMA

Google Gemma
