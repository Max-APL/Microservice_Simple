from fastapi import FastAPI
from api.venta import router as venta_router
from api.detalle_venta import router as detalle_venta_router

app = FastAPI()

app.include_router(venta_router, prefix="/ventas", tags=["Ventas"])
app.include_router(detalle_venta_router, prefix="/ventas", tags=["Detalles de Venta"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)
