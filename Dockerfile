FROM python:3
RUN apt-get update && apt-get install -y \
	nginx
WORKDIR /app
COPY server1.py ./
COPY server2.py ./
COPY run.sh ./
COPY configs/nginx.conf /etc/nginx/nginx.conf
EXPOSE  81
CMD /app/run.sh
