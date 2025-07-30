from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

from api.auth_api import router as auth_router
from api.food_scan_api import router as food_router
from api.health_advice_api import router as advice_router
from api.alerts_api import router as alerts_router
from api.planner_api import router as planner_router

app = FastAPI(title="AI Health Assistant")

# Register API routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(food_router, prefix="/food", tags=["Food Scanner"])
app.include_router(advice_router, prefix="/advice", tags=["Health Advice"])
app.include_router(alerts_router, prefix="/alerts", tags=["Alerts"])
app.include_router(planner_router, prefix="/planner", tags=["Diet Planner"])

# Serve frontend as static files
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# Serve specific HTML files
@app.get("/")
def serve_index():
    return FileResponse(os.path.join(frontend_path, "index.html"))

@app.get("/login")
def serve_login():
    return FileResponse(os.path.join(frontend_path, "login.html"))

@app.get("/register")
def serve_register():
    return FileResponse(os.path.join(frontend_path, "register.html"))

@app.get("/dashboard")
def serve_dashboard():
    return FileResponse(os.path.join(frontend_path, "dashboard.html"))
