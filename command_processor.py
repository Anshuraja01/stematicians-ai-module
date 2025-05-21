

def simulate_ai_response(command: str) -> str:
    command = command.lower().strip()
    responses = {
        "start irrigation": "Irrigation motor started.",
        "stop irrigation": "Irrigation motor stopped.",
        "check soil": "Soil moisture is 45%.",
        "check weather": "Weather is clear. No rain expected.",
    }
    return responses.get(command, "Unknown command.")
