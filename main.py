import os
from sqlalchemy import create_engine, String, Float, CheckConstraint
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session, Mapped, mapped_column
from dotenv import load_dotenv
from fastapi import  Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, Field

DATABASE_URL = os.getenv("DATABASE_URL","postgresql://usuario:senha@localhost:5432/nome_do_banco")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db  = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ProdutoBase(Base):
    __tablename__ = "Produtos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    preco: Mapped[float] = mapped_column(Float,CheckConstraint("preco > 0", name="check_preco_positivo") ,nullable=False)
    estoque: Mappedp[int] = mapped_column(default=0)
    ativo: Mapped[bool] = mapped_column(default=True)

class ProdutoCreate(BaseModel):
    nome: str = Field(...,  min_length=1)
    preco: float = Field(..., gt=0)
    estoque: int = Field(default=0, ge=0)
    ativo: bool = Field(default=True)

class ProdutoResponse(ProdutoCreate):
    id: int

    model_config = {"from_attributes": True}

app = FastAPI(title="E-commerce")

@app.get("/produtos")
def get_produtos(db: Session =  Depends(get_db)):
    return db.query(ProdutoBase).all()