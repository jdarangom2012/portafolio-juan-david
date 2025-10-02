from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, validator
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
import os
from typing import Optional
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuración de la base de datos
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://usuario:password@localhost:5432/portafolio_db"
)

# Crear engine y sesión
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo de la base de datos
class ContactMessage(Base):
    __tablename__ = "contact_messages"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False)
    subject = Column(String(200), nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    ip_address = Column(String(45), nullable=True)
    user_agent = Column(String(500), nullable=True)

# Crear las tablas
Base.metadata.create_all(bind=engine)

# Modelos Pydantic
class ContactMessageCreate(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str
    
    @validator('name')
    def validate_name(cls, v):
        if len(v.strip()) < 2:
            raise ValueError('El nombre debe tener al menos 2 caracteres')
        if len(v.strip()) > 100:
            raise ValueError('El nombre no puede exceder 100 caracteres')
        return v.strip()
    
    @validator('subject')
    def validate_subject(cls, v):
        if len(v.strip()) < 5:
            raise ValueError('El asunto debe tener al menos 5 caracteres')
        if len(v.strip()) > 200:
            raise ValueError('El asunto no puede exceder 200 caracteres')
        return v.strip()
    
    @validator('message')
    def validate_message(cls, v):
        if len(v.strip()) < 10:
            raise ValueError('El mensaje debe tener al menos 10 caracteres')
        if len(v.strip()) > 2000:
            raise ValueError('El mensaje no puede exceder 2000 caracteres')
        return v.strip()

class ContactMessageResponse(BaseModel):
    id: int
    name: str
    email: str
    subject: str
    message: str
    created_at: datetime
    
    class Config:
        orm_mode = True

# Inicializar FastAPI
app = FastAPI(
    title="Portafolio Juan David Arango - API",
    description="API backend para el portafolio profesional de Juan David Arango Morales",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios exactos
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rutas
@app.get("/")
async def root():
    """Endpoint raíz con información de la API"""
    return {
        "message": "API del Portafolio de Juan David Arango Morales",
        "version": "1.0.0",
        "status": "active",
        "endpoints": {
            "contact": "/api/contact",
            "health": "/api/health",
            "docs": "/api/docs"
        }
    }

@app.get("/api/health")
async def health_check():
    """Endpoint para verificar el estado de la API"""
    try:
        # Verificar conexión a la base de datos
        db = SessionLocal()
        db.execute("SELECT 1")
        db.close()
        
        return {
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
            "database": "connected",
            "version": "1.0.0"
        }
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return JSONResponse(
            status_code=503,
            content={
                "status": "unhealthy",
                "timestamp": datetime.utcnow().isoformat(),
                "database": "disconnected",
                "error": str(e)
            }
        )

@app.post("/api/contact", response_model=dict)
async def create_contact_message(
    contact_data: ContactMessageCreate,
    db: Session = Depends(get_db)
):
    """Crear un nuevo mensaje de contacto"""
    try:
        # Crear el mensaje en la base de datos
        db_message = ContactMessage(
            name=contact_data.name,
            email=contact_data.email,
            subject=contact_data.subject,
            message=contact_data.message,
            created_at=datetime.utcnow()
        )
        
        db.add(db_message)
        db.commit()
        db.refresh(db_message)
        
        logger.info(f"Nuevo mensaje de contacto creado: ID {db_message.id}")
        
        return {
            "success": True,
            "message": "Mensaje enviado exitosamente",
            "id": db_message.id,
            "timestamp": db_message.created_at.isoformat()
        }
        
    except Exception as e:
        logger.error(f"Error creating contact message: {str(e)}")
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Error interno del servidor. Por favor, intenta de nuevo más tarde."
        )

@app.get("/api/contact/messages", response_model=list[ContactMessageResponse])
async def get_contact_messages(
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    """Obtener mensajes de contacto (para administración)"""
    try:
        messages = db.query(ContactMessage)\
                    .order_by(ContactMessage.created_at.desc())\
                    .offset(skip)\
                    .limit(limit)\
                    .all()
        
        return messages
        
    except Exception as e:
        logger.error(f"Error retrieving contact messages: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Error al obtener los mensajes"
        )

@app.get("/api/stats")
async def get_stats(db: Session = Depends(get_db)):
    """Obtener estadísticas básicas"""
    try:
        total_messages = db.query(ContactMessage).count()
        
        return {
            "total_messages": total_messages,
            "api_version": "1.0.0",
            "status": "active"
        }
        
    except Exception as e:
        logger.error(f"Error getting stats: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Error al obtener estadísticas"
        )

# Manejo de errores globales
@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "error": "Datos de entrada inválidos",
            "detail": str(exc)
        }
    )

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "Error interno del servidor",
            "detail": "Por favor, intenta de nuevo más tarde"
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

