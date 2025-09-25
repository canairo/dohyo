FROM --platform=linux/amd64 python:3.11-slim-bookworm

WORKDIR /challf

RUN pip3 install pycryptodome
COPY main.py .
COPY ynetd .

RUN chmod +x main.py
RUN chmod +x ynetd

EXPOSE 8000

CMD ./ynetd -p 8000 "python3 main.py"
