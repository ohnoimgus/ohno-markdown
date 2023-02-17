from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import aiofiles
from markdown import markdown
from aiocache import cached, Cache

app = FastAPI()


@app.get('/')
@app.get('/{file_name}')
async def document(file_name='index'):
    return await serve_document(file_name)


async def serve_document(file_name):
    try:
        return HTMLResponse(await get_file(file_name))
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail='Whops!')


@cached(cache=Cache.MEMORY)
async def get_file(file_name='index'):
    async with aiofiles.open(f'documents/{file_name}.md', mode='r') as file:
        content = await file.read()
        return markdown(content)
