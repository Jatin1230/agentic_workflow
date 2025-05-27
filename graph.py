from langgraph.graph import StateGraph
from agents.plan_agent import get_subtasks
from agents.tool_agent import run_tool

# Define schema
class AgentState(dict):
    input: str
    subtasks: str
    current: int
    output: str

def plan_node(state):
    subtasks = get_subtasks(state["input"])
    return {"subtasks": subtasks, "current": 0}

def tool_node(state):
    subtasks = state["subtasks"].split("\n")
    current = state["current"]
    
    # ✅ STOP condition
    if current >= len(subtasks):
        return {"output": state.get("output", "Done")}
    
    subtask = subtasks[current]
    result = run_tool(subtask)
    outputs = state.get("output", "") + f"\nSubtask: {subtask}\nResult: {result}\n"

    return {
        "subtasks": state["subtasks"],
        "current": current + 1,
        "output": outputs
    }

# Setup graph with state schema
sg = StateGraph(state_schema=AgentState)
sg.add_node("plan", plan_node)
sg.add_node("tool_use", tool_node)

sg.set_entry_point("plan")
sg.add_edge("plan", "tool_use")

# ✅ Key line: this tells LangGraph where to stop
sg.set_finish_point("tool_use")

# Do not add edge from tool_use to tool_use anymore
agentic_workflow = sg.compile()
