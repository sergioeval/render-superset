# Render Superset

A custom Apache Superset Docker image optimized for deployment on Render.

## Features

- Based on official Apache Superset image
- Environment variable configuration
- Redis caching support
- Celery task queue integration
- Security best practices
- Render-optimized configuration

## Deployment on Render

### 1. Create a New Web Service

1. Connect your GitHub repository to Render
2. Create a new **Web Service**
3. Select your repository
4. Configure the service:
   - **Name**: `superset` (or your preferred name)
   - **Environment**: `Docker`
   - **Region**: Choose closest to your users
   - **Branch**: `main` (or your default branch)
   - **Root Directory**: Leave empty (if files are in root)

### 2. Environment Variables

Set these environment variables in your Render service:

#### Required Variables
```bash
# Database (use Render's managed PostgreSQL)
DATABASE_URL=postgresql://user:password@host:port/database

# Security
SECRET_KEY=your-very-long-secret-key-here
```

#### Optional Variables
```bash
# Admin user configuration
SUPERSET_ADMIN_USERNAME=admin
SUPERSET_ADMIN_FIRSTNAME=Superset
SUPERSET_ADMIN_LASTNAME=Admin
SUPERSET_ADMIN_EMAIL=admin@yourdomain.com
SUPERSET_ADMIN_PASSWORD=your-secure-password

# Redis configuration (for caching and Celery)
REDIS_HOST=your-redis-host
REDIS_PORT=6379
REDIS_CELERY_DB=0
REDIS_RESULTS_DB=1
REDIS_CACHE_DB=2

# Security settings
SESSION_COOKIE_SECURE=true
WEBDRIVER_BASEURL=https://your-app-name.onrender.com/
WEBDRIVER_BASEURL_USER_FRIENDLY=https://your-app-name.onrender.com/
```

### 3. Generate Secret Key

Generate a secure secret key:
```bash
openssl rand -base64 42
```

### 4. Database Setup

For production, use Render's managed PostgreSQL service:
1. Create a new **PostgreSQL** service in Render
2. Copy the connection string to your `DATABASE_URL` environment variable
3. The database will be automatically initialized on first run

### 5. Redis (Optional but Recommended)

For better performance, add a Redis service:
1. Create a new **Redis** service in Render
2. Use the connection details in your environment variables

## Local Development

### Prerequisites
- Docker
- Docker Compose (optional)

### Quick Start
```bash
# Build the image
docker build -t render-superset .

# Run with environment variables
docker run -p 8088:8088 \
  -e DATABASE_URL=sqlite:///superset.db \
  -e SECRET_KEY=your-secret-key \
  render-superset
```

### Using Docker Compose
Create a `docker-compose.yml` file:
```yaml
version: '3.8'
services:
  superset:
    build: .
    ports:
      - "8088:8088"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/superset
      - SECRET_KEY=your-secret-key
      - REDIS_HOST=redis
    depends_on:
      - db
      - redis
  
  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=superset
      - POSTGRES_USER=superset
      - POSTGRES_PASSWORD=superset
    volumes:
      - postgres_data:/var/lib/postgresql/data
  
  redis:
    image: redis:6-alpine

volumes:
  postgres_data:
```

## Configuration

The `superset_config.py` file contains all the configuration settings. Key features:

- **Database**: Configurable via `DATABASE_URL`
- **Caching**: Redis-based caching
- **Security**: CSRF protection, secure cookies
- **Features**: Native filters, RBAC, template processing
- **Logging**: File-based logging with rotation

## Troubleshooting

### Common Issues

1. **Database Connection Errors**
   - Ensure `DATABASE_URL` is correctly formatted
   - Check if database service is running
   - Verify network connectivity

2. **Permission Errors**
   - Ensure proper file permissions on `bootstrap.sh`
   - Check if user has write access to mounted volumes

3. **Port Issues**
   - Render automatically sets the `PORT` environment variable
   - The app listens on `0.0.0.0` to accept external connections

4. **Memory Issues**
   - Superset can be memory-intensive
   - Consider increasing Render's memory allocation
   - Monitor resource usage in Render dashboard

### Logs

Check Render logs for detailed error information:
- Go to your service dashboard
- Click on "Logs" tab
- Look for error messages during startup

## Security Considerations

1. **Change Default Passwords**: Always change the default admin password
2. **Use HTTPS**: Enable `SESSION_COOKIE_SECURE` in production
3. **Secret Key**: Use a strong, unique secret key
4. **Database**: Use managed databases with proper access controls
5. **Environment Variables**: Never commit secrets to version control

## Performance Optimization

1. **Redis**: Use Redis for caching and Celery tasks
2. **Database**: Use managed PostgreSQL for better performance
3. **Memory**: Allocate sufficient memory in Render
4. **Caching**: Configure appropriate cache timeouts

## Support

For issues specific to this deployment:
- Check the [Apache Superset documentation](https://superset.apache.org/docs/intro)
- Review [Render documentation](https://render.com/docs)
- Check logs for specific error messages
