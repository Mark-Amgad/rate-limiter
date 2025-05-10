from fastapi import FastAPI, Depends

from app.dependencies.rate_limiters import (
    fixed_window_rate_limiter_dependency,
    token_bucket_rate_limiter_dependency,
)

app = FastAPI()


@app.get(
    "/ping",
    dependencies=[
        Depends(fixed_window_rate_limiter_dependency(limit=3, window_size=2))
    ],
    tags=["limited by Fixed Window Rate Limiter"],
)
def ping():
    return {"message": "pong"}


@app.get(
    "/tic",
    dependencies=[
        Depends(
            token_bucket_rate_limiter_dependency(capacity=3, refill_rate_per_second=1)
        )
    ],
    tags=["limited by Token Bucket Rate Limiter"],
)
def tic():
    return {"message": "toc"}
