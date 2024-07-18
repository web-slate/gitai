# GitAI Agent

GitAI Agent is an AI-powered assistant that can execute Git commands through natural language instructions. It uses OpenAI's language model and LangChain's agent framework to interpret user requests and perform Git operations.

## Features
- Executes Git commands directly in the shell
- Uses language model as a reasoning engine to determine which actions to take and in which order
- Agent can interpret error messages and take actions on its own

## Prerequisites
- OpenAI API key
- Git installed and configured on your system

## SetUp
Install Dependencies
   ```
   pip install langchain openai
   ```

Set up your OpenAI API key:
   ```
   export OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the GitAI agent script:

```
python GitAI.py
```

The agent will prompt you for a Git-related task. Enter your request in natural language, and the agent will interpret and execute the appropriate Git commands.
