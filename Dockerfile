FROM python:3.12

# Set CWD & copy files
WORKDIR /usr/src/app
COPY . .

# Install system dependencies
RUN apt-get update
RUN apt-get install -y virtualenv 

# Install requirements
RUN make install

CMD [ "make", "run" ]