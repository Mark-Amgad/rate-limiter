from app.services.rate_limiter.fixed_window import FixedWindowRateLimiter
import time


def test_fixed_window_allows_within_limit():
    limiter = FixedWindowRateLimiter(10,2)
    identifier = "user-1"
    for i in range(10):
        assert limiter.allow_request(identifier) == True

def test_fixed_window_blocks_over_limit():
    limiter = FixedWindowRateLimiter(10, 2)
    identifier = "user-1"
    for i in range(10):
        limiter.allow_request(identifier)
    assert limiter.allow_request(identifier) == False

def test_fixed_window_reset():
    limiter = FixedWindowRateLimiter(10,2)
    identifier = "user-1"
    for i in range(10):
        assert limiter.allow_request(identifier) == True

    assert limiter.allow_request(identifier) == False
    time.sleep(2.5)
    assert limiter.allow_request(identifier) == True


def test_fixed_window_manual_reset():
    limiter = FixedWindowRateLimiter(10,2)
    identifier = "user-1"
    for i in range(10):
        assert limiter.allow_request(identifier) == True

    assert limiter.allow_request(identifier) == False
    limiter.reset(identifier)
    assert limiter.allow_request(identifier) == True
