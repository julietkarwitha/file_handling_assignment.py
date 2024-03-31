try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("Line 1: Hello, world!\n")
        file.write("Line 2: 12345\n")
        file.write("Line 3: Python is awesome!\n")
    
    # File Reading and Display
    print("Contents of my_file.txt:")
    with open("my_file.txt", "r") as file:
        for line in file:
            print(line.strip())
    
    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("Line 4: Adding more text...\n")
        file.write("Line 5: 67890\n")
        file.write("Line 6: Python file handling is fun!\n")

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Script execution completed.")