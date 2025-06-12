from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../.env")  # Adjust path as needed
print(os.getenv("API_KEY"))# Example of using an environment variable