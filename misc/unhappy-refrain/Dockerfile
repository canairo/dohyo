FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
  xinetd gcc \
  && rm -rf /var/lib/apt/lists/*

RUN useradd unhappy

RUN mkdir -m 777 /app
COPY flag.txt /
COPY jail.py /app/
COPY jail.xinetd /etc/xinetd.d/jail
COPY getflag.c /tmp/getflag.c 

RUN gcc /tmp/getflag.c -o /app/getflag && \
    chown root:root /app/getflag && chmod 4755 /app/getflag && \
    chmod 400 /flag.txt && chown root:root /flag.txt && \
    rm /tmp/getflag.c

WORKDIR /app
EXPOSE 1337

CMD ["xinetd", "-dontfork"]
