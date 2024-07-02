import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from database.connection import conn

app = FastAPI(title="AppName", version="0.0.1")

# Configurando middleware CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conexão ao banco de dados no evento de inicialização
@app.on_event("startup")
async def on_startup():
    conn()

# Rota para a página de login
@app.get("/", response_class=HTMLResponse)
async def hello():
    return open("templates/login.html", "r").read()

# Rota para a página de registro
@app.get("/register", response_class=HTMLResponse)
async def register():
    return open("templates/register.html", "r").read()

# Rota para a página do dashboard
@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    return open("templates/dashboard.html", "r").read()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
