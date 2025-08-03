# src/utils/payloads.py

class PayloadBuilder:
    def __init__(self):
        self.payload = {}

    def add(self, key, value):
        self.payload[key] = value  # מוסיף מפתח וערך ל־payload
        return self  # מחזיר את עצמו כדי לאפשר ש chaining

    def build(self):
        return self.payload  # מחזיר את המילון המלא
