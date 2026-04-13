from fastapi import FastAPI, Response

app = FastAPI()

http_requests_total = 0
http_errors_total = 0

@app.get("/")
def root():
    global http_requests_total
    http_requests_total += 1
    data = "OK"
    return Response(content=data, media_type="text/plain")

@app.get("/metrics")
def metrics():
    global http_requests_total, http_errors_total
    http_requests_total += 1
    data = (
        "# HELP http_requests_total Total requests\n"
        "# TYPE http_requests_total counter\n"
        f"http_requests_total {http_requests_total}\n"
        "# HELP http_errors_total Total errors\n"
        "# TYPE http_errors_total counter\n"
        f"http_errors_total {http_errors_total}\n"
    )
    return Response(content=data, media_type="text/plain")