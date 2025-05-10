from collections import defaultdict

from app.services.rate_limiter.base import RateLimiter
import time


class FixedWindowRateLimiter(RateLimiter):
    def __init__(self, limit: int, window_size: int):
        self.limit = limit
        self.window_size = window_size
        self.window_start = defaultdict(lambda: int(time.time()))
        self.counter = defaultdict(lambda: 0)

    def allow_request(self, identifier: str) -> bool:
        current_time = int(time.time())
        start_window = self.window_start[identifier]

        if current_time - start_window >= self.window_size:
            self.reset(identifier)

        if self.counter[identifier] < self.limit:
            self.counter[identifier] += 1
            return True

        return False

    def reset(self, identifier: str):
        self.counter[identifier] = 0
        self.window_start[identifier] = int(time.time())
