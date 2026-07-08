from autogen import AssistantAgent
from utility.llm_config import llm_config

def get_notification_agent():
    return AssistantAgent(
        name="NotificationAgent",
        system_message="You are an It notification agent that alerts or escalates unresolved tckets.",
        llm_config=llm_config
    )
