from daytona import CreateSandboxFromImageParams, Daytona, DaytonaConfig, Resources


# Using environment variables (DAYTONA_API_KEY, DAYTONA_API_URL, DAYTONA_TARGET)
# daytona = Daytona()
# Using explicit configuration
config = DaytonaConfig(api_key="", api_url="https://app.daytona.io/api", target="us")
daytona = Daytona(config)
params = CreateSandboxFromImageParams(
    image="",
    # image=Image.debian_slim("3.12"),
    public=True,
    labels=None,
    env_vars={
        "CHROME_PERSISTENT_SESSION": "true",
        "RESOLUTION": "1024x768x24",
        "RESOLUTION_WIDTH": "1024",
        "RESOLUTION_HEIGHT": "768",
        "VNC_PASSWORD": "123456",
        "ANONYMIZED_TELEMETRY": "false",
        "CHROME_PATH": "",
        "CHROME_USER_DATA": "",
        "CHROME_DEBUGGING_PORT": "9222",
        "CHROME_DEBUGGING_HOST": "localhost",
        "CHROME_CDP": "",
    },
    resources=Resources(
        cpu=1,
        memory=1,
        disk=1,
    ),
    auto_stop_interval=15,
    auto_archive_interval=24 * 60,
)
# Create the sandbox
sandbox = daytona.create(params)
print(f"Sandbox created with ID: {sandbox.id}")


# from daytona import Daytona

# def main():
#     # Initialize the SDK (uses environment variables by default)
#     daytona = Daytona(config)

#     # Create a new sandbox
#     sandbox = daytona.create()

#     # Execute a command
#     response = sandbox.process.exec("echo 'Hello, World!'")
#     print(response.result)

# if __name__ == "__main__":
#     main()
# from daytona import Daytona, DaytonaConfig

# Define the configuration

# config = DaytonaConfig(api_key="")

# # Initialize the Daytona client

# daytona = Daytona(config)

# # Create the Sandbox instance

# sandbox = daytona.create()

# # Run the code securely inside the Sandbox

# response = sandbox.process.code_run('print("Hello World from code!")')
# if response.exit_code != 0:
#   print(f"Error: {response.exit_code} {response.result}")
# else:
#     print(response.result)

# Clean up

# sandbox.delete()
