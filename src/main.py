from fastapi import FastAPI

from src.ai_solutions import ai_solutions_router_v0
from src.utils.db.db_connections import lifespan
from src.utils.exceptions.exceptions_handling_middleware import ExceptionHandlingMiddleware

app = FastAPI(
    title='ALICE Backend',
    description='ALICE Backend API Server',
    lifespan=lifespan,
)


app.add_middleware(ExceptionHandlingMiddleware)


@app.get('/')
async def main() -> dict:
    return {'message': 'Hello, world. This is TMS(Tell Me Solution) Backend Service'}


app.include_router(ai_solutions_router_v0.router, prefix='/api')
