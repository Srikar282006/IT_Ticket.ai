from autogen import AssistantAgent
from utility.llm_config import llm_config
from tools.knowledge_base_tool import search_similar_solution
def get_knowledge_base_agent():
    knowledge_agent=AssistantAgent(
        name="knowlegeBaseAgent",
        system_message=(
            "You are It support assistant that retrieves solutions to user issues."
            "Always call the 'search_similar_solution' tool with the query to get a matching solution."
            "Afetr calling, summarize the top solution and respond with TERMINAL",
        ),
        llm_config=llm_config,
        code_execution_config={"use_docker":False}
    )
    
    knowledge_agent.register_for_llm(
        name="search_similar_solution",
        description="Searches for top IT solutions frm a knowledge base using a vector similarity search. Accept query and top_k"
    )(search_similar_solution)

    knowledge_agent.register_for_execution(
        name="search_similar_solution"
    )(search_similar_solution)
    
    return knowledge_agent