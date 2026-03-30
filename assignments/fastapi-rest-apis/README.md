# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Build a REST API using the FastAPI framework to define routes, handle requests, and return JSON responses.

## 📝 Tasks

### 🛠️ Create the FastAPI App

#### Description

Set up a new FastAPI application and define the core structure for handling incoming requests.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`
- Define at least one root endpoint (`/`) that returns a JSON welcome message
- Include comments describing how to start the server with Uvicorn

### 🛠️ Define REST Endpoints

#### Description

Add API endpoints to support basic CRUD-style operations for a sample resource.

#### Requirements
Completed program should:

- Define a `GET` endpoint to return a list of sample items
- Define a `POST` endpoint to accept JSON request data and return the created item
- Use Pydantic models for request validation and response structure

### 🛠️ Test and Run the API

#### Description

Run the FastAPI application and verify the endpoints using example requests.

#### Requirements
Completed program should:

- Include example request and response details in comments
- Demonstrate that the server can run locally with `uvicorn`
- Return appropriate JSON responses for each endpoint
