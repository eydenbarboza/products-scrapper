from abc import ABC, abstractmethod
import httpx



class BaseHTTPXRepository(ABC):

    @abstractmethod
    async def fetch(self, url: str) -> bytes:
        """ Realiza una solicitud GET y devuelve el contenido como bytes. """
        pass



class HTTPXRepository(BaseHTTPXRepository):

    async def fetch(self, url: str) -> bytes:
        """ Implementación de la solicitud GET para obtener contenido. """
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status() 
            return response
