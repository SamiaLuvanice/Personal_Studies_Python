gameName = "The Legend of Zelda: Breath of the Wild"
gameDescription = """
An open-world action-adventure game developed and published by Nintendo.
"""

print(gameName.upper())  # Convert to uppercase
print(gameName.lower())  # Convert to lowercase
print(gameName.title())  # Convert to title case
print(gameName.capitalize())  # Capitalize the first letter
print(gameName.center(50, '-'))  # Center the string with padding
print(gameName.find("Z"))  # Find the index of a substring
print(gameDescription.count("o"))  # Count occurrences of a substring
print(gameDescription.replace("Nintendo", "Nintendo Switch"))  # Replace a substring
print(gameDescription.strip())  # Remove leading and trailing whitespace
print(gameDescription.split())  # Split the string into a list of words