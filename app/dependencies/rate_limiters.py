from fastapi import Request, HTTPException

from app.services.rate_limiter.fixed_window import FixedWindowRateLimiter
from app.services.rate_limiter.token_bucket import TokenBucketRateLimiter


def fixed_window_rate_limiter_dependency(limit: int, window_size: int = 10):
    limiter = FixedWindowRateLimiter(limit=limit, window_size=window_size)

    def _dependency(request: Request):
        identifier = request.client.host
        if not limiter.allow_request(identifier):
            raise HTTPException(status_code=429, detail="Rate limit exceeded")

    return _dependency


def token_bucket_rate_limiter_dependency(
    capacity: int, refill_rate_per_second: int = 1
):
    limiter = TokenBucketRateLimiter(
        capacity=capacity, refill_rate_per_second=refill_rate_per_second
    )

    def _dependency(request: Request):
        identifier = request.client.host
        if not limiter.allow_request(identifier):
            raise HTTPException(status_code=429, detail="Rate limit exceeded")

    return _dependency
