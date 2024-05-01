```python
import sys
import traceback
from utils.logging_utils import log_action, log_error

def execute_dynamic_code(code_string, api_key, context):
    """
    Dynamically executes a code snippet provided as a string.

    :param code_string: A string containing the Python code to execute.
    :param api_key: The API key for any external service calls within the code.
    :param context: A dictionary containing any additional context or variables needed for code execution.
    :return: The result of the executed code or an error message.
    """
    try:
        # Prepare the execution environment with the provided context
        exec_environment = globals().copy()
        exec_environment.update(context)
        exec_environment['api_key'] = api_key

        # Execute the code snippet
        exec(code_string, exec_environment)

        # Log the successful execution
        log_action(f"Executed dynamic code: {code_string}")

        # Return the result if any, from the executed code
        return exec_environment.get('result', None)
    except Exception as e:
        # Log the error with traceback
        error_message = f"Error executing dynamic code: {traceback.format_exc()}"
        log_error(error_message)

        # Return the error message
        return {'error': str(e), 'traceback': traceback.format_exc()}

# Example usage:
# result = execute_dynamic_code("result = 'Hello, World!'", api_key, {})
# print(result)  # Output should be 'Hello, World!'
```