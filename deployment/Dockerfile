# Use the official Nginx image as a base image
FROM nginx:alpine

COPY build/index.html /usr/share/nginx/html/
COPY build/favicon.ico /usr/share/nginx/html/
COPY build/logo192.png /usr/share/nginx/html/
COPY build/logo512.png /usr/share/nginx/html/
COPY build/manifest.json /usr/share/nginx/html/
COPY build/robots.txt /usr/share/nginx/html/
COPY build/static/css /usr/share/nginx/html/css/
COPY build/static/js /usr/share/nginx/html/js/
COPY build/asset-manifest.json /usr/share/nginx/html/
COPY build/_redirects /usr/share/nginx/html/

# Expose port 80 to allow outside access
EXPOSE 80

# Command to start the Nginx server
CMD ["nginx", "-g", "daemon off;"]
