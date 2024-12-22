import pyodbc
import socket

def test_connection():
    # Get local machine name and IP
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    print(f"Local hostname: {hostname}")
    print(f"Local IP: {local_ip}\n")
    
    # Try different server specifications
    server_options = [
        local_ip,       # Your machine's IP
        hostname,       # Your machine's hostname
        'localhost',    # Local
        '10.5.0.2',    # Your specific IP
        'ALTAY'        # Your server name
    ]
    
    database = 'flask_app'
    username = 'ibrhm'
    password = '12345'

    for server in server_options:
        print(f"\nTrying server: {server}")
        conn_str = (
            f'DRIVER={{ODBC Driver 18 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password};'
            f'TrustServerCertificate=yes;'
            f'Encrypt=no;'
            f'Timeout=30;'
        )
        
        print(f"Connection string:\n{conn_str.replace(password, '****')}")
        
        try:
            print("Attempting connection...")
            conn = pyodbc.connect(conn_str)
            print(f"Connection successful to {server}!")
            cursor = conn.cursor()
            cursor.execute("SELECT @@SERVERNAME, @@VERSION")
            row = cursor.fetchone()
            print(f"Server Name: {row[0]}")
            print(f"SQL Version: {row[1]}")
            conn.close()
            return  # Exit after first successful connection
        except pyodbc.Error as e:
            print(f"Failed to connect to {server}:")
            print(f"Error: {str(e)}")
            continue

if __name__ == "__main__":
    test_connection() 