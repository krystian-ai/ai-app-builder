# AI App Builder

AI App Builder is an intelligent Python application that streamlines and automates the app development process. Developed by krystian-ai on GitHub, this tool leverages OpenAI (GPT-3.5 Turbo or GPT-4) to generate project plans, create file structures, and guide developers through the development process.

## Features

- Interactive app description input
- OpenAI-powered app naming and confirmation
- Feature collection with user hints
- OpenAI-generated project file structure
- Iterative user feedback on file structure
- Automated file and folder creation in the workspace
- OpenAI-generated file content with user confirmation
- Built-in test suite and error reporting
- OpenAI-assisted error fixing
- Support for chat-based OpenAI interactions

## Installation

1. Clone the repository:

```bash
git clone https://github.com/krystian-ai/ai-app-builder.git
```

2. Install the required dependencies:

```bash
cd ai-app-builder
pip install -r requirements.txt
```


## Usage

To run the AI App Builder, simply execute the following command:

```
python app/main.py
```


Follow the prompts to input your app description, name, features, and provide feedback on the generated project structure and file contents. The AI App Builder will create files and folders in the workspace directory and iteratively improve the generated content based on your feedback.

## Tests

To run the test suite, execute the following command:

```
pytest tests/
```

This will run all tests and display the results, including any errors or failures.

## License

This project is released under the [MIT License](LICENSE).

## Contributing

If you'd like to contribute to the AI App Builder project, please feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/krystian-ai/ai-app-builder).

