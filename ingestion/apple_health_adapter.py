class AppleHealthAdapter:
    def __init__(self):
        pass

    def ingest_payload(self, payload: dict) -> list:
        """
        Payload example (from iOS app):
        {
            "date": "2026-02-12",
            "steps": 7200,
            "sleep_hours": 7.1,
            "heart_rate_avg": 68
        }
        """
        date = payload.get("date")

        records = []

        for key, value in payload.items():
            if key == "date":
                continue

            records.append({
                "source": "apple_health",
                "date": date,
                "metric": key,
                "value": value
            })

        return records
