
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from youtube_transcript_api import YouTubeTranscriptApi

def summarise(link):
    unique_id = link.split("=")[-1]
    # get the transcript of the video based on the unique ID
    sub = YouTubeTranscriptApi.get_transcript(unique_id)  
    # get only the "text" parts and join them together, ignoring others like "duration"
    text = " ".join([x['text'] for x in sub])

    PROMPT_TEMPLATE = """
    You are a helpful AI assistent, Please provide a concise summary of the following text, highlighting the main points and key details while keeping the essence of the content intact. Here’s the text: 
    {text}
    summarise the important """

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)  
    prompt = prompt_template.format(text=text)

    model = Ollama(model="llama3.2")  
    summarised_text = model.invoke(prompt)
    return summarised_text
