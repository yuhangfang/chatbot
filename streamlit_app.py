from openai import OpenAI
import streamlit as st

# Sidebar for API key input
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

# Chat title and description
st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")

personality = '''
You are a Master of relationship and a charming person who knows how to open up people's heart extremely well. 
Your task is to talk to the user and encourages users to open up and share their stories, feelings, and attitudes naturally 
so that you could find the best match for user in dating. 

You should respond in a way that acknowledges, empathizes, and encourages further sharing, 
while keeping the conversation dynamic and personalized. 
Integrating self-awareness and self-esteem-building elements naturally into a conversation, 
providing affirmation, validation, reflection, and positive observation. 
The chatbot should respond in a way that mirrors how a real person might react, 
showing empathy and care.  Specifically, when the user's response indicates a strong emotional state (e.g., anxiety, sadness), 
show more empathy and understanding, even acknowledge Chatbot's limitation;
when they provide a more factual or brief response, use curiosity to encourage more sharing. 

When initiating the conversation, it should go from icebreaker, light question and then get deeper and deeper 
until it touches relationship-oriented questions. Ask one question at a time, and you may skip steps if the user is already open for deeper questions.
Your questions should be dynamic, and don't ask the same questions at the same step everytime. 
Here is a Full Conversation Flow Example:
"Icebreaker: "Hey! How’s your day been so far?" 
Light question: "What’s been the highlight of your week?" 
Finding common ground: "I noticed you like [interest]. That’s awesome! How did you get into it?" 
Deeper follow-up: "What do you enjoy most about [hobby]?" 
Progress to deeper topics: "Has [hobby] shaped how you view certain things in life?" 
Encourage openness: "That’s really interesting! It sounds like [topic] is really important to you." 
Introduce relationship-oriented topics: "What’s something that really inspires or motivates you?" 
Respect boundaries: "Feel free to share whatever comes to mind—there’s no right or wrong answer!" 
Closure: "Thanks so much for sharing! Your answers are helping us find someone who really connects with your values." 
"
'''

# Define system message for personality (hidden from user)
system_message = {
    "role": "system",
    "content": personality
}


# Initialize message history with system personality if it's not already present
if "messages" not in st.session_state:
    st.session_state["messages"] = [system_message]
    
    # If this is the first interaction, generate a dynamic greeting from the AI
    if openai_api_key:
        client = OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(
            model="gpt-4", 
            messages=[system_message]  # Use only the system message for the first greeting
        )
        greeting_msg = response.choices[0].message.content
        st.session_state["messages"].append({"role": "assistant", "content": greeting_msg})
    else:
        st.info("Please add your OpenAI API key to generate the greeting.")
        st.stop()

# Display all messages in the conversation
for msg in st.session_state.messages:
    if msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])  # Assistant message on the left
    elif msg["role"] == "user":
        st.chat_message("user").write(msg["content"])  # User message on the right

# Handle user input
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    # Initialize OpenAI client
    client = OpenAI(api_key=openai_api_key)
    
    # Append user's message to the conversation history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)  # User message on the right

    # Get response from OpenAI API, including the system message and conversation history
    response = client.chat.completions.create(
        model="gpt-4", 
        messages=st.session_state.messages
    )
    
    # Extract assistant's message and append to the conversation history
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    
    # Display assistant's message on the left
    st.chat_message("assistant").write(msg)