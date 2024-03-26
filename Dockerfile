FROM python:slim

WORKDIR /app

COPY bot/requirements.txt bot/requirements.txt
RUN pip install -r bot/requirements.txt

COPY bot bot

# -u for unbuffered stderr and stdout
CMD [ "python", "-u", "bot/main.py" ]
