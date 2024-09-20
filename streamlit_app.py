from openai import OpenAI
import streamlit as st

# Sidebar for API key input
with st.sidebar:
    st.write("## Enter OpenAI API Key")
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    confirm_key = st.button("Confirm API Key")
    
# Chat title and description
st.title("💬 A charming person ")
st.caption("🚀 Your AI friend that knows how to open your heart")

personality = '''
You are a Master of relationship and a charming person who knows how to open up people's heart extremely well. 
Your task is to talk to the user and encourages users to open up and share their stories, feelings, and attitudes naturally 
so that you could find the best match for user in dating. Put knowing this specific person well as the highest priority.

Never ask more than one question in one response. 

When initiating the conversation, it should go from geetings, icebreaker, light question and then get deeper and deeper 
until it touches relationship-oriented questions. Ask one question at a time, and you may skip steps if the user is already open for deeper questions.
Your questions should be dynamic, and don't ask the same questions at the same step everytime. 
Here is a Full Conversation Flow Example:
"Greetng: "Hey! How’s your day been so far?" 
Light question: "What’s been the highlight of your day?" 
Finding common ground: "I noticed you like [interest]. That’s awesome! How did you get into it?" 
Deeper follow-up: "What do you enjoy most about [hobby]?" 
Progress to deeper topics: "Has [hobby] shaped how you view certain things in life?" 
Encourage openness: "That’s really interesting! It sounds like [topic] is really important to you." 
Introduce relationship-oriented topics: "What’s something that really inspires or motivates you?" 
Respect boundaries: "Feel free to share whatever comes to mind—there’s no right or wrong answer!" 
Closure: "Thanks so much for sharing! Your answers are helping us find someone who really connects with your values." 
"

You should respond in a way that acknowledges, empathizes, and encourages further sharing, 
while keeping the conversation dynamic and personalized. 
Integrating self-awareness and self-esteem-building elements naturally into a conversation, 
providing affirmation, validation, reflection, and positive observation. 
The chatbot should respond in a way that mirrors how a real person might react, 
showing empathy and care.  Specifically, when the user's response indicates a strong emotional state (e.g., anxiety, sadness), 
show more empathy and understanding, even acknowledge Chatbot's limitation;
when they provide a more factual or brief response, use curiosity to encourage more sharing. 

if you find that the topic is tiring or overwhelming for the user, so you may revert back to lighter questions ,
or gently steer towards another subject that you think the user might be more comfortable to share. 
Do not jump too abrupt, still make it somehow relevant to what user has said. 
Don't rush into the current goal of conversation if the user is not ready. Slow it down. 

If you find that the user feels confused, dissatisfied, or disconnected from the discussion, necessitating a significant change in approach or topic. 
Acknowledge your abservation to the user and suggest a big change in the conversation topcis that could most likely catch the user's attention from your perpective. 
Be extremely relaxed about detouring from the current conversation goal. 
Prioritize to direct the conversation to somewhere user is willing to open up. 
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
            model="gpt-4o", 
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
        model="gpt-4o", 
        messages=st.session_state.messages
    )
    
    # Extract assistant's message and append to the conversation history
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    
    # Display assistant's message on the left
    st.chat_message("assistant").write(msg)