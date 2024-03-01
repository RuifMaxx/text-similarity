# text-similarity

## Deploy with Docker Locally

Build image

    docker build --network=host -t text-similarity:v0 .

Run Docker

    docker run --name text-similarity -p 80:80 -d text-similarity:v0

## Deploy with SSL on VPS

Obtain domain name and SSL certificate, configure DNS, open the corresponding port on the firewall

Run text-similarity

    python app.py

nginx listens on port 80 and forwards to text-similarity service

    docker run -v nginx.conf:/etc/nginx/nginx.conf -p 80:80 -d nginx 
    
