from fastapi import FastAPI
from api.auth_api import router as auth_router
from api.food_scan_api import router as food_router
from api.health_advice_api import router as advice_router
from api.alerts_api import router as alerts_router
from api.planner_api import router as planner_router

app = FastAPI(title="AI Health Assistant")

# Register routes
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(food_router, prefix="/food", tags=["Food Scanner"])
app.include_router(advice_router, prefix="/advice", tags=["Health Advice"])
app.include_router(alerts_router, prefix="/alerts", tags=["Alerts"])
app.include_router(planner_router, prefix="/planner", tags=["Diet Planner"])

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Health Assistant API"}
