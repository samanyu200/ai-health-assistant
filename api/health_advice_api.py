from fastapi import APIRouter
import random

router = APIRouter()

tips = [
    "Drink at least 2 liters of water daily.",
    "Eat fruits in the morning.",
    "Avoid sugar after 7 PM.",
    "Include protein in every meal.",
    "Do 30 mins of cardio daily."
]

@router.get("/tip")
def random_tip():
    return {"tip": random.choice(tips)}

@router.post("/ask")
def ask_health_question(question: str):
    return {
        "question": question,
        "answer": "This is a placeholder AI answer. (Integrate OpenAI or Cohere here.)"
    }
