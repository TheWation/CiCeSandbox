from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get("/rce/execute/{code}")
async def execute(code: str):
    try:
        exec(code)
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}

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