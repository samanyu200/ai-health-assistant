from fastapi import APIRouter

router = APIRouter()

@router.get("/future-risk")
def get_risk_assessment():
    return {
        "risk_level": "Low",
        "recommendations": [
            "Keep exercising",
            "Maintain current diet",
            "Avoid processed food"
        ]
    }

@router.post("/generate")
def create_custom_alert(data: dict):
    # data can include diet, activity, vitals etc.
    return {
        "status": "ok",
        "alert": "Based on your sugar intake, reduce sweets for 3 days."
    }
