from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

# Optional: Enable CORS for browser compatibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": ""})

@app.post("/colorful", response_class=HTMLResponse)
async def make_colorful(request: Request, user_input: str = Form(...)):
    colors = ["red", "orange", "green", "blue", "purple", "pink", "teal"]
    colorful_text = "".join(
        f'<span style="color:{colors[i % len(colors)]}">{ch}</span>' for i, ch in enumerate(user_input)
    )
    return templates.TemplateResponse("index.html", {"request": request, "result": colorful_text})

# Error handling
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return PlainTextResponse(f"Internal Error: {str(exc)}", status_code=500)
