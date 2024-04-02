import streamlit as st
from langchain_experimental.agents import create_csv_agent
from langchain_openai import OpenAI
from dotenv import load_dotenv


def main():
    load_dotenv()
    st.set_page_config(page_title="📊 Analyze your business")
    st.header("📊 Analyze your business")

    # page_bg_img = '''
    #     <style>
    #     body {
    #     background-image: url("https://unsplash.com/photos/business-visual-data-analyzing-technology-by-creative-computer-software-ZJKfQ8Ber7E");
    #     background-size: cover;
    #     }
    #     </style>
    #     '''

    # st.markdown(page_bg_img, unsafe_allow_html=True)

    user_csv = st.file_uploader("Upload CSV file", type="csv")

    if user_csv is not None:
        agent = create_csv_agent(OpenAI(temperature=0), user_csv, verbose=True)

        user_question = st.text_input("Ask a question")

        if user_question is not None and user_question != "":
            response = agent.run(user_question)
            st.write(response)


if __name__ == "__main__":
    main()
