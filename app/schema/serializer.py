def all_dict(tasks):
    return [{**task, "_id": str(task["_id"])} for task in tasks]


def individual_dict(task):
    if not task:
        return {"error": "Task not found"}
    task["_id"] = str(task["_id"])
    return task
