FROM nginx:latest

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
COPY project.conf /etc/nginx/conf.d/
#COPY local.conf /etc/nginx/conf.d/