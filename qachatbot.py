# import streamlit as st
# from langchain.chat_models import init_chat_model
# from langchain_groq import ChatGroq
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.messages import HumanMessage,AIMessage
# from langchain_core.prompts import ChatPromptTemplate
# import os


# ## Page config
# st.set_page_config(page_title="Simple LangChain Chatbot with Groq", page_icon="🤖")

# # Title
# st.title("🤖 Simple LangChain Chat with Groq")
# st.markdown("Learn LangChain basics with Groq's ultra-fast inference!")

# with st.sidebar:
#     st.header("Settings")

#     ## APi Key
#     api_key=st.text_input("GROQ API Key", type="password",help="GET Free API Key at console.groq.com")

#     ## Model Selection
#     model_name=st.selectbox(
#         "Model",
#         ["llama3-8b-8192", "gemma2-9b-it"],
#          index=0
#     )

#     # Clear button
#     if st.button("Clear Chat"):
#         st.session_state.messages = []
#         st.rerun()

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# ## Initialize LLM
# @st.cache_resource
# def get_chain(api_key,model_name):
#     if not api_key:
#         return None
    
#     ## Initialize the GROQ Model
#     llm=ChatGroq(groq_api_key=api_key,
#              model_name=model_name,
#              temperature=0.7,
#              streaming=True)
    
#     # Create prompt template
#     prompt = ChatPromptTemplate.from_messages([
#         ("system", "You are a helpful assistant powered by Groq. Answer questions clearly and concisely."),
#         ("user", "{question}")
#     ])

#     ## create chain
#     chain=prompt| llm | StrOutputParser()

#     return chain

# ## get chain
# chain=get_chain(api_key,model_name)

# if not chain:
#     st.warning("👆 Please enter your Groq API key in the sidebar to start chatting!")
#     st.markdown("[Get your free API key here](https://console.groq.com)")

# else:
#     ## Display the chat messages

#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.write(message["content"])

    
#     ## chat input
#     if question:= st.chat_input("Ask me anything"):
#         ## Add user message to session state
#         st.session_state.messages.append({"role":"user","content":question})
#         with st.chat_message("user"):
#             st.write(question)

#         # Generate response
#         with st.chat_message("assistant"):
#             message_placeholder = st.empty()
#             full_response = ""
            
#             try:
#                 # Stream response from Groq
#                 for chunk in chain.stream({"question": question}):
#                     full_response += chunk
#                     message_placeholder.markdown(full_response + "▌")
                
#                 message_placeholder.markdown(full_response)
                
#                 # Add to history
#                 st.session_state.messages.append({"role": "assistant", "content": full_response})
                
#             except Exception as e:
#                 st.error(f"Error: {str(e)}")


# # Footer
# st.markdown("---")
# st.markdown("Built with LangChain & Groq | Experience the speed! ⚡")

import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# ----------------------
# Page Config
# ----------------------
st.set_page_config(
    page_title="Agentic LangChain Chatbot with Groq",
    layout="wide"
)

# ----------------------
# Title & Description
# ----------------------
st.title("🤖 Agentic LangChain Chatbot")
st.markdown("""
Experience ultra-fast and intelligent conversations powered by **Groq's blazing inference** and **LangChain's power**. 
Supports LLaMA and Gemma models. Personalize your experience with theme, memory, and context options.
""")

# ----------------------
# Theme Styling
# ----------------------
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

with st.sidebar:
    dark_mode = st.checkbox("🌙 Dark Mode", value=st.session_state.dark_mode)
    st.session_state.dark_mode = dark_mode

page_bg_color = "#0e1117" if st.session_state.dark_mode else "#FFFFFF"
text_color = "#FAFAFA" if st.session_state.dark_mode else "#000000"
link_color = "#1f77b4" if not st.session_state.dark_mode else "#4dabf7"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {page_bg_color};
        color: {text_color};
    }}
    a {{
        color: {link_color} !important;
    }}
    .stMarkdown p {{
        color: {text_color};
    }}
    .stAlert {{
        color: {text_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------
# Sidebar Configuration
# ----------------------
with st.sidebar:
    st.header("⚙️ Settings")

    api_key = st.text_input("🔑 GROQ API Key", type="password", help="Get your key from https://console.groq.com")
    model_name = st.selectbox("🧠 Select Model", ["llama3-8b-8192", "gemma2-9b-it"], index=0)

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ----------------------
# Session State Init
# ----------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------
# Get LLM Chain
# ----------------------
@st.cache_resource
def get_chain(api_key, model_name):
    if not api_key:
        return None

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name=model_name,
        temperature=0.7,
        streaming=True
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI agent. Answer concisely and help the user effectively."),
        ("user", "{question}")
    ])

    return prompt | llm | StrOutputParser()

chain = get_chain(api_key, model_name)

# ----------------------
# Main Chat Interface
# ----------------------
if not chain:
    st.markdown(
        f"<div style='color:{text_color};'>🔐 Please enter your GROQ API Key to begin chatting.</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<a href='https://console.groq.com' target='_blank' style='color:{link_color};'>🔗 Get a free API key from Groq</a>",
        unsafe_allow_html=True
    )
else:
    # Display chat messages first
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Then display the chat input at the bottom
    if question := st.chat_input("💬 Ask something smart..."):
        st.session_state.messages.append({"role": "user", "content": question})

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            try:
                for chunk in chain.stream({"question": question}):
                    full_response += chunk
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# ----------------------
# Footer
# ----------------------
st.markdown(f"""
    <div style='text-align: center; padding-top: 2rem; font-size: 0.9rem; color: {text_color};'>
        <hr>
        Made with ❤️ using <a href='https://www.langchain.com' target='_blank' style='color:{link_color};'>LangChain</a>, 
        <a href='https://groq.com' target='_blank' style='color:{link_color};'>Groq</a>, and 
        <a href='https://streamlit.io' target='_blank' style='color:{link_color};'>Streamlit</a>
    </div>
""", unsafe_allow_html=True)