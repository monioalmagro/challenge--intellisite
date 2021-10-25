# challenge--intellisite

## Author: Emiliano Mazzurque emazzurque@gmail.com



Run the proyect 
==========================
*  Create  network intellisite
```bash
$ docker network create intellisite
```
*  build and start service
```bash
$ docker-compose up --buil -d
```

## Check Swagger
http://localhost:8000/docs/

## Check alerts `intellisite.alerts`.
http://0.0.0.0:9000/

## Check  GET /detections 
http://localhost:8000/detections
## Check  GET/stats
http://localhost:8000/stats