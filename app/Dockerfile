#FROM python:3.9
#
#WORKDIR /var/task
#
#COPY ./requirements.txt /var/task/requirements.txt
#
#RUN pip install --no-cache-dir --upgrade -r /var/task/requirements.txt


FROM python:3.9-slim

RUN apt-get update
RUN apt-get -y --no-install-recommends install procps nginx vim curl && apt-get install -y openssh-client
RUN apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*


WORKDIR /var/task
COPY requirements.txt /var/task/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt -U
COPY . /var/task/app
# RUN mkdir -p /var/task/app
# COPY . /var/task/app
RUN echo "alias egrep='egrep --color=auto'" >> ~/.bashrc
RUN echo "alias fgrep='fgrep --color=auto'" >> ~/.bashrc
RUN echo "alias grep='grep --color=auto'" >> ~/.bashrc
RUN echo "alias l='ls -CF'" >> ~/.bashrc
RUN echo "alias la='ls -A'" >> ~/.bashrc
RUN echo "alias ll='ls -alF'" >> ~/.bashrc
RUN echo "alias ls='ls --color=auto'" >> ~/.bashrc

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/var/task:${PATH}"
ENV PS1="[\u@\h \w]\\$ "
ENV TZ=Asia/Seoul

ENV PYTHONPATH='/var/task'

#CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
