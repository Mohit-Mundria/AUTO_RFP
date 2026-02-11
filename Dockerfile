FROM python:3.13
COPY . .
COPY requirements.txt .
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 7860
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
