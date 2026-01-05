from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from langchain_groq import ChatGroq


from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model_name="llama-3.3-70b-versatile" )

def extract(text):
    prompt ='''
    From the below news artical, extract revenue and eps in-JSON format containing the 
    following keys : 'revenue actual' , 'revenue expected' , 'eps_actual' ,'eps_expected' .

    all value must have a unit (Billon or million
    only return the valid JSON not preamble.

    Article
    ======
    {article}
    '''
    pt = PromptTemplate.from_template(prompt)
    global llm
    chain = pt| llm

    response = chain.invoke({'article': text})
    parser = JsonOutputParser()
    try:
        output_json = parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context is too big. Unable to parse the output.")

    return output_json

