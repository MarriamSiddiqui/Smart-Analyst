import streamlit as st
from langchain_experimental.agents import create_csv_agent
from langchain_openai import OpenAI
from dotenv import load_dotenv


def main():
    """
    The main function is the entry point of the program.
    It loads environment variables from a .env file, sets up Streamlit's page title and header,
    and then prompts the user to upload a CSV file. If they do so, it asks them what type of query they want to run:
    - Analyze: A simple question about one or more columns in their data (e.g., &quot;What is my average revenue?&quot;)
    - Visualize: A visualization request (e.g., &quot;Show me a bar chart of my revenue by month&quot;)
    - Predict: A prediction request (e.g., &quot;Predict

    :return: A string
    :doc-author: Trelent
    """
    load_dotenv()

    st.set_page_config(page_title="📊 Analyze your business")
    st.header("📊 Analyze your business")

    user_csv = st.file_uploader("Upload CSV file", type="csv")

    if user_csv is not None:
        question_type = st.selectbox(
            "Select Your Query Type",
            ("Analyze", "Visualize", "Predict", "Simple Query"),
            index=None,
            placeholder="Click to select an option",
        )

        user_question = None
        agent = create_csv_agent(OpenAI(temperature=0), user_csv, verbose=True)
        if question_type == "Simple Query":
            user_question = st.text_input("Ask your query")
            # agent = create_csv_agent(OpenAI(temperature=0), user_csv, verbose=True)

            if user_question is not None and user_question != "":
                response = agent.run(user_question)
                st.write(response)
        if question_type == "Analyze":

            user_question = "Write a concise yet clear analysis of the provided data in a professional tone."
            response = agent.run(user_question)
            st.write(response)
        #     user_question = st.text_input("Ask your query")
        # if question_type == "Visualize":
        #     user_question = st.text_input("Ask your query")
        # if question_type == "Predict":
        #     user_question = st.text_input("Ask your query")


if __name__ == "__main__":
    main()
