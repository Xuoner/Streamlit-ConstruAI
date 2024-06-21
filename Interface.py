import streamlit as st
import random
import time
import os
import streamlit_option_menu

# def manage_projects():
#     st.subheader("Manage Projects")
    
#     # Initialize project list in session state if not present
#     if "projects" not in st.session_state:
#         st.session_state.projects = {}

#     # Select an action: Create, Remove, or Choose
#     action = st.radio("Select Action", ["Create Project", "Choose Project", "Remove Project"], key="action")

#     if action == "Create Project":
#         # Use form to handle submission on Enter key press
#         with st.form(key='create_project_form'):
#             # Input for new project name
#             new_project_name = st.text_input("Enter new project name", key="new_project")
#             # Submit button
#             submit_button = st.form_submit_button("Create Project")
#             if submit_button and new_project_name:
#                 st.session_state.projects[new_project_name] = []
#                 st.session_state.selected_project = new_project_name  # Set the selected project
#                 st.success(f"Project '{new_project_name}' created successfully!")  # Success message
#                 #st.experimental_rerun()
#             elif submit_button and not new_project_name:
#                 st.error("Please enter a valid project name.")
#     elif action == "Choose Project":
#         # Select a project to work on
#         if st.session_state.projects:
#             selected_project = st.selectbox("Choose Project", list(st.session_state.projects.keys()), key="choose_project")
#             if selected_project != "Select a Project":
#                 st.session_state.selected_project = selected_project
#     elif action == "Remove Project":
#         # Option to remove an existing project
#         if st.session_state.projects:
#             remove_project = st.selectbox("Remove Project", list(st.session_state.projects.keys()), key="remove_project")
#             if st.button("Remove Project"):
#                 if remove_project != "Select a Project to Remove":
#                     del st.session_state.projects[remove_project]
#                     st.success(f"Project '{remove_project}' removed successfully!")
#                     st.experimental_rerun()
#                 else:
#                     st.error("Please select a valid project to remove.")

# # Function to render the chatbot for a selected project
# def render_chatbot(project_name):
#     st.subheader(f"Project: {project_name}")

#     # Initialize chat history for the selected project if not present
#     if project_name not in st.session_state.projects:
#         st.session_state.projects[project_name] = []

#     # Display chat messages from history on app rerun
#     for message in st.session_state.projects[project_name]:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     # Accept user input
#     if prompt := st.chat_input("What is up?"):
#         # Display user message in chat message container
#         with st.chat_message("user"):
#             st.markdown(prompt)
#         # Add user message to chat history
#         st.session_state.projects[project_name].append({"role": "user", "content": prompt})

#         # Display assistant response in chat message container
#         with st.chat_message("assistant"):
#             response = st.write_stream(response_generator())
#         # Add assistant response to chat history
#         st.session_state.projects[project_name].append({"role": "assistant", "content": response})

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

### Configuration de la page
st.set_page_config(page_title="Assitant AmonAI", page_icon="Logo.png", layout="wide", initial_sidebar_state="expanded", menu_items=None)

### Left Sidebar centering
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

st.markdown(
    """
    <style>
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

#Logo image on sidebar
st.sidebar.image("Logo.png", width=100)

# Sidebar Title
st.sidebar.title('👷💬 Assistant AmonAI')

# Project Selection
project = st.sidebar.selectbox(
    "Sélectionnez un projet:",
    ("Projet A57 NGE", "Projet A57 NGE - Use Case")
)

# Profile sidebar
if 'profile_visible' not in st.session_state:
    st.session_state['profile_visible'] = True

def disconnect():
    st.session_state['profile_visible'] = False

if st.session_state['profile_visible']:
# Add profile picture, name, and function
    st.sidebar.markdown("---")
    
    st.sidebar.markdown(f'<div style="margin-bottom: 15px;text-align: center;"><strong>Projet Actuel:</strong> {project}</div>', unsafe_allow_html=True)

    st.sidebar.image("pp.png", output_format="auto", width=100)
    # Centered name and function
    st.sidebar.markdown('<div class="center-text"><h3>Alexandre Hoang</h3></div>', unsafe_allow_html=True)
    #st.sidebar.markdown('<div class="center-text"><h5>Directeur des Travaux</h5></div>', unsafe_allow_html=True)
    st.sidebar.markdown('<div style="font-size: 14px; font-weight: normal; margin-bottom: 15px; text-align: center;">Directeur des Travaux</div>', unsafe_allow_html=True)


    button_container = st.sidebar.empty()
    with button_container:
        col1, col2 = st.columns(2)
        col1.button('Paramètres')

        col2.button('Se Déconnecter')

# Sidebar contacts
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

#### MAIN PAGE

## markdowns for centering
st.markdown(
    """
    <style>
         [data-testid="stImage"] {
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
        
    </style>
    """, 
    unsafe_allow_html=True
)
### Logo
st.image("Logo.png", width = 170)

### Functions to handle conversations history through page actualisation
def find_conversation(name):
    for conv in st.session_state.conversations:
        if conv["name"] == name:
            return conv
    return None

def start_new_conversation():
    st.session_state.messages = []
    st.session_state.current_conversation = None

def on_option_change(key):
    for conversation in st.session_state.conversations:
        if conversation['name'] == st.session_state["choice"]:
            st.session_state.current_conversation = conversation['name']
            st.session_state.messages = conversation['history']
            break
    st.session_state['menu_option'][1] = 1
    st.rerun()

### Menus and options for chat
if 'menu_option' not in st.session_state:
       st.session_state['menu_option'] =[0,1]
if "selected2" not in st.session_state:
    st.session_state['selected2'] = "Chat"
st.session_state['selected2'] = streamlit_option_menu.option_menu(None, ["Conversations", "Chat"], 
    icons=["list-task", "chat"], 
    menu_icon="cast", default_index=st.session_state['menu_option'][1], orientation="horizontal")
if "current_conversation" not in st.session_state:
    st.session_state.current_conversation = None
if "conversations" not in st.session_state:
    st.session_state.conversations = []


# Handle different menu selections

# Si on choisit l'onglet CONVERSATIONS
if st.session_state['selected2'] == "Conversations":
    
    st.session_state['menu_option'][1]=0
    if not st.session_state.conversations:
        st.warning("Aucune conversation n'a encore été démarrée.")
    else:
        st.write("Sélectionnez une conversation")
        # for conversation in st.session_state.conversations:
        #     if st.button(conversation['name']):
        #         st.session_state.current_conversation = conversation['name']
        #         st.session_state.messages = conversation['history']
        conversation_names = [conv['name'] for conv in st.session_state.conversations]
        if st.session_state.current_conversation:
            default_index = conversation_names.index(st.session_state.current_conversation)
        else:
            default_index = 0
        col1, col2, col3 = st.columns(3)
        with col1:
            convo = streamlit_option_menu.option_menu(None, conversation_names, default_index=default_index, key = "choice", on_change=on_option_change)
        for conversation in st.session_state.conversations:
            if conversation['name'] == convo:
                st.session_state.current_conversation = conversation['name']
                st.session_state.messages = conversation['history']
                break
    if st.button("Nouvelle Conversation"):    
        start_new_conversation()
        st.session_state['menu_option'][1] = 1
        st.rerun()


# SI ON CHOISIT l"ONGLET CHAT --> C"EST SEULEMENT ICI QUE LE TEXTE DOIT ETRE CHANGÉ
elif st.session_state['selected2'] == "Chat":
    # Initialisation de l'historique
    st.session_state['menu_option'][1]=1
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Affichage des messages stockés dans l'historique de conversation
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Cette partie correspond au chat --> C'est ici que le texte en réponse doit etre ajouté
    if prompt := st.chat_input("Posez votre question"):

        # Afficher le prompt utilisateur
        with st.chat_message("user"):
            st.markdown(prompt)

        # Enregistrer ce prompt
        st.session_state.messages.append({"role": "user", "content": prompt})

        # REPONSE DU CHAT BOT --> C'est cette partie qui doit contenir la reponse
        # Ici, l'assistant attend 5 secondes en faisant apparaitre un logo de chargement, c'est simplement pour montrer, j'imagine qu'un while... \
        # jusqu'a ce que la reponse soit chargé suffira
        with st.chat_message("assistant"):
            with st.spinner('Veuillez patienter quelques secondes, une réponse arrive !'):
                time.sleep(5)
            # Cette ligne contient la reponse (actuellement c'est du texte aleatoire)
            # J'utilise un stream (https://docs.streamlit.io/develop/api-reference/write-magic/st.write_stream) car cela permet d'avoir l'effect machine a ecrire (le bot ecrit devant nous)
            # Si pas moyen de convertir en stream ou trop chiant, utiliser st.write a la place de st.write_stream, mais le texte apparait d'un coup.
            # La fonction response_generator (ligne 76) illustre comment convertir en stream. 
            response = st.write_stream(response_generator())

        # gestion de l'historique et sauvegarde
        st.session_state.messages.append({"role": "assistant", "content": response})
        if st.session_state.current_conversation:
            conversation = find_conversation(st.session_state.current_conversation)
            if conversation:
                conversation['history'] = st.session_state.messages
            else:
                st.session_state.conversations.append({
                    "name": st.session_state.current_conversation,
                    "history": st.session_state.messages
                })
        else:
            st.session_state.current_conversation = st.session_state.messages[0]['content']
            st.session_state.conversations.append({
                "name": st.session_state.current_conversation,
                "history": st.session_state.messages
            })

if st.session_state['menu_option'][0] !=st.session_state['menu_option'][1]:
       st.session_state['menu_option'][0] =st.session_state['menu_option'][1]
       st.rerun()