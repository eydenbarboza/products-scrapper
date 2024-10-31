## Introduction
Implement basic product scraping using Playwright, laying groundwork for future enhancements with Scrapy. The solution is designed with a robust layered architecture, design patterns, and is oriented to Domain-Driven Design (DDD). The project is documented using Swagger/OpenAPI.



# Architecture 

```
+-------------------------------------------+
|                   API                     |
|       (FastAPI + Swagger/OpenAPI)         |
+------------------------+------------------+
                         |
                         |
+------------------------v------------------+
|                Application Layer          |
|  (Service handlers, DTOs, API controllers)|
+------------------------+------------------+
                         |
                         |
+------------------------v------------------+
|                Domain Layer               |
|   (Entities, Value Objects, Aggregates,   |
|           Domain Services)                |
+------------------------+------------------+
                         |
                         |
+------------------------v------------------+
|                Infrastructure Layer       |
|    (Repositories, Data Sources,           |
|     External Service Integrations, Playwright/Scrapy)        |
+------------------------+------------------+
                         
```



# Use Cases Supported

- Endpoint to retrieve the first 15 products
- Endpoint to retrieve all products by page 
- Asynchronous Browser Management
- Configurable Headless Mode 
- Progressive Scrolling to Load Dynamic Content



# Usage
docker compose up -d


# Access the API documentation
Open your browser and go to http://localhost:8000/docs to see the Swagger UI.
