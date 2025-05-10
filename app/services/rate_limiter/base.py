from abc import ABC, abstractmethod


class RateLimiter(ABC):
    @abstractmethod
    def allow_request(self, identifier: str) -> bool:
        """
        Check if a request is allowed for the given identifier (e.g., user_id or IP).
        Returns True if allowed, False if rate limited.
        """
        pass