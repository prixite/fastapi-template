from fastapi import APIRouter


router = APIRouter()


@router.get("/users/")
def list_users():
    return [{"name": "Umair"}]
