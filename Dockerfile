# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /github_repos
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /github_repos/