# Stage 1: Build the MkDocs site
FROM ghcr.io/astral-sh/uv:python3.12-alpine AS builder

WORKDIR /mkdocs

# Install dependancies
COPY pyproject.toml uv.lock /mkdocs/
RUN uv sync

# Copy the MkDocs project files
COPY . /mkdocs

# Build the MkDocs site
RUN uv run mkdocs build

# Stage 2: Serve the MkDocs site with Nginx
FROM nginx:alpine

# Copy the built site from the builder stage
COPY --from=builder /mkdocs/site /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]