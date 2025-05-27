from graph import agentic_workflow

def run():
    user_input = input("Enter your query: ")
    result = agentic_workflow.invoke({"input": user_input})
    print("\nFinal Output:")
    print(result)

if __name__ == "__main__":
    run()