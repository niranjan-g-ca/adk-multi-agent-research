def search_tool(query: str) -> str:
    query = query.lower()

    if "electric vehicle" in query or "ev" in query:
        return "Electric vehicles reduce greenhouse gas emissions compared to traditional vehicles."

    elif "battery" in query:
        return "EV battery production involves mining lithium and cobalt, which has environmental impact."

    elif "electricity" in query or "charging" in query:
        return "EV emissions depend on electricity source; renewable energy makes them cleaner."

    elif "recycling" in query:
        return "Battery recycling reduces environmental harm and recovers valuable materials."

    elif "comparison" in query or "vs" in query:
        return "EVs generally have lower lifetime emissions than internal combustion vehicles."

    return "Limited data available, but EVs generally help reduce emissions."
