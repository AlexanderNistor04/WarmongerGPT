For this project, an OpenAI API key is needed. The user can generate a key on OpenAI's website here https://platform.openai.com/docs/overview
Go to API -> API keys -> create new secret key. This will generate a unique API key starting with "sk-". It is very important that this key is kept secret to prevent outside users from using GPT generation tokens without your permission.
To use the key in the project, open keys.py and enter the key into the openai_key variable.

This project requires the user to have installed langchain and specifically the langchain-openai package. It's easiest to do this using pip. 
To install pip, follow the instructions in this link https://pip.pypa.io/en/stable/installation/
Once pip is installed, navigate to the project directory in terminal and install langchain-open with the line:
$ pip install langchain-openai
After installing langchain, the project should be ready to run. Running the main file will prompt the user to ask warmongerGPT a question, which will use the OpenAI API to generate a response.
