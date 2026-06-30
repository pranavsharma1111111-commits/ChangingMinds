class ResponseEvaluator:

    def evaluate(self, response: str):

        response = response.lower()

        if "i'll do my homework" in response or "i will do my homework" in response:
            return {
                "mission_complete": True,
                "conversation_end": True,
                "agreement_detected": True,
                "reason": "Character agreed to do homework."
            }

        return {
            "mission_complete": False,
            "conversation_end": False,
            "agreement_detected": False,
            "reason": "Mission still in progress."
        }