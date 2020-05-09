from fastapi import Request, status, BackgroundTasks
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sparky import app, templates
import time
from datetime import datetime


def _run_task(name: str, id=None):
    time.sleep(3)
    
    with open("task_result.txt", mode="a") as file:
        now = datetime.now()
        content = f"{name} [{id}]:  {now}\n"
        file.write(content)

@app.post("/task/run/{name}/{id}")
async def task_run(name: str, id: int, background_tasks: BackgroundTasks):
    ''' runs a task '''
    background_tasks.add_task(_run_task, name, id)
    return {"message": f"Task {name}: ID [{id}] is being run now.\n"}

@app.get("/task/show")
async def task_show(request: Request):
    ''' 
    This returns a list of tasks uou can run
    '''
    return JSONResponse(content='bunch of tasks')