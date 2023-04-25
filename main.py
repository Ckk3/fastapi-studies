from fastapi import FastAPI
import subprocess
import os

app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/name")
def name(name: str):
    return {"name": name}


@app.get("/pm2logs")
def read_pm2logs():
    proc = subprocess.run(
        ["pm2", "logs", "--lines", "100", "--nostream"], capture_output=True
    )
    output = proc.stdout
    return {"output": output}


@app.delete("/deletefolder")
def delete_folder():
    try:
        os.rmdir("testfolder")
        return {"output": "File deleted successfully"}
    except OSError as error:
        raise Exception(f"File deletion failed: {error}")
