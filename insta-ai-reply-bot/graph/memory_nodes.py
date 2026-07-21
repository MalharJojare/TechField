from graph.state import AgentState

from memory.repository import (
    get_conversation_history,
    save_conversation
)



def memory_loader_node(
    state: AgentState
):

    history = get_conversation_history(
        state["user_id"]
    )


    state["conversation_history"] = history


    return state



def memory_saver_node(
    state: AgentState
):

    save_conversation(

        user_id=state["user_id"],

        message=state["message"],

        response=state["final_reply"]

    )


    return state