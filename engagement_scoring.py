
class EngagementScorer:

    def __init__(self):
        self.weights = {
            "visual_presence": 0.35,
            "movement": 0.15,
            "inactivity": 0.20,
            "speech_activity": 0.30
        }

    def calculate_score(self, visual_presence,
                        movement, inactivity,
                        speech_activity):

        # Normalize input values between 0 and 100
        visual_presence = max(0, min(100, visual_presence))
        movement = max(0, min(100, movement))
        inactivity = max(0, min(100, inactivity))
        speech_activity = max(0, min(100, speech_activity))

        # Higher inactivity reduces engagement
        score = (
            visual_presence * self.weights["visual_presence"]
            + movement * self.weights["movement"]
            + (100 - inactivity) * self.weights["inactivity"]
            + speech_activity * self.weights["speech_activity"]
        )

        score = round(score, 2)

        if score >= 75:
            level = "High"
        elif score >= 45:
            level = "Moderate"
        else:
            level = "Low"

        return {
            "engagement_score": score,
            "engagement_level": level
        }

    def analyze_session(self, session_data):

        results = []

        for segment in session_data:
            result = self.calculate_score(
                segment["visual_presence"],
                segment["movement"],
                segment["inactivity"],
                segment["speech_activity"]
            )

            results.append({
                "timestamp": segment["timestamp"],
                **result
            })

        return results


if __name__ == "__main__":

    scorer = EngagementScorer()

    session_data = [
        {
            "timestamp": "10:00",
            "visual_presence": 90,
            "movement": 70,
            "inactivity": 10,
            "speech_activity": 80
        },
        {
            "timestamp": "10:15",
            "visual_presence": 60,
            "movement": 40,
            "inactivity": 50,
            "speech_activity": 30
        },
        {
            "timestamp": "10:30",
            "visual_presence": 95,
            "movement": 75,
            "inactivity": 5,
            "speech_activity": 90
        }
    ]

    report = scorer.analyze_session(session_data)

    for item in report:
        print(item)
