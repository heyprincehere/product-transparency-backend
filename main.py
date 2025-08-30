from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow frontend to connect (update for deployed frontend URL later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update to Vercel URL after deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Product(BaseModel):
    name: str
    category: str
    ingredients: str

products = []

@app.post("/add-product")
async def add_product(product: Product):
    products.append(product)
    return {"message": "Product added", "product": product}

@app.post("/generate-questions")
async def generate_questions(product: Product):
    questions = [
        f"What is the source of the ingredients in {product.name}?",
        f"Is {product.name} in the {product.category} category sustainable?"
    ]
    return {"questions": questions}