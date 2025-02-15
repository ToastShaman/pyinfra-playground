build:
    docker build -t ssh_server_image .

run:
    docker run -p 2222:22 --name ssh_server_container ssh_server_image

ssh:
    ssh root@localhost -p 2222

deploy ENV:
    pdm run pyinfra inventories/{{ENV}}.py deploy.py

fmt:
    pdm run ruff format **/*.py
