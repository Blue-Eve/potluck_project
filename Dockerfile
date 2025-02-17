FROM python:3.10.6-slim

WORKDIR /prod

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY data data
COPY potluck_code potluck_code
COPY style style
COPY app.py app.py
COPY .streamlit .streamlit
COPY setup.py setup.py
RUN pip install .
ENV NLTK_DATA=data

CMD streamlit run app.py --server.port $PORT --server.address 0.0.0.0
