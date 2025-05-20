FROM python:3.13.3-slim

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD [ "streamlit", "run", "Main.py" ] 