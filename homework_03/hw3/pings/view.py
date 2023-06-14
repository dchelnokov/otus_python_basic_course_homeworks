from fastapi import APIRouter, status

router = APIRouter()


@router.get(
    "/ping/",
    response_model=dict,
    description="reacts to ping",
)
def reply_to_ping() -> dict:
    return {
        "message": "pong"
    }