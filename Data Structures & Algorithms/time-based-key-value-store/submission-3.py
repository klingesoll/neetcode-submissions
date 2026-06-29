class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []

        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""

        answer = ""

        for value, time in self.keyStore[key]:
            if time <= timestamp:
                answer = value
            else:
                break

        return answer