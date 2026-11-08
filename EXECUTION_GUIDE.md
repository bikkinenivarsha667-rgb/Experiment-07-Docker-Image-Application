# Experiment 07 – Develop a Simple Containerized Application Using Docker

## 1. Check Software Installations

```powershell
docker --version
docker ps
```

## 2. Start Docker Desktop

1. Open Docker Desktop.
2. Wait until Docker Engine is running.
3. Open VS Code → Terminal → New Terminal.

## 3. Open the Project

1. Open the GitHub repository.
2. Click Code → Download ZIP.
3. Extract the ZIP file.
4. Create a folder using the name given by your faculty.
5. Open the extracted project folder in VS Code.
6. Open Terminal → New Terminal.

## 4. Check Project Files

```powershell
dir
```

Check that these files and folders are available:

- Dockerfile
- hello.py
- app
- app/image.jpg

## 5. Build Docker Image

```powershell
docker build -t myimage .
```

Expected output:

```text
Successfully built
Successfully tagged myimage:latest
```

## 6. Verify Docker Image

```powershell
docker images
```

Check that `myimage` is available.

## 7. Run Docker Container

```powershell
docker run -d --name mycontainer -p 8000:8000 myimage
```

This creates and starts a container in detached mode.

## 8. Check Running Containers

```powershell
docker ps
```

Check that `mycontainer` is running and port 8000 is mapped.

## 9. Check Container Logs

```powershell
docker logs mycontainer
```

## 10. Open Application in Chrome

Open:

http://localhost:8000

Expected output:

- Hello World!
- My First Containerized Application
- The selected picture (image.jpg).

## 11. Important Notes

1. Docker Desktop must be running.
2. The Dockerfile must be in the project root folder.
3. The hello.py file must be available.
4. The image.jpg file must be inside the app folder.
5. Build the image before running the container.
6. Use port 8000 to access the application.
7. If the container name already exists, remove the old container before creating another one.

## 12. Clean Up (If Required)

```powershell
docker stop mycontainer
docker rm mycontainer
```

## Result

A simple Python application displaying Hello World and an image is successfully containerized and executed using Docker.
