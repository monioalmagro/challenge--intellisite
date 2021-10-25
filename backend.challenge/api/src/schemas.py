def detectionEntity(item) -> dict:
    return {
        "year": item["Year"],
        "make": item["Make"],
        "model": item["Model"],
        "category": item["Category"]
    }


def detectionsEntity(entity) -> list:
    return [detectionEntity(item) for item in entity]
