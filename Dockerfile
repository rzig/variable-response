FROM python:3.8

RUN useradd --create-home appuser
USER appuser

WORKDIR /app
COPY . .

RUN pip install flask

EXPOSE 3001

ENTRYPOINT ["python3"]
CMD ["server.py"]
