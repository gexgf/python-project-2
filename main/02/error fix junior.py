def process_user(data):
    print("Processing user...")  # debug
    print(data)  # debug
    user_id = data["id"]
    age = int(data["age"])
    print("User processed!")  # debug
    return {"id": user_id, "adult": age >= 18}


# Symulacja błędu
users = [{"id": 1, "age": "25"}, {"id": 2, "age": None}]
for u in users:
    result = process_user(u)
    print(result)
