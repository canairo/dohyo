FROM debian:12
WORKDIR /srv/app

RUN addgroup --gid 1001 nonroot && \
  adduser --uid 1001 --gid 1001 --disabled-password --gecos "" nonroot && \
  echo 'nonroot ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

RUN apt-get update && apt-get install -y --no-install-recommends socat patchelf && rm -rf /var/lib/apt/lists/*


COPY ./chal /srv/app/run
COPY ./libc.so.6 /srv/app/libc.so.6
COPY ./ld-linux-x86-64.so.2 /srv/app/ld-linux-x86-64.so.2
COPY ./entry.sh /srv/app/entry.sh
RUN echo "DOHYO{$(head -n 32 /dev/urandom | od -A n -t x | head -n 1 | tr -d ' ')}" > /srv/app/flag.txt
RUN chmod 555 /srv/app/run \
  && chmod 444 /srv/app/flag.txt \
  && chmod 555 /srv/app/entry.sh \
  && chmod 555 /srv/app/libc.so.6 \
  && chmod 555 /srv/app/ld-linux-x86-64.so.2

WORKDIR /srv/app
RUN patchelf --set-interpreter ./ld-linux-x86-64.so.2 --set-rpath '$ORIGIN' run
USER 1001
EXPOSE 8080
CMD [ "/srv/app/entry.sh" ]
