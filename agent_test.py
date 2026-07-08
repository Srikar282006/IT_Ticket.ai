from autogen import UserProxyAgent
from agents.classifier_agent import get_classifier_agent
from utility.llm_config import llm_config
from pprint import pprint

print("========== LLM CONFIG ==========")
pprint(llm_config)
print("================================")

sample_tickets = [
    "The VPN is not connecting since after afternoon"
]


def get_user_agent():
    return UserProxyAgent(
        name="User",
        human_input_mode="NEVER",
        code_execution_config=False,
    )


def run_test():
    print("\nCreating User Agent...")
    user = get_user_agent()

    print("Creating Classifier Agent...")
    classifier = get_classifier_agent()

    print("Agents created successfully.\n")

    for ticket in sample_tickets:
        print(f"Ticket: {ticket}")

        try:
            response = user.initiate_chat(
                recipient=classifier,
                message=f"Classify this ticket: {ticket}",
                max_turns=1,
            )

            print("\nChat completed successfully.")
            print(response)

        except Exception as e:
            print("\nERROR OCCURRED")
            print(type(e).__name__)
            print(e)
            raise


if __name__ == "__main__":
    print("Starting agent_test.py...\n")
    run_test()