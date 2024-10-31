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
|     External Service Integrations (Bright Data), Playwright/Scrapy)        |
+------------------------+------------------+
                         
```



# Use Cases Supported

- Endpoint to retrieve the first 15 products
- Endpoint to retrieve all products by page 
- Asynchronous Browser Management
- Configurable Headless Mode 
- Progressive Scrolling to Load Dynamic Content

# Future Improvements

- Implementation of Rotating IPs with Bright Data: Integrate Bright Data’s rotating IP service to enhance web scraping capabilities by ensuring a stable and reliable connection while minimizing the risk of IP bans. This approach will improve the scraper’s performance and resilience against restrictions imposed by target websites.

- Complete Playwright-Scrapy Integration: Achieve a fully integrated Playwright and Scrapy setup to enable highly scalable web scraping capabilities, allowing for efficient handling of complex web pages and dynamic content.

- Data Persistence in MongoDB: Implement MongoDB as a data storage solution for scraped information, facilitating structured data storage and retrieval for further analysis and reporting.

- OpenTelemetry Implementation for Enhanced Observability: Integrate OpenTelemetry to gain comprehensive visibility into scraping workflows, enabling detailed tracking and troubleshooting, and optimizing overall performance and reliability.

- Increased Use of Constants and Code Parameterization: Refactor code to expand the use of constants and parameters, enhancing flexibility, readability, and ease of maintenance, and allowing the scraper to adapt more readily to changing requirements or configurations.

- Function Composition Optimization: Refine the structure and composition of functions to enhance modularity and reduce redundancy, fostering a codebase that is more readable, maintainable, and adaptable to future enhancements.

- Adherence to SOLID Principles and Clean Architecture: Improve alignment with SOLID principles and Clean Architecture standards, reinforcing the separation of concerns, improving code scalability, and establishing a robust, maintainable framework that simplifies testing and facilitates long-term evolution.

- Secure MongoDB Persistence in Docker Compose: Integrate MongoDB as the primary data storage solution with secure configurations directly in the docker-compose.yml file. This setup will include authentication, access controls, and data encryption settings to ensure secure and reliable data storage within the containerized environment.



# Usage
```bash
docker compose up -d


# Access the API documentation
Open your browser and go to http://localhost:8000/docs to see the Swagger UI.
