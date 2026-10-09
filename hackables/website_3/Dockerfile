FROM python:3.12-slim
WORKDIR /app
COPY ./ ./
RUN pip install flask
RUN pip install requests
CMD ["flask", "--app", "site3", "run", "--host", "0.0.0.0", "--port", "5000"]