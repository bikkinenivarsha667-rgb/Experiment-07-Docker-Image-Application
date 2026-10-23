\# Experiment 7: Develop a Simple Containerized Application Using Docker



\## Aim

To develop and run a simple containerized application using Docker that displays Hello World and a picture in a web browser.



\## Requirements

\- Docker Desktop

\- Python 3.9 Docker image

\- PowerShell

\- Web browser



\## Files Used

\- `hello.py` – Python application that serves a web page.

\- `Dockerfile` – Defines the Docker image configuration.

\- `app/image.jpg` – Picture displayed by the application.



\## Procedure

1\. Create the Python application in `hello.py`.

2\. Add the picture inside the `app` directory.

3\. Create a Dockerfile using the Python 3.9 base image.

4\. Build the Docker image.

5\. Run a container and map port 8000.

6\. Open the application in a web browser.



\## Docker Commands



```powershell

docker build -t myimage .

docker run -d --name mycontainer -p 8000:8000 myimage

docker ps

docker logs mycontainer

```



\## Output

The application displays “Hello World!”, “My First Containerized Application”, and the selected picture at `http://localhost:8000`.



\## Result

A simple Python application containing text and a picture was successfully containerized and executed using Docker.



