from langgraph.graph import StateGraph, START, END

from graph.state import AgentState

from agents.analyzer import analyzer_node
from agents.meme_search import meme_search_node
from agents.caption import caption_node
from agents.sarcasm import sarcasm_node

from graph.memory_nodes import (
    memory_loader_node,
    memory_saver_node
)


def meme_decision(state: AgentState):

    if state["meme_found"]:
        return "caption"

    return "sarcasm"


def build_workflow():

    graph = StateGraph(AgentState)

    # Nodes

    graph.add_node(
        "analyzer",
        analyzer_node
    )

    graph.add_node(
        "meme_search",
        meme_search_node
    )

    graph.add_node(
        "caption",
        caption_node
    )

    graph.add_node(
        "sarcasm",
        sarcasm_node
    )

    graph.add_node(
    "memory_loader",
    memory_loader_node
    )


    graph.add_node(
        "memory_saver",
        memory_saver_node
    )

    # Flow
    graph.add_edge(
    START,
    "memory_loader"
    )


    graph.add_edge(
        "memory_loader",
        "analyzer"
    )

    graph.add_edge(
        "analyzer",
        "meme_search"
    )


    graph.add_conditional_edges(

        "meme_search",

        meme_decision,

        {

            "caption": "caption",

            "sarcasm": "sarcasm"

        }

    )


    graph.add_edge(
    "caption",
    "memory_saver"
    )


    graph.add_edge(
        "sarcasm",
        "memory_saver"
    )


    graph.add_edge(
        "memory_saver",
        END
    )
    
    return graph.compile()