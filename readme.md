# text-similarity

## Deploy with Docker Locally

Build image

    docker build --network=host -t text-similarity:v0 .

Run Docker

    docker run --name text-similarity -p 5000:5000 -d text-similarity:v0

## Deploy with SSL on VPS

Obtain domain name and SSL certificate, configure DNS, open the corresponding port on the firewall

Create Venv

    python3 -m venv txt-sim # ubuntu 22.04, python 3.10
    source txt-sim/bin/activate
    # pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
    pip install Flask==3.0.2 scikit-learn==1.4.1.post1 Levenshtein==0.25.0 simhash==2.1.2

Run text-similarity

    python app.py

Nginx listens on port 80 and implements access link mandatory ssl

    docker run -v ./nginx.conf:/etc/nginx/conf.d/default.conf -v ./sim.ppeak.site_bundle.crt:/etc/nginx/ssl/certificate.crt -v ./sim.ppeak.site.key:/etc/nginx/ssl/private_key.key -p 80:80 -p 443:443 -d nginx 
    
Nginx Docker Version

/home/ubuntu# docker image inspect nginx:latest | grep -i version

        "DockerVersion": "",
                "NGINX_VERSION=1.25.4",
                "NJS_VERSION=0.8.3",
/home/ubuntu# docker version

    Client: Docker Engine - Community
     Version:           26.0.0-rc1
     API version:       1.45
     Go version:        go1.21.6

