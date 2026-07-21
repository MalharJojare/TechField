from graph.state import AgentState

from services.giphy_service import search_giphy


def score_meme(title: str, keywords: list[str]):

    title = title.lower()

    score = 0

    for keyword in keywords:

        if keyword.lower() in title:
            score += 1

    return score


def meme_search_node(state: AgentState):

    keywords = state["keywords"]

    queries = []


    # Full query but limited
    queries.append(
        " ".join(keywords[:3])
    )


    # Smaller combinations
    if len(keywords) >= 2:
        queries.append(
            " ".join(keywords[:2])
        )


    queries.append(
        keywords[0]
    )
    all_memes = []

    seen = set()

    for query in queries:

        results = search_giphy(query)

        for meme in results:

            if meme["id"] not in seen:

                seen.add(meme["id"])

                all_memes.append(meme)

    if not all_memes:

        state["meme_found"] = False

        return state

    ranked = sorted(

        all_memes,

        key=lambda meme: score_meme(
            meme["title"],
            keywords
        ),

        reverse=True

    )

    best = ranked[0]

    state["meme_found"] = True

    state["meme_title"] = best["title"]

    state["meme_url"] = best["url"]

    return state