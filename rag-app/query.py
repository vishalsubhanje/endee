contexts = []

if isinstance(results, list):
    for item in results:
        try:
            # Endee returns list format internally
            if isinstance(item, list) and len(item) >= 2:
                meta = item[1]  # meta is second element
                if isinstance(meta, dict):
                    text = meta.get("text")
                    if text:
                        contexts.append(text)
        except:
            pass

return "\n\n".join(contexts) if contexts else "No relevant context found."