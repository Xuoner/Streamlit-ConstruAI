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

# Page title
st.title("Amon AI")

# Sidebar for model selection
st.sidebar.title('🤗💬 Amon Ai Chat')
model = st.sidebar.selectbox(
    "Choose a model to chat with:",
    ("GPT-4", "GPT-3.5", "Another model")
)

st.sidebar.markdown(f"**Selected model:** {model}")


# Sidebar for credentials at the very bottom
st.sidebar.markdown("---")
st.sidebar.markdown("#### Enter your credentials")
if 'EMAIL' in st.secrets and 'PASS' in st.secrets:
    st.sidebar.success('HuggingFace Login credentials already provided!', icon='✅')
    hf_email = st.secrets['EMAIL']
    hf_pass = st.secrets['PASS']
else:
    hf_email = st.sidebar.text_input('Enter E-mail:')
    hf_pass = st.sidebar.text_input('Enter password:', type='password')
    if not (hf_email and hf_pass):
        st.sidebar.warning('Please enter your credentials!', icon='⚠️')
    else:
        st.sidebar.success('Proceed to entering your prompt message!', icon='👉')

# Add social media and contact icons in the sidebar under credentials
st.sidebar.markdown("---")
st.sidebar.markdown("#### Any question? Contact us!")
st.sidebar.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <a href="https://www.linkedin.com/in/yourprofile" target="_blank">
            <img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" alt="LinkedIn" style="width:30px;height:30px;margin:5px;">
        </a>
        <a href="mailto:your-email@example.com" target="_blank">
            <img src="https://banner2.cleanpng.com/20180605/qke/kisspng-computer-icons-email-clip-art-5b1643c0644c28.2686936815281857924108.jpg" alt="Email" style="width:30px;height:30px;margin:5px;">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)



selected2 = streamlit_option_menu.option_menu(None, ["Home", "Projects", 'Settings'], 
    icons=['house', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

# Handle different menu selections
if selected2 == "Home":
    # Display a short introduction text
    st.write("This is an introduction to the amazing Amon Ai project. This introduction could be as long as you want, and could includde pictures, but that's your job to write it not mine.")
    st.image("Logo.png", caption="Logo")

elif selected2 == "Projects":
    manage_projects()
    if "selected_project" in st.session_state:
        render_chatbot(st.session_state.selected_project)
    # st.subheader("Manage Projects")
    
    # # Initialize project list in session state if not present
    # if "projects" not in st.session_state:
    #     st.session_state.projects = {}

    # # Select project
    # selected_project = st.selectbox("Select Project", ["Create New Project"] + list(st.session_state.projects.keys()))

    # if selected_project == "Create New Project":
    #     new_project_name = st.text_input("Enter project name")
    #     if st.button("Create Project") and new_project_name:
    #         st.session_state.projects[new_project_name] = []
    #         st.success(f"Project '{new_project_name}' created successfully!")
    #         st.experimental_rerun()
    # else:
    #     if selected_project:
    #         st.session_state.selected_project = selected_project

    # # Remove project
    # remove_project = st.selectbox("Remove Project", ["Select a Project to Remove"] + list(st.session_state.projects.keys()))
    # if st.button("Remove Project") and remove_project != "Select a Project to Remove":
    #     del st.session_state.projects[remove_project]
    #     st.success(f"Project '{remove_project}' removed successfully!")
    #     st.experimental_rerun()

    #  st.subheader(f"Project: {project_name}")

    # # Initialize chat history for the selected project if not present
    # if project_name not in st.session_state.projects:
    #     st.session_state.projects[project_name] = []

    # # Display chat messages from history on app rerun
    # for message in st.session_state.projects[project_name]:
    #     with st.chat_message(message["role"]):
    #         st.markdown(message["content"])

    # # Accept user input
    # if prompt := st.chat_input("What is up?"):
    #     # Display user message in chat message container
    #     with st.chat_message("user"):
    #         st.markdown(prompt)
    #     # Add user message to chat history
    #     st.session_state.projects[project_name].append({"role": "user", "content": prompt})

    #     # Display assistant response in chat message container
    #     response = response_generator()  # Assume response_generator() returns the assistant's response
    #     with st.chat_message("assistant"):
    #         st.markdown(response)
    #     # Add assistant response to chat history
    #     st.session_state.projects[project_name].append({"role": "assistant", "content": response})


elif selected2 == "Settings":
    # Display basic settings options
    st.subheader("Settings")

    # Example 1: Checkbox for notifications
    notifications_enabled = st.checkbox("Enable Notifications", value=True)
    if notifications_enabled:
        st.write("Notifications are enabled.")
    else:
        st.write("Notifications are disabled.")

    # Example 2: Slider for volume control
    volume_level = st.slider("Volume Control", min_value=0, max_value=100, value=50)
    st.write(f"Current volume level: {volume_level}")

    # Example 3: Radio buttons for theme selection
    theme = st.radio("Select Theme", options=["Light", "Dark"], index=0)
    st.write(f"Selected theme: {theme}")

    # Example 4: Text input for user preferences
    user_preference = st.text_input("Enter Your Preference", "")

    # Example 5: Button for saving settings
    if st.button("Save Settings"):
        st.success("Settings saved successfully!")
