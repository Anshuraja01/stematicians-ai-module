
import json
from command_processor import simulate_ai_response

def main():
    # Load command from file
    try:
        with open("commands.json", "r") as f:
            data = json.load(f)
            command = data.get("command", "")
    except Exception as e:
        print(f"Error reading command file: {e}")
        return

    # Process command
    result = simulate_ai_response(command)

    # Write to output_log.txt
    try:
        with open("output_log.txt", "w") as f:
            f.write(f"Command parsed: {command}\n")
            f.write(f"{result}\n")
        print("Command processed successfully.")
    except Exception as e:
        print(f"Error writing output: {e}")

if __name__ == "__main__":
    main()
