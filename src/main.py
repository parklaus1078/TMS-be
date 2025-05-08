from fastapi import FastAPI

app = FastAPI(
    title='ALICE Backend',
    description='ALICE Backend API Server',
)


@app.get('/')
async def main() -> dict:
    return {'message': 'Hello, world. This is TMS(Tell Me Solution) Backend Service'}
