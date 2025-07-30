from fastapi import APIRouter

router = APIRouter()

user_health = {
    "energy": 80,
    "hydration": 60,
    "nutrition_score": 75
}

@router.get("/status")
def health_status():
    return user_health

@router.get("/plan")
def diet_plan():
    return {
        "breakfast": "Oats + Banana + Green Tea",
        "lunch": "Grilled chicken + Brown rice + Salad",
        "dinner": "Soup + Whole grain bread",
        "snacks": "Nuts or fruits"
    }

@router.post("/update")
def update_status(changes: dict):
    for key, value in changes.items():
        if key in user_health:
            user_health[key] = value
    return {"message": "Health status updated", "current": user_health}
