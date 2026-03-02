FROM python:3.12-slim

# Set CWD & copy files
WORKDIR /usr/src/app
COPY . .

# Install requirements
RUN pip install -r requirements.txt

CMD [ "python", "bot.py" ]