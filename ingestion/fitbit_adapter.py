import requests
from datetime import date

class FitbitAdapter:
    def __init__(self, access_token: str):
        self.base_url = "https://api.fitbit.com/1/user/-"
        self.headers = {
            "Authorization": f"Bearer {access_token}"
        }

    def get_daily_steps(self, day: str = None) -> dict:
        """
        Fetch daily steps from Fitbit
        """
        if day is None:
            day = date.today().isoformat()

        url = f"{self.base_url}/activities/steps/date/{day}/1d.json"
        response = requests.get(url, headers=self.headers)

        response.raise_for_status()
        data = response.json()

        steps = int(data["activities-steps"][0]["value"])

        return {
            "source": "fitbit",
            "date": day,
            "metric": "steps",
            "value": steps
        }

