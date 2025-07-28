from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": ""})

@app.post("/colorful", response_class=HTMLResponse)
async def make_colorful(request: Request, user_input: str = Form(...)):
    colors = ["red", "orange", "green", "blue", "purple", "pink", "teal"]
    colorful_text = ""
    for i, ch in enumerate(user_input):
        color = colors[i % len(colors)]
        colorful_text += f'<span style="color:{color}">{ch}</span>'
    return templates.TemplateResponse("index.html", {"request": request, "result": colorful_text})
