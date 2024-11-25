from fastapi import FastAPI
from api.producto import router as producto_router
from api.marca import router as marca_router
from api.categoria import router as categoria_router
from services.rabbitmq_consumer import run_consumer_in_thread
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(producto_router, prefix="/gestion_productos", tags=["Productos"])
app.include_router(marca_router, prefix="/gestion_productos", tags=["Marcas"])
app.include_router(categoria_router, prefix="/gestion_productos", tags=["Categorías"])


# Iniciar el consumidor RabbitMQ en un hilo separado
run_consumer_in_thread()

@app.on_event("startup")
async def startup_event():
    print("Microservicio de Productos iniciado correctamente.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
