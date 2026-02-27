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

## Docker Port Mapping EXPLANATION:
docker run -p 8080:8000 sayee-lab3

      ↑HOST PORT      ↑CONTAINER PORT
localhost:8080 → container:8000 (uvicorn)

** BROWSER:** 
http://localhost:8000/ ←  CURRENT PORT!
In Lab3, Uvicorn runs inside a Docker container on 0.0.0.0:8000, and Docker maps that to localhost:8080 on my host.
That’s why I open http://localhost:8080 in the browser, which matches the port mapping shown by docker ps (8080->8000).

**Terminal shows "0.0.0.0:8000" = INSIDE container only!**
**Browser uses:** `localhost:8080` ( port mapping!) 

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
