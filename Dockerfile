FROM locustio/locust

# RUN pip3 install --no-cache-dir --upgrade pip && \
# RUN pip3 install python3-dotenv
RUN python -m pip install --upgrade pip

RUN pip install python-dotenv