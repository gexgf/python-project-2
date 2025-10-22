import logging
import json

# Konfiguracja loggera
logger = logging.getLogger("user_processor")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter(json.dumps({
    "level": "%(levelname)s",
    "message": "%(message)s",
    "function": "%(funcName)s",
    "time": "%(asctime)s"
}))
handler.setFormatter(formatter)
logger.addHandler(handler)


def process_user(data):
    logger.info(f"Processing user {data.get('id')}", extra={"data": data})
    try:
        user_id = data["id"]
        age = int(data["age"])
        result = {"id": user_id, "adult": age >= 18}
        logger.info("User processed successfully", extra={"result": result})
        return result
    except Exception as e:
        logger.exception("Error while processing user")
        return None


# Symulacja błędu
users = [{"id": 1, "age": "25"}, {"id": 2, "age": None}]
for u in users:
    process_user(u)
