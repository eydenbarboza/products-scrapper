from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ProductDTO:
    name: str
    price: str
    promo_price: Optional[str] = None

@dataclass
class ProductListDTO:
    url: str
    products: List[ProductDTO]
