import fastapi
from llm import LanguageModel


app = fastapi.FastAPI()
model = LanguageModel()


@app.get('/question')
def question(question: str):
    return {'answer': model.ask(question)}


if __name__ == '__main__':
    app.run()
