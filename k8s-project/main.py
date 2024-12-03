from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Tempalates

app = FastAPI()
tempalates = Jinja2Tempalates(dirctory="/code")

@app.get("/")
def form_post(requst: Request):
    return tempalates.TempalateResponse('form.html', context={'request': request})
