import time
from collections import defaultdict

from app.services.rate_limiter.base import RateLimiter


class TokenBucketRateLimiter(RateLimiter):
    def __init__(self, capacity: int, refill_rate_per_second: float):
        self.capacity = capacity
        self.refill_rate = refill_rate_per_second
        self.tokens = defaultdict(lambda: self.capacity)
        self.last_refill = defaultdict(lambda: int(time.time()))

    def allow_request(self, identifier: str) -> bool:
        self.refill(identifier)
        if self.tokens[identifier] > 0:
            self.tokens[identifier] -= 1
            return True
        return False

    def refill(self, identifier):
        last_time_refill = self.last_refill[identifier]
        now = int(time.time())
        elapsed = now - last_time_refill
        refill_amount = elapsed * self.refill_rate
        self.tokens[identifier] = min(
            self.capacity, int(self.tokens[identifier] + refill_amount)
        )
        self.last_refill[identifier] = now
