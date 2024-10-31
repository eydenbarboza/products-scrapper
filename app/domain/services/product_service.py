from infrastructure.playwright.playwright_manager import PlaywrightManager
from infrastructure.repositories.product_repository import ProductRepository
from core.config import (
    PLAYWRIGHT_HEADLESS, 
    PLAYWRIGHT_IGNORE_HTTPS_ERRORS, 
    DB_URL,
    DB_NAME,
    DB_COLLECTION_PRODUCT
    )


def get_service():
    playwright_manager = PlaywrightManager(
        headless=PLAYWRIGHT_HEADLESS,
        ignore_https_errors=PLAYWRIGHT_IGNORE_HTTPS_ERRORS
    )
    repo_product = ProductRepository(
        db_url=DB_URL,
        db_name=DB_NAME,
        collection_name=DB_COLLECTION_PRODUCT
    )
    service = ProductService(
        playwright_manager=playwright_manager,
        repo_product=repo_product
    )
    return service



class ProductService:


    def __init__(
            self,
            playwright_manager: PlaywrightManager,
            repo_product: ProductRepository
            ) -> None:
        self.playwright_manager = playwright_manager
        self.repo_product = repo_product


    async def get_products(self, url: str, limit: int = None):
        products = await self.playwright_manager.get_products(url=url)

        if limit is None:
            limit = 15

        data = dict()
        data["url"] = url
        data["products"] = products[:limit]
        return data