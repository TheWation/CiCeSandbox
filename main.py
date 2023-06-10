from fastapi import FastAPI
import os
from fastapi.responses import HTMLResponse

from io import StringIO
from contextlib import redirect_stdout

app = FastAPI()

@app.get("/rce/execute/{name}")
async def execute(name: str):
    try:
        f = StringIO()
        with redirect_stdout(f):
            exec(f'print("Hello {name} !!!")')
        output = f.getvalue()

        status_code = 200
    except Exception as e:
        output = 'Server Error !'
        status_code = 500

    return HTMLResponse(content=output, status_code=status_code)

@app.get("/rce/break/{firstname}")
async def execute(firstname: str):
    try:
        namespace = {}
        exec(f'user_name="Hi dear {firstname}"', namespace)
        return {"success": True, 'result': namespace['user_name']}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.get("/ci/ping/blind/{host}")
async def ping(host: str):
    status = True
    exit_status = os.system(f"ping -c 1 {host}")
    if exit_status != 0:
        status = False
    return {"status": status}

@app.get("/ci/ping/{host}")
async def ping(host: str):

    output_file = "output.txt"
    os.system(f"ping -c 1 {host} > {output_file}")
    with open(output_file, "r") as f:
        output = f.read()

    return {"status": output}