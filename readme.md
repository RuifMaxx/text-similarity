# text-similarity

## Deploy with Docker Locally

Build image

    docker build --network=host -t text-similarity:v0 .

Run Docker

    docker run --name text-similarity -p 80:80 -d text-similarity:v0