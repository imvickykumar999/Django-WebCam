# Django-WebCam

Visit IPV4 IP Address : http://192.168.0.18:8000/

---

### Install Daphne if you haven't already
    pip install daphne

### Run the server with Daphne
    daphne -p 8000 webcam_project.asgi:application

### Run on IPV4 Network
    daphne -b 0.0.0.0 -p 8000 webcam_project.asgi:application

---

### Install Uvicorn if you haven't already
    pip install uvicorn

### Run the server with Uvicorn
    uvicorn webcam_project.asgi:application --port 8000

### Run on IPV4 Network
    uvicorn webcam_project.asgi:application --host 0.0.0.0 --port 8000
