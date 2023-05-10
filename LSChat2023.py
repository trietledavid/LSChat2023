import streamlit as st
from streamlit_chat import message
import openai

openai.api_type = "azure"
openai.api_key = "324838fc705f496695205801f33596d2"
openai.api_base = "https://lssupport2.openai.azure.com/"
openai.api_version = "2022-12-01"

st.set_page_config(page_title="LSChat2023", page_icon="💬")

st.markdown("# LSChat2023")
st.markdown('CoE of Healcare and Life Science - An example of using the Azure OpenAI and Python')
st.markdown('For more information drop me a message at **tle216@dxc.com**.')


deployment_name = 'LSChat2'

# generating 2 empty lists to store past and generated value in the conversation

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

user_input = st.text_input("You: ", "", key="input")

if user_input:
    output = openai.Completion.create(
        engine=deployment_name,
        prompt=user_input,
        temperature=1,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=1,
        stop=None)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output["choices"][0]["text"].strip())

if st.session_state['generated']:

    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        message(st.session_state["generated"][i], avatar_style='bottts', key=str(i))
        message(st.session_state['past'][i], avatar_style='big-ears', is_user=True, key=str(i) + '_user')
