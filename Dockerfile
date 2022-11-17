FROM python:3.8
COPY Exe_1_python.py ./
EXPOSE 8080
CMD ["python", "./Exe_1_python.py"]
