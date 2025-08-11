import dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import json

# Load environment variables from a .env file
dotenv.load_dotenv()

# Initialize the ChatGroq language model with specified parameters
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.6,
    max_retries=2
)


# 1st tool
@tool("PlanetDistanceSun")
def PlanetDistenceSun(planet_name: str) -> str:
    """This tool should take the name of a planet as input (string)
    and return its approximate distance from the Sun in Astronomical Units (AU)"""
    if "earth" in planet_name.lower():
        return "Earth is approximately 1 AU from the Sun."
    elif "mars" in planet_name.lower():
        return "Mars is approximately 1.5 AU from the Sun."
    elif "jupiter" in planet_name.lower():
        return "Jupiter is approximately 5.2 AU from the Sun."
    elif "pluto" in planet_name.lower():
        return "Pluto is approximately 39.5 AU from the Sun."
    else:
        return f"Information about the distance of {planet_name} from the Sun is not available in this tool."


# 2nd tool
@tool("PlanetRevolutionPeriod")
def PlanetRevolutionPeriod(planet_name: str) -> str:
    """this tool should take the name of a planet as input (string)
    and return its approximate revolution period around the Sun in Earth years;"""
    if "earth" in planet_name.lower():
        return "Earth takes approximately 1 Earth year to revolve around the Sun."
    elif "mars" in planet_name.lower():
        return "Mars takes approximately 1.88 Earth years to revolve around the Sun."
    elif "jupiter" in planet_name.lower():
        return "Jupiter takes approximately 11.86 Earth years to revolve around the Sun."
    elif "pluto" in planet_name.lower():
        return "Pluto takes approximately 248 Earth years to revolve around the Sun."
    else:
        return f"Information about the revolution period of {planet_name} is not available in this tool."


# 3rd tool
@tool("PlanetGeneralInfo")
def PlanetGeneralInfo(planet_name: str) -> str:
    """This tool should take the name of a planet as input (string) and handle general planet queries
    that are not about the planet's distance from the Sun or its revolution period.
    This tool should retrieve information about the planet by performing a similarity search over
    documents in the planets/ directory"""
    # Corrected the conditional logic to check for any known planet
    planets = ["earth", "mars", "jupiter", "pluto","mercury","neptune","saturn","uranus","venus"]
    if any(p in planet_name.lower() for p in planets):
        loader = DirectoryLoader("planets", glob="*.txt", loader_cls=TextLoader)
        documents = loader.load()
        embeddings_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        db = Chroma.from_documents(documents, embeddings_model)
        docs = db.similarity_search(planet_name)
        return docs[0].page_content
    else:
        # Corrected the "not available" message to be relevant
        return f"Additional information for {planet_name} is not available in this tool."

# A list of all three tools
tools_list = [PlanetDistenceSun, PlanetRevolutionPeriod, PlanetGeneralInfo]

model_with_tools = llm.bind_tools(tools_list)

user_query = input()

# Getting to the response:

# 1. Invoke the model to get its decision on which tool to use
first_response = model_with_tools.invoke(user_query)

# 2. Check if the model decided to call a tool
if first_response.tool_calls:
    # Get the details of the first tool call
    tool_call = first_response.tool_calls[0]
    tool_name = tool_call["name"]

    # Create a map to look up the actual tool function from its name
    tool_map = {tool.name: tool for tool in tools_list}

    # 3. Select and invoke the chosen tool to get the string response
    if tool_name in tool_map:
        selected_tool = tool_map[tool_name]
        tool_output_string = selected_tool.invoke(tool_call["args"])

        # 4. Convert the model's `tool_calls` list to a JSON string
        tool_calls_json = json.dumps(first_response.tool_calls)

        # 5. Concatenate the tool's output and the JSON string to match the required format
        final_output = tool_output_string + "\n" + tool_calls_json
        print(final_output)
    else:
        print(f"Error: Model chose a tool named '{tool_name}' which is not available.")
else:
    # If the model didn't use a tool, print its direct text response
    print(first_response.content)
