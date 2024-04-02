# Smart Analyst

This Python application facilitates loading a CSV file and querying its contents using natural language. The application utilizes Language Models (LLMs) to generate responses based on the data within the CSV file, ensuring that responses are relevant to the information present.

## How it Operates

You can interact with the application through different tabs: 'Analyze', 'Explain', 'Seek Advice', and 'Predict'. These tabs provide assistance with analyzing business statistics and strategies.

The application reads the CSV file, processes the data, and employs OpenAI LLMs along with Langchain Agents to address user queries. The CSV agent utilizes various tools to find solutions to questions and then generates suitable responses with the assistance of a LLM.

The graphical user interface (GUI) is built using Streamlit, and Langchain is employed for interacting with the LLM.

## Installation

To install the application, follow these steps:

1. Clone this repository to your local machine.
2. Install the necessary dependencies by running the following command:

    ```
    pip install -r requirements.txt
    ```

3. Additionally, you need to obtain an OpenAI API key and add it to the `.env` file.

## Usage

To utilize the application, execute the `main.py` file using the Streamlit Command-Line Interface (CLI). Ensure that Streamlit is installed before running the application. Run the following command in your terminal:

