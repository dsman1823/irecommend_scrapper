FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
ARG AWS_SECRET_KEY
ARG AWS_ACCESS_KEY
CMD [ "python3", "./go-spider.py", "$AWS_ACCESS_KEY",  "$AWS_SECRET_KEY"]