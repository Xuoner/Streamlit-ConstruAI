import streamlit as st
import random
import time
import os
import streamlit_option_menu

def manage_projects():
    st.subheader("Manage Projects")
    
    # Initialize project list in session state if not present
    if "projects" not in st.session_state:
        st.session_state.projects = {}

    # Select an action: Create, Remove, or Choose
    action = st.radio("Select Action", ["Create Project", "Choose Project", "Remove Project"], key="action")

    if action == "Create Project":
        # Use form to handle submission on Enter key press
        with st.form(key='create_project_form'):
            # Input for new project name
            new_project_name = st.text_input("Enter new project name", key="new_project")
            # Submit button
            submit_button = st.form_submit_button("Create Project")
            if submit_button and new_project_name:
                st.session_state.projects[new_project_name] = []
                st.session_state.selected_project = new_project_name  # Set the selected project
                st.success(f"Project '{new_project_name}' created successfully!")  # Success message
                #st.experimental_rerun()
            elif submit_button and not new_project_name:
                st.error("Please enter a valid project name.")
    elif action == "Choose Project":
        # Select a project to work on
        if st.session_state.projects:
            selected_project = st.selectbox("Choose Project", list(st.session_state.projects.keys()), key="choose_project")
            if selected_project != "Select a Project":
                st.session_state.selected_project = selected_project
    elif action == "Remove Project":
        # Option to remove an existing project
        if st.session_state.projects:
            remove_project = st.selectbox("Remove Project", list(st.session_state.projects.keys()), key="remove_project")
            if st.button("Remove Project"):
                if remove_project != "Select a Project to Remove":
                    del st.session_state.projects[remove_project]
                    st.success(f"Project '{remove_project}' removed successfully!")
                    st.experimental_rerun()
                else:
                    st.error("Please select a valid project to remove.")

# Function to render the chatbot for a selected project
def render_chatbot(project_name):
    st.subheader(f"Project: {project_name}")

    # Initialize chat history for the selected project if not present
    if project_name not in st.session_state.projects:
        st.session_state.projects[project_name] = []

    # Display chat messages from history on app rerun
    for message in st.session_state.projects[project_name]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.projects[project_name].append({"role": "user", "content": prompt})

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator())
        # Add assistant response to chat history
        st.session_state.projects[project_name].append({"role": "assistant", "content": response})

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)
# current_dir = os.path.dirname(__file__)
# logo_path = os.path.join(current_dir, "Logo.png")
# pp_path = os.path.join(current_dir, "pp.png")
st.set_page_config(page_title="Assitant AmonAI", page_icon="Logo.png", layout="wide", initial_sidebar_state="expanded", menu_items=None)

st.markdown(
    """
    <style>
        [data-testid="stSidebar"] [data-testid="stImage"] {
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
        [data-testid="stSidebar"] .center-text {
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
    """, 
    unsafe_allow_html=True
)

st.sidebar.image("Logo.png", width=100)
# Sidebar for model selection
st.sidebar.title('👷💬 Assistant AmonAI')
project = st.sidebar.selectbox(
    "Sélectionnez un projet:",
    ("Projet A57 NGE", "Projet A57 NGE - Use Case")
)

st.sidebar.markdown(f"**Projet Actuel:** {project}")


if 'profile_visible' not in st.session_state:
    st.session_state['profile_visible'] = True

def disconnect():
    st.session_state['profile_visible'] = False

if st.session_state['profile_visible']:
# Add profile picture, name, and function
    st.sidebar.markdown("---")
    st.sidebar.image("pp.png", output_format="auto", width=170)
    # Centered name and function
    st.sidebar.markdown('<div class="center-text"><h3>Alexandre Hoang</h3></div>', unsafe_allow_html=True)
    st.sidebar.markdown('<div class="center-text"><h4>Directeur des Travaux</h4></div>', unsafe_allow_html=True)

st.sidebar.markdown(
    """
    <style>
        .sidebar-buttons {
            display: flex;
            justify-content: space-between;
        }
        .sidebar-buttons button {
            width: 48%;
            border: none;
            padding: 4px;
            font-size: 12px;
            cursor: pointer;
        }
        .sidebar-buttons button:hover {
            background-color: #e0e0e0;
        }
    </style>
    <div class="sidebar-buttons">
        <button onclick="document.querySelector('[aria-label=Settings]').click()">Settings</button>
        <button onclick="document.querySelector('[aria-label=Disconnect]').click()">Disconnect</button>
    </div>
    """, 
    unsafe_allow_html=True
)
st.sidebar.markdown("---")
st.sidebar.markdown('<div class="center-text"><h4>Des questions? Nous contacter :</h4></div>', unsafe_allow_html=True)
st.sidebar.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <a href="https://www.linkedin.com/in/yourprofile" target="_blank">
            <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" alt="LinkedIn" style="width:30px;height:30px;margin:5px;">
        </a>
        <a href="mailto:your-email@example.com" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/fr/a/a7/Mail_%28Apple%29_logo.png" alt="Email" style="width:30px;height:30px;margin:5px;">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# current_dir = os.path.dirname(__file__)
# logo_path = os.path.join(current_dir, "Logo.png")

col1, col2, col3 = st.columns(3)
with col2: 
    st.image("Logo.png")








selected2 = streamlit_option_menu.option_menu(None, ["Conversations", "Chat"], 
    icons=["list-task", "chat"], 
    menu_icon="cast", default_index=1, orientation="horizontal")

if "conversations" not in st.session_state:
    st.session_state.conversations = []

# Handle different menu selections
if selected2 == "Conversations":
    if not st.session_state.conversations:
        st.warning("No conversations available. Start a new one in the Chat mode.")
    else:
        st.write("Select one of the conversations previously done with the chatbot:")
        # Display list of conversations



elif selected2 == "Chat":
    if "messages" not in st.session_state:
        st.session_state.messages = []
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("posez votre question"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator())
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    #st.session_state.conversations.append({"name": st.session_state.messages['content'], "history" : st.session_state.messages})