# Lab3: Docker Containerization - Sayee Aher 

## Customized Docker_Labs/Lab1 (FastAPI ML API)

### Changes Made:
- ✅ Flask → FastAPI + ML model (iris prediction)
- ✅ Port 5000 → 8000 (production standard)  
- ✅ Python 3.9 → 3.11 (latest)
- ✅ Added uvicorn production server
- ✅ Swagger UI + ML endpoints

## 📋 Overview
Containerized FastAPI ML prediction API (iris classification). Upgraded from Lab1 Flask → Production Docker deployment.

### Run:
## 🚀 Quick Start

```bash
# Build Docker image
docker build -t sayee-lab3 .

# Run container
docker run -p 8080:8000 sayee-lab3
# Check Docker
# 1. SHOW DOCKER PROOF
docker ps

# 2. SHOW PORT MAPPING
docker port [container_id]
