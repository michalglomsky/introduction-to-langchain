# 🪐 Introduction to LangChain: A Conversational Planet AI

This project serves as a hands-on introduction to **LangChain**, demonstrating how to build a sophisticated conversational AI agent capable of answering questions about planets. The agent leverages Large Language Models (LLMs), custom tools, and a vector database to provide accurate and context-aware responses.

You'll learn the core concepts of LangChain by building a system that can:
- Understand a user's query.
- Decide which tool to use for a specific question.
- Retrieve information from a local knowledge base.
- Generate a coherent answer.

## ✨ Features

- **Tool-Based Architecture**: The agent is equipped with custom tools to answer specific questions about a planet's distance from the sun and its revolution period.
- **Retrieval-Augmented Generation (RAG)**: For general questions, the agent uses a `PlanetGeneralInfo` tool that performs a similarity search over a local `Chroma` vector database to find relevant information from text files.
- **LLM Integration**: Uses the high-speed `Groq` inference engine with a Llama 3 model to power the conversation.
- **LangChain Expression Language (LCEL)**: The entire workflow is built as a composable chain using LCEL (`|`), making the code modular and easy to read.
- **Dynamic Tool-Calling**: The LLM automatically decides when to call a function (a "tool") based on the user's query, demonstrating a core concept of agentic AI.

## 🛠️ Technologies Used

*   **Core**: Python
*   **LLM Orchestration**: LangChain
*   **LLM Provider**: Groq (with Llama 3)
*   **Embeddings**: HuggingFace `sentence-transformers`
*   **Vector Database**: Chroma

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python 3.8+
- A Groq API Key

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/michalglomsky/introduction-to-langchain.git
    cd introduction-to-langchain
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```sh
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up your environment:**
    - Create a file named `.env` in the root of the project directory.
    - Add your Groq API key to this file:
      ```
      GROQ_API_KEY="your_api_key_here"
      ```

5.  **Create the knowledge base:**
    - Create a folder named `planets` in the root of the project directory.
    - Inside the `planets` folder, create text files for each planet (e.g., `earth.txt`, `mars.txt`).
    - Add some facts to each file. For example, in `mars.txt`:
      ```
      Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System, being larger than only Mercury. Mars is a terrestrial planet with a thin atmosphere, and has a crust primarily composed of elements similar to Earth's crust.
      ```

## 🏃‍♀️ Usage

Once the setup is complete, you can run the script and start asking questions.

1.  **Run the script:**
    ```sh
    python "introduction to langchain.py"
    ```

2.  **Ask a question:**
    The script will wait for your input. Try different types of questions to see how the agent responds.

    **Example 1: Using a specific tool**
    ```
    > How long does it take for Jupiter to revolve around the Sun?
    Jupiter takes approximately 11.86 Earth years to revolve around the Sun.
    ```

    **Example 2: Using the RAG tool**
    ```
    > Tell me something about Mars.
    Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System, being larger than only Mercury. Mars is a terrestrial planet with a thin atmosphere, and has a crust primarily composed of elements similar to Earth's crust.
    ```

    **Example 3: A general conversation**
    ```
    > Hello, what can you do?
    I can answer questions about planets! You can ask me about their distance from the sun, their revolution period, or just general facts.
    ```

## 📄 License

This project is licensed under the MIT License.

---

Created by Michał Głomski

```

### New File: `c:\Users\micha\Desktop\CV\requirements.txt`

This file lists all the Python packages your project depends on, making it easy for anyone to install the correct dependencies.

```diff
--- /dev/null
++++ b/c:\Users\micha\Desktop\CV\requirements.txt
@@ -0,0 +1,8 @@
+python-dotenv
+langchain
+langchain-groq
+langchain-chroma
+langchain-huggingface
+sentence-transformers
+groq
+chromadb

```

These files will give your GitHub repository a professional and informative structure, making it easy for visitors to understand your work and get it running quickly.

<!--
[PROMPT_SUGGESTION]Can you explain the role of the `@chain` decorator in the `call_tool` function?[/PROMPT_SUGGESTION]
[PROMPT_SUGGESTION]How could I add a new tool to this agent for checking a planet's number of moons?[/PROMPT_SUGGESTION]
-->
