# ArticleAssistant

ArticleAssistant is a dynamic chatbot that answers questions based on the content of provided articles. It utilizes the power of OpenAI's models and ActiveLoop's Deep Lake to efficiently search and respond to user queries.

## Getting Started

### Prerequisites

- Python 3.x
- OpenAI API key
- ActiveLoop token

### Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/djpapzin/ArticleAssistant.git
   cd ArticleAssistant
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Environment Variables**:
   - Rename the `.env copy` file to `.env`.
   - Obtain your OpenAI API key and ActiveLoop token.
   - Paste them in the appropriate places in the `.env` file.

### Usage

Run the `article_assistant.py` script:
```bash
python article_assistant.py
```
Follow the on-screen prompts to interact with the chatbot.

## Acknowledgements

This project was inspired and built by following the tutorial available at [ActiveLoop's Langchain Course](https://learn.activeloop.ai/courses/take/langchain/multimedia/46318012-build-a-customer-support-question-answering-chatbot).