FROM python:3.10
ENV PYTHONUNBUFFERED 1

# Configura o locale para pt_BR.UTF-8
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
	&& localedef -i pt_BR -c -f UTF-8 -A /usr/share/locale/locale.alias pt_BR.UTF-8
ENV LANG pt_BR.UTF-8
ENV LC_ALL pt_BR.UTF-8

#Web pdb
EXPOSE 5555
ENV PYTHONBREAKPOINT=web_pdb.set_trace

RUN mkdir /code
WORKDIR /code
COPY requirements.dev.txt requirements.dev.txt

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN python3 -m pip install --no-cache-dir -r requirements.dev.txt

COPY . .
# Set the locale
