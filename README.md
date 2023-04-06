# Command Injection & Code Execution Sandbox

This project is a web application that provides a sandbox environment for testing and learning about command injection and code execution vulnerabilities. The application is built using FastAPI.

The application provides several endpoints that can be used for testing different types of vulnerabilities.

Each endpoint provides a simple API that can be accessed using standard HTTP methods. The server executes the input and returns the result to the client. The application also provides detailed error messages if the input is invalid or if an error occurs during execution.

This application is intended for educational purposes only and should not be used for malicious purposes. It is designed to help developers and security professionals learn about common vulnerabilities and how to protect against them. Users should be aware that executing arbitrary code or commands on a server can be dangerous and can result in security vulnerabilities.

## Installation:

Install Python: This web application is built using Python, so you'll need to install it if you haven't already. You can download Python from the official website at https://www.python.org/downloads/.

Install dependencies: This project uses several third-party Python packages, including fastapi, uvicorn, and requests. To install these packages, you can use the following command:

```bash
pip install fastapi uvicorn requests
```

Clone the repository: You can clone the repository from Github using the following command:

```bash
git clone https://github.com/TheWation/CiCeSandbox.git
```

Start the server: Once you've installed the dependencies and cloned the repository, you can start the server using the following command:
```bash
uvicorn main:app --reload
```
This will start the server and make it available at http://localhost:8000/.

## Installation With Docker:

### Prerequisites
- Docker installed on your system

### Installation Steps
1. Pull the Docker image from Docker Hub:
```bash
docker pull thewation/cicesandbox
```

2. Run the Docker container:
```bash
docker run -p 8000:8000 thewation/cicesandbox
```

This will start the container and map port 8000 on the host to port 8000 in the container.

3. Access the web application in your browser at `http://localhost:8000`.

## Usage:

Open the application: Once the server is running, you can open the application in your web browser by navigating to http://localhost:8000/.

Choose an endpoint: The application provides several endpoints that can be used for testing different types of vulnerabilities. Choose an endpoint that you'd like to test and click on the endpoint to open the web form.

Submit input: Once you've opened the web form, enter input into the form and submit it to the server. The server will execute the input and return the result to the web browser.

Review output: After submitting the input, the server will return the output of the command or code that was executed. Review the output to see if there are any vulnerabilities or errors in the input.

Note: This application is intended for educational purposes only and should not be used for malicious purposes. It is designed to help developers and security professionals learn about common vulnerabilities and how to protect against them. Users should be aware that executing arbitrary code or commands on a server can be dangerous and can result in security vulnerabilities.

`/rce/execute/{code}`: This endpoint accepts a string of Python code from the client and executes it using the exec() function. This can be used to test for code execution vulnerabilities, where an attacker can craft input that will be executed as code on the system.

`/rce/break/{firstname}`: This endpoint accepts a string from the client and executes it as Python code using the exec() function. The code sets a variable named user_name to a string that contains the client's input. This can be used to test for code injection vulnerabilities, where an attacker can inject malicious Python code that will be executed in the context of the web application.

`/ci/ping/blind/{host}`: This endpoint accepts a hostname or IP address from the client and executes a ping command on the system. This can be used to test for command injection vulnerabilities, where an attacker can inject malicious commands into the input field to execute arbitrary code on the system. The endpoint returns a boolean value indicating whether the ping command was successful.

`/ci/ping/{host}`: This endpoint accepts a hostname or IP address from the client and executes a ping command on the system. This can be used to test for command injection vulnerabilities, where an attacker can inject malicious commands into the input field to execute arbitrary code on the system. The endpoint returns the output of the ping command as a string.
