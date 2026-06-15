"""
I learn FastAPI with CRUD points. In this system, tasks will be created,
 these tasks will belong to specific categories,
 and how many Pomodoros (work sessions) have been performed on the tasks will be tracked.
"""

from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel

app = FastAPI()
class DBCategories:
    id : str
    name : str

    def __init__(self,id,name):
        self.id = id
        self.name = name

class CategoryRequest(BaseModel):
    id : str
    name : str

db_categories = [{'id' : '12324', 'name' : 'software'},
                 {'id' : '34234', 'name' : 'software'},
                 {'id' : '36443', 'name' : 'sport'},
                 {'id' : '56745', 'name' : 'personal'},
                 {'id' : '23525', 'name' : 'personal'},
                 {'id' : '35434', 'name' : 'personal'}
                 ]

class DBTask:
    id : str
    category_id : str
    title : str
    status : str
    estimated_pomodoros : int
    completed_pomodoros : int

    def __init__(self,id,category_id,title,status,estimated_pomodoros,completed_pomodoros):
        self.id = id
        self.category_id = category_id
        self.title = title
        self.status = status
        self.estimated_pomodoros = estimated_pomodoros
        self.completed_pomodoros = completed_pomodoros

class TaskRequest(BaseModel):
    id : str
    category_id : str
    title : str
    status : str
    estimated_pomodoros : int
    completed_pomodoros : int

db_tasks = [
    {'id': '23456',
     'category_id':'12324',
     'title':'doings',
     'status': 'todo',
     'estimated_pomodoros':4,
     'completed_pomodoros':0 },
    {'id':'34534',
     'category_id':'34234',
     'title':'important',
     'status':'in_progress',
     'estimated_pomodoros':2,
     'completed_pomodoros':1 },
    {'id':'23465',
     'category_id':'36443',
     'title':'did_things',
     'status':'completed',
     'estimated_pomodoros':0,
     'completed_pomodoros':3 }

]

@app.get("/categories/")
async def read_all_categories():
    return db_categories

@app.get("/tasks/")
async def read_tasks(status: str = None, category_id: str = None):
    if not status and not category_id: # Eğer hiçbir filtre girilmezse direkt tüm listeyi döner
        return db_tasks

    tasks_to_return=[]
    for task in db_tasks:
        if status and task['status'].casefold()==status.casefold():# Status filtresi varsa ve eşleşiyorsa
            tasks_to_return.append(task)

        elif category_id and task['category_id']==category_id:# Category_id filtresi varsa ve eşleşiyorsa
            tasks_to_return.append(task)

    return tasks_to_return


@app.post("/categories/")
async def create_category(category_request: CategoryRequest):
    new_category = DBCategories(**category_request.model_dump())
    db_categories.append(new_category)
    return {'message' : 'Category created successfully!', "category" : new_category}

@app.post("/tasks/")
async def create_task(task_request : TaskRequest ):
    new_task=DBTask(**task_request.model_dump())

    category_exists = False
    for category in db_categories:
        if category['id'] == new_task.category_id:
            category_exists = True
            break

    if not category_exists:
        raise HTTPException(status_code=400, detail="Category does not exist!")

    db_tasks.append(new_task)
    return {'message' : 'Task created successfully!', "task" : new_task}


@app.put("/tasks/{task_id}")
async def update_task(task_id: str, updated_task: TaskRequest ):
        for i in range(len(db_tasks)):
            if db_tasks[i].get('id') == task_id:
                new_data = updated_task.model_dump()
                new_data['id'] = task_id
                db_tasks[i].update(new_data)
                return {'message' : 'Task updated successfully!', "task" : updated_task}

        raise HTTPException(status_code=400, detail="Task does not exist!")


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    for i in range(len(db_tasks)):
        if db_tasks[i].get('id') == task_id:
            db_tasks.pop(i)
            return {'message' : 'Task deleted successfully!'}

    raise HTTPException(status_code=400, detail="Task does not exist!")

@app.post("/tasks/{task_id}/pomodoro")
async def add_pomodoro(task_id: str):
    for task in db_tasks:
        if task['id'] == task_id:
            if task['status'] == 'completed':
                raise HTTPException(status_code=400, detail="Pomodoro already completed!")

            task['completed_pomodoros'] += 1

            if task['completed_pomodoros'] >= task['estimated_pomodoros']:
                task['status'] = 'completed'
                return {'message' : 'Pomodoro completed successfully!', "task" : task}

            return {'message' : 'Pomodoro not completed!', "task" : task}

        raise HTTPException(status_code=400, detail="Pomodoro does not exist!")

