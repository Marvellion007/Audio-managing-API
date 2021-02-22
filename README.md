# INTODUCTION 
This is a CRUD api for managing audiofiles.
there are 3 types of file namely:
-Song
-Podcast
-Audiobook
The api is dockerized using docker compose.


# HOW TO RUN
In the config directory there are 3 files with different port numbers.
qa which is default port with value 8080
prod with port no. 8000
stg with port no. 5000

1: Move to directory
2: run 'make build ENV=filename' command in the terminal it will build the image
3: run 'make run ENV=filename' command and it will create the docker container 
for example, we can move to the directory and run following commands for qa environment
make build ENV=qa
make run ENV=qa

4: you can open the link
http://127.0.0.1:filename/docs
for interactive Fastapi
     or 
http://127.0.0.1:filename/redoc 
for alternate interactive api


# STRUCTURE OF PROJECT
# core: 
It contains the source code with 3 layers, namely 
- Controller Layer
- Service Layer 
- Repository Layer
Controller layer is the outermost layer of the API which takes the request.
Service layer is the medium which transfer the API call to repository layer
Repository layer is the layer which connects with the database.

# config:
It contains dependencies of source code

# Doc:
It contains the documents

# Build:
It contains the build related things 

# CURL requests for the api:

# CREATE:
curl -X POST "http://127.0.0.1:{PORT}/%22${audioFileType}%22" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{}"

# GET:
curl -X GET "http://127.0.0.1:{PORT}/${audioFileType}/${audioFileID}" -H  "accept: application/json"

# DELETE:
curl -X DELETE "http://127.0.0.1:{PORT}/${audioFileType}/${audioFileID}" -H  "accept: application/json"	
 
# PATCH:
curl -X PATCH "http://127.0.0.1:{PORT}/{audioFileType}/{audioFileID}" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{}"

# FOR EXAMPLE:

#CREATE request for song:
- curl -X POST "http://127.0.0.1:8000/%22song%22" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"ID\":1,\"NAME\":\"fallen\",\"DURATION\":500,\"UPLOAD_TIME\":\"2021-02-22 03:34:05\"}"


#CREATE request for podcast:
- curl -X POST "http://127.0.0.1:8000/%22podcast%22" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"ID\":1,\"NAME\":\"fallen podcast\",\"DURATION\":100,\"UPLOAD_TIME\":\"2021-02-22 03:35:05\",\"HOST\":\"update host\",\"PARTICIPANTS\":[\"fallen\"]}"


#CREATE request for audiobook:
- curl -X POST "http://127.0.0.1:8000/%22audiobook%22" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"ID\":1,\"TITLE\":\"fallen audiobook\",\"AUTHOR\":\"A author\",\"NARRATOR\":\"A Narrator\",\"DURATION\":4563,\"UPLOAD_TIME\":\"2021-02-24 03:35:05\"}"


#GET request for song:
- curl -X GET "http://127.0.0.1:8000/song/1" -H  "accept: application/json"

#GET request for podcast:
- curl -X GET "http://127.0.0.1:8000/podcast/1" -H  "accept: application/json"

#GET request for audiobook:
- curl -X GET "http://127.0.0.1:8000/audioBook/1" -H  "accept: application/json"

#DELETE request for song:
- curl -X DELETE "http://127.0.0.1:8000/song/1" -H  "accept: application/json"

#DELETE request for podcast:
- curl -X DELETE "http://127.0.0.1:8000/podcast/1" -H  "accept: application/json"

#DELETE request for audiobook:
- curl -X DELETE "http://127.0.0.1:8000/audioBook/1" -H  "accept: application/json"

#PATCH request for song:
- curl -X PATCH "http://127.0.0.1:8000/song/1" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"ID\":1,\"NAME\":\"fallen\",\"DURATION\":500,\"UPLOAD_TIME\":\"2021-02-22 03:34:05\"}"


#PATCH request for podcast:
- curl -X PATCH "http://127.0.0.1:8000/podcast/1" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"ID\":1,\"NAME\":\"fallen podcast\",\"DURATION\":100,\"UPLOAD_TIME\":\"2021-02-22 03:35:05\",\"HOST\":\"update host\",\"PARTICIPANTS\":[\"fallen\"]}"


#PATCH request for audiobook:
- curl -X PATCH "http://127.0.0.1:8000/audiobook/1" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"ID\":1,\"TITLE\":\"fallen audiobook\",\"AUTHOR\":\"A author\",\"NARRATOR\":\"A Narrator\",\"DURATION\":4563,\"UPLOAD_TIME\":\"2021-02-22 03:35:05\"}"
 

