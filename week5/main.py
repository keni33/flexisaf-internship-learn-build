from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts: list[dict] =[
      {
          "id": 1,
          "author": "Corey shaffer",
          "title": "FastAPI is Awesome",
          "content": "This framework is really easy to use and super fast",
          "date_posted":"April 20, 2025"
    },
    {
        
    }





]