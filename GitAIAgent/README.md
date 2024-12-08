# GitAI Agent

GitAI Agent is an AI-powered assistant that can execute Git commands through natural language instructions. It uses OpenAI's language model and LangChain's agent framework to interpret user requests and perform Git operations.

## Features
- Executes Git commands directly in the shell
- Uses language model as a reasoning engine to determine which actions to take and in which order
- Agent can interpret error messages and take actions on its own

## Prerequisites
- OpenAI API key
- Git installed and configured on your system

## Setup
1. Install Dependencies
   ```
   pip install langchain openai
   ```

2. Set up your OpenAI API key:
   ```
   export OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the GitAI agent script:

```
python GitAIAgent.py
```

The agent will prompt you for a Git-related task. Enter your request in natural language, and the agent will interpret and execute the appropriate Git commands.

## Contributing

We welcome contributions to improve and expand the GitAI Agent. Here are some ways you can contribute:

### Enhancing Security with Guardrails

One of the key areas for contribution is implementing and improving guardrails for the shell tool. This involves adding safety checks and input validation to ensure that only safe Git commands are executed. Contributors are encouraged to think about potential security risks and propose solutions.

### Other Contribution Areas

- Enhancing the agent's capabilities to handle more complex Git scenarios
- Improving error handling and user feedback
- Expanding the documentation with more examples and use cases
- Adding comprehensive test coverage
- Reporting issues and suggesting improvements

When contributing, please ensure that your changes align with the project's goals of maintaining a balance between functionality and security.
