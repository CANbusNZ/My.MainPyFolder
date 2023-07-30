import subprocess

# Run a Bash script
result = subprocess.run(["bash", "/path/to/script.sh"], capture_output=True, text=True)

# Print the output
print(result.stdout)
