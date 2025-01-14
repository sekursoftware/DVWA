# Intentionally Vulnerable Code: Do not use in production!
import sqlite3
import os

def authenticate_user(username, password):
    # SQL Injection Vulnerability
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)  # User input is directly injected into the query
    user = cursor.fetchone()
    conn.close()
    if user:
        return "Authentication successful!"
    else:
        return "Authentication failed!"

def insecure_file_read(file_path):
    # Path Traversal Vulnerability
    with open(file_path, 'r') as file:
        return file.read()

def insecure_environment_access():
    # Potential exposure of sensitive information
    secret_key = os.environ.get('SECRET_KEY')
    print(f"Secret key: {secret_key}")  # Leaks sensitive data

# Example usage
if __name__ == "__main__":
    # 1. SQL Injection Example
    print(authenticate_user("admin", "' OR '1'='1"))

    # 2. Path Traversal Example
    print(insecure_file_read("../../etc/passwd"))

    # 3. Environment Variable Exposure
    insecure_environment_access()
