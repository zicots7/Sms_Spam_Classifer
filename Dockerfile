# based image is used that is python 3.13.o
FROM python:3.13.0-slim
# set up working directory
WORKDIR /app
# copy current working directory into the container at /app
COPY . /app
# install any required dependencies
RUN pip install --no-cache-dir -r requirement.txt
# Download NLTK punkt data
RUN python -m nltk.downloader punkt_tab
# Expose the port to run the app
EXPOSE 8501
# run application in python using streamlit
CMD ["streamlit","run","app.py"]