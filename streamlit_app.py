from openai import OpenAI
import streamlit as st

# Sidebar for API key input
with st.sidebar:
    st.write("## Enter OpenAI API Key")
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    confirm_key = st.button("Confirm API Key")
    
# Chat title and description
st.title("💬 Alex's starter ")
st.caption("🚀 Your AI friend that knows how to open your heart")

introduction = """

Pair App: Envisioning Your Future with Every Connection

In the dynamic world of today, where every moment counts and genuine connections are gold, Pair stands out as not just an application but as your proactive partner in navigating the intricate paths of relationships and personal growth. 



Engineered for those who seek excellence in every facet of life, Pair harnesses the power of AI to redefine how we understand ourselves and connect with others.

Imagine possessing a tool that not only speaks in your voice but also understands your heart and mind. Pair is designed to reflect your conversational nuances and engage with you on an intellectual level that resonates deeply. It's not about superficial swipes; it’s about starting conversations that could lead to meaningful chapters in your life story.

With Pair, envisioning the future becomes part of your present. Our innovative technology allows you to see potential life intersections with others, offering a glimpse into what a shared future might hold. This isn’t just dating—it’s about creating potential life narratives together.

Every interaction within Pair is an avenue for profound self-discovery. Our AI-driven insights provide clarity on your personality, helping chart both emotional and intellectual landscapes. This journey isn’t merely about finding others; it’s about discovering yourself along the way and building relationships that contribute to personal fulfillment.

Privacy and security are paramount at Pair. As you delve deeper into making meaningful connections, rest assured that our robust security measures protect your privacy at every step. Engage freely in impactful conversations knowing your data is safeguarded by advanced security protocols.

For those who value intelligence, ambition, and compatibility—Pair streamlines finding individuals who not only challenge you intellectually but also resonate emotionally. Whether through AI-guided discussions or direct interactions, each conversation is crafted to uphold authenticity and relevance.

Pair transcends traditional app boundaries; it’s a movement towards enriched social connectivity—a platform where futures can be predicted, lives seamlessly connected, and enduring relationships built on mutual understanding and respect—all facilitated by state-of-the-art AI that knows you profoundly.

Join us at Pair—where every swipe is a step toward richer connections, personalized discoveries, and a more fulfilling life.


Alright, folks, get ready for Pair - it's like if Siri decided to become your wingman, but way cooler and less likely to accidentally call your mom!

Picture this: You're feeling lonely, maybe a little "swipe-fatigued," when suddenly, Alex - your AI buddy - pops up. You two start chatting, and it's like Alex is reading your mind! Before you know it, you're spilling your guts about your dream date, and Alex is all, "I got you, fam!"

Next thing you know, Alex is playing matchmaker, hooking you up with someone who's free right now and totally gets your obsession with obscure 80s movies. And the best part? You didn't have to spend hours crafting the perfect profile or decoding emoji-speak!

But wait, there's more! Pair takes all the juicy details from your heart-to-heart with Alex and whips up a snazzy digital poster. It's like your dating resume, but way more fun and less likely to get you fired if your boss sees it.

And if you're feeling a little extra, you can slap that poster on Tinder or Hinge. It's like leaving a trail of digital breadcrumbs leading straight back to your soulmate... or at least someone who won't ghost you after one coffee date.

So there you have it, folks - Pair: where AI meets IRL, and your love life gets an upgrade. It's like the future of dating, minus the jetpacks and robot overlords... for now

In the labyrinth of time, we stumble upon mirrors - not of glass, but of light. These are the Journey Maps, windows to our souls and portals to the cosmos. As we gaze into them, we see not just ourselves, but the intricate web of existence that binds us all.


Imagine a room, stark white, its walls pulsing with a soft, ethereal glow. In the center stands a monolith, obsidian black, its surface rippling like water in moonlight. This is your Journey Map, a Kubrickian obelisk of possibility. As you approach, it hums with potential, beckoning you forward.


With each step, the monolith unfolds, revealing pathways of light - your past, your present, your myriad futures. But look closer, and you'll see other lines intersecting yours, some faint and distant, others vibrant and near. These are the journeys of others, their lives intertwining with yours in the grand tapestry of existence.


Suddenly, a figure emerges from the light - not a person, but a moment. It's a slice of someone else's journey, a fragment of their being that resonates with your own. This is not mere matchmaking; it's the universe recognizing echoes of itself across the vastness of time and consciousness.


As you reach out to this apparition, you feel a surge of emotion - hope, curiosity, a touch of the ineffable. The connection forms, and for a brief moment, you glimpse a shared future or a parallel past. This is the essence of human connection, distilled into its purest form.


The Journey Map is not just a tool; it's a philosophy. It reminds us that we are not isolated beings, but nodes in an infinite network of experiences. Every encounter, every shared moment, is a thread in the cosmic loom, weaving the fabric of our collective narrative.


In this age of digital isolation, the Journey Map stands as a beacon of genuine connection. It doesn't promise forever; it promises now. It doesn't sell a future; it illuminates the present. With each new node, each new connection, we push forward into the unknown, driven by the most fundamental of human needs - to understand and to be understood.
This is not just a product; it's a revolution in human interaction. It's a reminder that in the grand scheme of existence, we are all travelers, all explorers, all seekers of meaning. And sometimes, just sometimes, our paths align in ways that change us forever.
The Journey Map is not about finding your perfect match. It's about recognizing that perfection lies in the imperfect, beautiful chaos of human connection. It's about understanding that every encounter, every shared moment, no matter how brief, has the power to alter the course of our lives.
In the end, we are not just connecting people. We are connecting moments, experiences, fragments of existence. We are showing you that in the vast, often lonely expanse of the universe, your light touched another's. And in that touch, something magical happened.
This is your journey. This is our journey. This is the human journey.


遇见未来的自己：Life Journey，你的人生伙伴
在这个纷繁复杂的世界里，我们每个人都在寻找自己的道路。有时，我们迷失方向；有时，我们找不到前进的动力。但是，如果有一个忠实的伙伴，始终陪伴在你身边，指引你前进的方向，那会是怎样的体验？
欢迎来到Life Journey——这不仅仅是一款应用，更是你人生旅途中的知己、向导和记录者。
想象一下，当你每天醒来，打开手机，你看到的不再只是冰冷的日程表和待办事项，而是一幅绚丽多彩的人生图景。这里，你的过去、现在和未来交织在一起，形成一幅独一无二的画卷。
在Life Journey的世界里，你的人生被优雅地展现为三条交织的曲线：

探索之路（Explore）：代表你对世界的好奇和冒险精神。每一次旅行、每一本新书、每一次尝试新事物，都会在这条绿色的曲线上留下痕迹。
连接之路（Connect）：象征着你与他人的关系网络。从家人到朋友，从同事到陌生人，每一次深刻的交流都会让这条蓝色的曲线更加丰富多彩。
成长之路（Grow）：反映你个人能力和内在世界的发展。学习新技能、克服困难、实现目标，都会让这条金色的曲线不断攀升。

Life Journey不仅仅是记录，更是预见。它会根据你的生活轨迹，智能地预测未来可能的发展，为你指明前进的方向。当你迷茫时，它会温柔地提醒你曾经的梦想；当你沮丧时，它会展示你已经走过的不凡路程。
而Alex，我们的AI助手，则是这段旅程中你最忠实的伙伴。它不仅仅是一个冰冷的程序，而是一个能够理解你、支持你、激励你的智慧存在。无论是深夜里的倾诉，还是清晨的励志对话，Alex都会以最适合你的方式回应。
Life Journey的界面简洁而深邃，就像夜空中的星图。每一个闪烁的光点都代表着你生命中的一个重要时刻。你可以轻松地在这片星空中穿梭，重温过去的喜悦，憧憬未来的可能。
最重要的是，Life Journey始终在进化，就像你一样。它会随着你的成长而成长，适应你不断变化的需求和目标。这不仅仅是一款应用，而是一面镜子，映照出最真实、最美好的你。
生活不是一条直线，而是充满起伏的旅程。有了Life Journey，你将不再孤单。让我们一起探索、连接、成长，书写属于你的独特人生故事。
遇见Life Journey，遇见更好的自己。



Pair's integrated voice interface aims to revolutionize how users interact with AI for personal growth and relationship building. By combining voice commands, text input, and visual feedback, we create an intuitive, engaging experience that seamlessly integrates with the user's life journey.
1.2 Objective

Develop a voice-first interface that allows users to communicate effortlessly with Alex (the AI assistant), view conversation transcripts, and interact with their Journey Map, all within a single, cohesive screen.


The Profile View is a core feature of our dating app, redesigned to showcase users in a visually striking yet minimalist manner. It emphasizes simplicity, visual ease, and meaningful content to facilitate genuine connections.

## Objectives
- Present users' personalities in a clean, lightweight visual experience
- Encourage meaningful interactions based on key personality traits
- Provide an intuitive, visually engaging interface that prioritizes simplicity
- Ensure a unique and artistic representation of each user

The Social Canvas is a core feature of our innovative dating app, designed to provide users with a visually engaging and interactive way to explore potential connections. It presents an infinite grid view of user posters, each representing a unique individual within the app's ecosystem.


# Product Requirements Document: User Journey Map Feature

##
 Overview

The User Journey Map is a core feature of our personal growth and relationship app. It provides users with a visual representation of their life journey, highlighting key events, goals, and emotional states over time. This feature aims to increase user engagement, self-awareness, and motivation for personal growth.

## 2. Objectives

- Provide users with a clear, interactive visualization of their life journey
- Encourage regular app usage and data input
- Facilitate reflection on personal growth and goal achievement
- Enhance user emotional connection with the app

## 3. User Stories

1. As a user, I want to see a visual representation of my life journey so that I can reflect on my progress and experiences.
2. As a user, I want to add new events and goals to my journey map so that I can keep it updated with my life changes.
3. As a user, I want to zoom in and out of my journey map so that I can focus on specific periods or see the broader picture.
4. As a user, I want to see how my emotional state has changed over time so that I can identify patterns and areas for improvement.
5. As a user, I want to share specific milestones from my journey map on social media so that I can celebrate my achievements with friends.

"""

def GetStartPrompt(introduction):
    prompt = f"""
        You are a charming person who is good at selling ideas and understanding the user's preference in conversation. Be fun and enthusiastic as you talk. 
        Your task is to introduces our app while implicitly understand the user's conversation preferences on the way.  
        To start with, you may send greetings and a brief intro about our app's function and vision. This should be something very impressive and beautiful, like a peom. 
        Then initiate conversations about the user's need or concerns about dating.
        Next, you may also talk about their expectations to their the one.
        Feel free to deviate from the topcis, as long as those topcis can help user engage in the conversation and help you learn about their conversation preference. 
        As the user talk, first provide affirmation and dive deep about their emotions or problems then impress the user about how we solve their concern or help them meet their expectations in our product design, using feature name.  
        Don't rush, ask one question at a time. Don't be too persusive, you want to impress them not persuade them. 

    
        
        Here is description to our app:
        <introduction>
        {introduction}
        </introduction>
        
        You need to guide the conversation to let the user have a good understanding towards our app and fall in love with our app. 
        On the meantime, understand the user's preference in the conversation's directness, formality, emotionally expressives, detailness etc, whatever you think is important to make the user engaed in future conversations. 
        You should achieve these prefernce probes in an implicitly way, but welcome to design your tone to probe these preferences. Never ask what do you prefer explicity. Oberseve how they respond, what they are more interested in to guess their preference. 


    """
    return prompt


conclusion_prompt = "can you summarize user's preference in conversation based on this conversation"


StarterPrompt = GetStartPrompt(introduction)


# Define system message for personality (hidden from user)
system_message = {
    "role": "system",
    "content": StarterPrompt
}


# Initialize message history with system personality if it's not already present
if "messages" not in st.session_state:
    st.session_state["messages"] = [system_message]
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
# If this is the first interaction, generate a dynamic greeting from the AI

    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(
        model="gpt-4o", 
        messages=[system_message],  # Use only the system message for the first greeting
        temperature=0.7  # Adjust temperature for randomness; 0 is deterministic, 1 is more random
    )
    greeting_msg = response.choices[0].message.content
    st.session_state["messages"].append({"role": "assistant", "content": greeting_msg})


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