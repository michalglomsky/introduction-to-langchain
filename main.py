# install the required packages:
# pip install langchain-groq langchain-core python-dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_groq import ChatGroq
import dotenv

dotenv.load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0,
    max_retries=2
)

examples = [
    {
        "input": "What is Earth?",
        "output": "Earth is the third planet from the Sun and the only known planet to support life. \n "
                  "It has a diverse environment, liquid water on its surface, and a protective atmosphere that sustains life."
    },
    {
        "input": "What is Jupiter?",
        "output": "Jupiter is the largest planet in our solar system. \n"
                  "This gas giant is primarily composed of hydrogen and helium, with a prominent Great Red Spot and numerous moons."
    },
    {
        "input": "What is Mars?",
        "output": "Mars, known as the Red Planet, is the fourth planet from the Sun. \n"
                  "It features a thin atmosphere composed mainly of carbon dioxide, vast canyons, and the largest volcano in the solar system, Olympus Mons."
    },
    {
        "input": "What is Neptune?",
        "output": "Neptune, the eighth planet, is known for its deep blue color and supersonic winds.\n "
                  "It is a distant ice giant with a dynamic atmosphere and several moons."
    },
    {
        "input": "What is Pluto?",
        "output": "A dwarf planet in the Kuiper belt, a ring of bodies beyond Neptune. \n"
                  "It was the first and the largest Kuiper belt object to be discovered. \n"
                  "After it was discovered in 1930, it was declared to be the ninth planet from the Sun. \n"
                  "Beginning in the late 20th century, many objects similar to Pluto were discovered in the outer solar system, \n"
                  "and in 2006 the International Astronomical Union (IAU) redefined Pluto as a 'dwarf planet', \n"
                  "which is a new category of solar system objects. In the new classification, Pluto was assigned the number 134340. \n"
                  "Pluto is the largest and second-most-massive known dwarf planet in the Solar System and the ninth-largest and tenth-most-massive known object directly orbiting the Sun."
    },
    {
        "input": "What is Saturn?",
        "output": "Saturn is renowned for its striking ring system. \n"
                  "As a gas giant, it has a composition similar to Jupiter and dozens of moons, with Titan being its largest."
    },
    {
        "input": "What is Uranus?",
        "output": "Uranus is the seventh planet from the Sun and is notable for its blue-green color due to methane in its atmosphere. \n"
                  "It rotates on its side, which results in extreme seasonal variations. Uranus has a faint ring system and 27 known moons."
    },
    {
        "input": "What is Venus?",
        "output": "Venus is the second planet from the Sun and is known for its thick, toxic atmosphere rich in carbon dioxide. \n"
                  "Its surface features include volcanic plains and a runaway greenhouse effect causing extreme surface temperatures."
    },
    {
        "input": "What is Mercury?",
        "output": "Mercury is the smallest planet in the solar system and the closest to the Sun. \n"
                  "It has a heavily cratered surface and a very thin atmosphere, leading to extreme temperature variations."
    }
]

example_template = PromptTemplate.from_template("Q: {input}\nA: {output}")

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_template,
    suffix="Q: {question}\nA:",
    input_variables=["question"],
)

prompt = input("Which planet you want to know about?")

final_prompt = few_shot_prompt.format(question="Explain what is {}? Include in your answer information sucha as: \n"
                                               "Physical characteristics (size, composition, atmosphere); \n"
                                               "Notable features (rings, moons, surface conditions); Scientific or historical significance; \n"
                                               "Fun or surprising facts;".format(prompt))

response = llm.invoke(final_prompt)

print(response.content)
