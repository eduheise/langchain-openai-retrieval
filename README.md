# Movie Recommender System

This is a simple movie recommender system built using matrix factorization. The system leverages the MovieLens dataset to predict user movie ratings and provides recommendations based on similar movies.

**Table of Contents**

- Description
- Installation
- Usage
- License
- Check Out Heise Mind

**Description**

This project contains two main components:

1. `documents`: Contains the document handling, loading, and preprocessing code.
2. `llm`: Includes the implementation of the chain to retrieve documents and consume OpenAI's model.
3. `app`: Contains the FastAPI-related stuff.

**Installation**

1. Clone the repository:

```bash
   git clone https://github.com/eduheise/langchain-openai-retrieval.git
   cd langchain-openai-retrieval
```

2. Install the required dependencies:

```bash
   pip install -r requirements.txt
```

3. Download and place the [MovieLens dataset](https://grouplens.org/datasets/movielens/) (`ratings.csv`, `movies.csv`, etc.) in the `data` directory.

**Usage**

1. Add all of the documents that you want in PDF format, with plain text in it.

2. Run the FastAPI:

```bash
   uvicorn app:app --reload
```

3. Ask the model sending a GET package or accessing the swagger API through http://127.0.0.1:8000/docs:

    Curl command:
```bash
    curl -X 'GET' \
      'http://127.0.0.1:8000/question?question=What%20is%20ADADRIFT%3F' \
      -H 'accept: application/json'
```

   This script demonstrates the process of recommending similar movies for a given list of movie IDs.

**License**

This project is licensed under the MIT License.

---

**Check Out Heise Mind**

If you're interested in AI, check out my YouTube channel, [Heise Mind](https://www.youtube.com/@HeiseMind). I create deep-tech content about a variety of tech-related topics.

You might find my video on "LangChain for Document Retrieval with ChatGPT" particularly helpful: [Watch the Video](https://www.youtube.com/watch?v=vuj69j60_nc).
