import asyncio
import logging
from playwright.async_api import async_playwright

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class PlaywrightManager:
    def __init__(self, headless: bool, ignore_https_errors: bool) -> None:
        self.headless = headless
        self.ignore_https_errors = ignore_https_errors
        self.browser = None
        self.page = None

    async def __aenter__(self):
        await self.launch_browser()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close_browser()

    async def launch_browser(self):
        """Launches the browser and opens a new page."""
        playwright = await async_playwright().start()
        self.browser = await playwright.chromium.launch(headless=self.headless)
        self.context = await self.browser.new_context(ignore_https_errors=self.ignore_https_errors) 
        self.page = await self.browser.new_page()

    async def close_browser(self):
        """Closes the browser and terminates the Playwright instance."""
        if self.browser:
            await self.browser.close()

    async def load_page(self, url: str):
        """Loads a URL in the current page."""
        await self.page.goto(url)

    async def scroll_to_load_products(self):
        """Performs gradual scrolling to load products on the page."""
        previous_product_count = 0
        while True:
            await self.scroll_down()
            sections = await self.page.query_selector_all('article.vtex-product-summary-2-x-element')
            current_product_count = len(sections)

            if current_product_count == previous_product_count:
                break
            previous_product_count = current_product_count

    async def scroll_down(self, steps: int = 15, step_distance: int = 50, delay: int = 1):
        """Scrolls the page down gradually."""
        for _ in range(steps):
            await self.page.mouse.wheel(0, step_distance)
            await asyncio.sleep(delay)

    async def extract_product_data(self, section) -> dict:
        """Extracts data for a specific product."""
        try:
            name = await self.extract_text(section, 'h3')
            price = await self.extract_text(section, '.tiendasjumboqaio-jumbo-minicart-2-x-pp_container')
            promo_price = await self.extract_text(section, '.tiendasjumboqaio-jumbo-minicart-2-x-price--product-prime')

            return {
                'name': name.strip(),
                'price': price.replace('\xa0', ' ').strip() if price else 'Not available',
                'promo_price': promo_price.replace('\xa0', ' ').strip() if promo_price else 'Not available'
            }
        except Exception as e:
            logger.error(f"Error extracting product data: {e}")
            return {}

    async def extract_text(self, section, selector: str) -> str:
        """Extracts text from the selected element, or returns 'Not available'."""
        element = await section.query_selector(selector)
        return await element.inner_text() if element else 'Not available'

    async def get_products(self, url: str) -> list:
        """Obtains product data on the specified page."""
        products = []
        async with self:
            await self.load_page(url)
            await self.scroll_to_load_products()

            sections = await self.page.query_selector_all('article.vtex-product-summary-2-x-element')
            for section in sections:
                product_data = await self.extract_product_data(section)
                if product_data:
                    products.append(product_data)

        return products
