import os

# Read the name from the WHO_TO_GREET environment variable.
# If it is not set, use the default value.
name = os.environ.get("WHO_TO_GREET", "GitHub Actions Student")

print(f"Hello {name}!")
print("This program is running inside GitHub Actions.")
