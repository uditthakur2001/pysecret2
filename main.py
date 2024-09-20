import os
import sqlite3

# Example of credentials in code
DATABASE_URL = "sqlite:///example.db"
SECRET_KEY = "superSecretKey1234"
API_KEY = "apikey1234567890"

def connect_to_database():
    conn = sqlite3.connect(DATABASE_URL)
    return conn

def main():
    print(f"Using API Key: {API_KEY}")
    connect_to_database()

if __name__ == "__main__":
    main()
