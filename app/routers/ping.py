from fastapi import  Depends
from fastapi import APIRouter

from app.dependencies.rate_limiters import (
    fixed_window_rate_limiter_dependency,
    token_bucket_rate_limiter_dependency,
)


router = APIRouter()


@router.get(
    "/ping",
    dependencies=[
        Depends(fixed_window_rate_limiter_dependency(limit=3, window_size=2))
    ],
    tags=["limited by Fixed Window Rate Limiter"],
)
def ping():
    return {"message": "pong"}


@router.get(
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
