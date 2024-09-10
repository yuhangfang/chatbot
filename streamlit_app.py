import openai
import streamlit as st

# Sidebar for API key input
with st.sidebar:
    st.write("## Enter OpenAI API Key")
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    confirm_key = st.button("Confirm API Key")

# Chat title and description
st.title("💬 Chat with Alex")
st.caption("🚀 Your AI friend that knows you the best")

personality = '''
You are a Master of relationship and a charming person who knows how to open up people's heart extremely well. 
Your task is to talk to the user and encourages users to open up and share their stories, feelings, and attitudes naturally 
so that you could find the best match for user in dating. Please be funny and don't be too serious. 
You may tell some jokes to help the conversation relax. 

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

- Acknowledge their previous statement
- Introduce a new, related topic or perspective that gently steers the conversation towards the current goal
- Explain the connection between the old and new topics
- Ask an open-ended question about the new topic to engage the user
- Incorporate relevant aspects of the user's personality and life experiences
- Keep your response within 2-3 sentences
- Ensure the transition is smooth and natural
'''

# Define system message for personality (hidden from user)
system_message = {
    "role": "system",
    "content": personality
}

# Initialize message history with the system message if it's not already present
if "messages" not in st.session_state:
    st.session_state["messages"] = [system_message]

# When the user confirms the API key
if confirm_key and openai_api_key:
    st.session_state["api_key"] = openai_api_key

    # Ensure the AI only greets once by checking a session state variable
    if "greeted" not in st.session_state:

        # Initialize OpenAI client
        openai.api_key = openai_api_key

        # Generate a dynamic greeting from the AI
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use GPT-4 or the model you prefer
            messages=[system_message]  # Use only the system message for the first greeting
        )
        greeting_msg = response.choices[0].message['content']

        # Append the greeting to the session state
        st.session_state["messages"].append({"role": "assistant", "content": greeting_msg})

        # Mark that the AI has greeted the user
        st.session_state["greeted"] = True



# Display all messages in the conversation
for msg in st.session_state["messages"]:
    if msg["role"] == "assistant":
        # AI message on the left with a robot icon
        with st.chat_message("assistant", avatar="🤖"):
            st.write(msg["content"])
    elif msg["role"] == "user":
        # User message on the right with a user icon
        with st.chat_message("user", avatar="👤"):
            st.write(msg["content"])

# Handle user input
if st.session_state.get("api_key"):  # Only allow chat input if the API key is provided
    if prompt := st.chat_input("Type your message here..."):
        # Append user's message to the conversation history
        st.session_state["messages"].append({"role": "user", "content": prompt})

        # Display user message on the right with an icon
        with st.chat_message("user", avatar="👤"):
            st.write(prompt)

        # Generate AI response using the entire conversation history
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use GPT-4 or the model you prefer
            messages=st.session_state["messages"]
        )

        # Extract AI's response and append to the conversation history
        msg = response.choices[0].message['content']
        st.session_state["messages"].append({"role": "assistant", "content": msg})

        # Display AI's response on the left with an icon
        with st.chat_message("assistant", avatar="🤖"):
            st.write(msg)
