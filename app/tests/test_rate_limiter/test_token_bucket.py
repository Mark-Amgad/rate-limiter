import time

from app.services.rate_limiter.token_bucket import TokenBucketRateLimiter


def test_token_bucket_allows_within_capacity():
    limiter = TokenBucketRateLimiter(10,1)
    identifier = 'user-1'
    for i in range(10):
        assert limiter.allow_request(identifier) == True

def test_token_bucket_blocks_over_capacity():
    limiter = TokenBucketRateLimiter(10, 1)
    identifier = 'user-1'
    for i in range(10):
        limiter.allow_request(identifier)

    assert limiter.allow_request(identifier) == False

def test_token_bucket_refill():
    limiter = TokenBucketRateLimiter(10, 1)
    identifier = 'user-1'
    for i in range(10):
        assert limiter.allow_request(identifier) == True

    assert limiter.allow_request(identifier) == False
    time.sleep(1.5)
    assert limiter.allow_request(identifier) == True


