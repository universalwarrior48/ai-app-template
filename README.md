# AI Application Template

[![CI](https://github.com/universalwarrior48/ai-app-template/actions/workflows/test.yml/badge.svg)](https://github.com/universalwarrior48/ai-app-template/actions/workflows/test.yml)
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://github.com/universalwarrior48/ai-app-template/actions/workflows/test.yml)

A comprehensive template for building AI applications with FastAPI backend, Gradio UI, and Hugging Face Spaces deployment.

## Features

- **Modular Architecture**: Clean separation between UI, API, core logic, models, and services
- **FastAPI Backend**: RESTful API endpoints with Pydantic models
- **Gradio UI**: Interactive web interface for AI applications
- **Configuration Management**: Pydantic-based settings with environment file support
- **Testing Framework**: Comprehensive test suite using pytest
- **Container Support**: Dockerfile with health checks and non-root user
- **Hugging Face Deployment**: GitHub Actions workflow for automatic Space deployment
- **Development Tools**: Black, MyPy, and pytest configuration

## Project Structure

```
ai-app-template/
├── app/                    # Main application code
│   ├── main.py            # Application entry point
│   ├── api/               # FastAPI endpoints
│   │   └── routes.py
│   ├── core/              # Business logic
│   │   ├── config.py
│   │   ├── inference.py
│   │   └── pipeline.py
│   ├── models/            # Model management
│   │   └── model_loader.py
│   ├── services/          # External integrations
│   │   ├── cache.py
│   │   └── vector_db.py
│   └── ui/                # Gradio interface
│       └── interface.py
├── tests/                 # Test suite
│   ├── test_api.py
│   ├── test_inference.py
│   └── test_pipeline.py
├── requirements.txt       # Python dependencies
├── Dockerfile            # Containerization
├── .env                  # Environment variables
├── pyproject.toml        # Project configuration
└── .github/workflows/    # GitHub Actions
    └── deploy.yml        # Hugging Face Spaces deployment
```

## 🌟 Live Demo

**Try the template in action!** Visit our [Hugging Face Space](https://huggingface.co/spaces/ai-app-template-demo) to see the template working before you fork it.

This live demo shows:
- ✅ FastAPI endpoints working correctly
- ✅ Gradio interface functionality
- ✅ Complete CI/CD pipeline validation
- ✅ Template structure and organization

## Quick Start

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd ai-app-template
pip install -r requirements.txt
```

### 2. Configure Environment

Copy `.env.example` to `.env` and configure your settings:

```bash
cp .env .env.local
# Edit .env.local with your configuration
```

### 3. Run the Application

**Development (API + UI):**
```bash
# Start FastAPI server
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Start Gradio UI
python app/ui/interface.py

# Start Hugging Face Space interface
python app/main.py
```

**Docker:**
```bash
docker build -t ai-app .
docker run -p 8000:8000 ai-app
```

## Hugging Face Spaces Deployment

This template includes automatic deployment to Hugging Face Spaces via GitHub Actions.

**Note:** This is a template repository. The workflows are configured to skip execution in the template itself. When you fork this repository, the workflows will automatically activate for your forked repository.

### 🚀 Quick Setup Guide

#### Step 1: Create Hugging Face Account
1. Go to [Hugging Face](https://huggingface.co/join) and create an account
2. Verify your email address
3. Sign in to your account

#### Step 2: Generate Hugging Face Access Token
1. **Navigate to Settings**: 
   - Click on your profile icon in the top-right corner
   - Select "Settings" from the dropdown menu

2. **Access Tokens Page**:
   - In the left sidebar, click on "Access Tokens"
   - This page shows all your existing tokens

3. **Create New Token**:
   - Click the "New token" button
   - Fill in the form:
     - **Token name**: Give it a descriptive name (e.g., "GitHub Actions Deployment")
     - **Role**: Select "Write" (required for creating/updating spaces)
   - Click "Generate a token"

4. **Copy Your Token**:
   - **IMPORTANT**: Copy the token immediately and save it securely
   - This is the only time you'll see the full token value
   - Store it in a password manager or secure location

#### Step 3: Configure GitHub Repository Secrets
1. **Go to Repository Settings**:
   - Navigate to your GitHub repository
   - Click on "Settings" tab
   - In the left sidebar, click "Secrets and variables" → "Actions"

2. **Add New Secret**:
   - Click "New repository secret"
   - Fill in the form:
     - **Name**: `HUGGINGFACE_TOKEN`
     - **Secret**: Paste your Hugging Face access token
   - Click "Add secret"

#### Step 4: Create Hugging Face Space (Optional)
**Automatic Creation**: The GitHub Actions workflow can automatically create your space when you push to the main branch.

**Manual Creation** (if preferred):
1. Go to [Hugging Face Spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. **Repository name**: Must match your GitHub repository name exactly
4. **SDK**: Select "Gradio" (recommended for this template)
5. **License**: Choose appropriate license
6. Click "Create Space"

#### Step 5: Deploy Your Application
1. **Push to Main Branch**:
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push origin main
   ```

2. **Monitor Deployment**:
   - Go to your repository's "Actions" tab
   - Watch the "Deploy to Hugging Face Spaces" workflow
   - Check the logs for deployment status

3. **Access Your Space**:
   - Once deployed, access your space at: `https://huggingface.co/spaces/your-username/your-repo-name`
   - The space will automatically update on future pushes to main/master

### 🔧 Troubleshooting

#### Common Issues

**❌ "HF_TOKEN is missing" Error**
- **Cause**: GitHub secret not configured properly
- **Solution**: 
  1. Verify the secret name is exactly `HUGGINGFACE_TOKEN`
  2. Ensure the token value is copied correctly
  3. Check that the secret is added to the correct repository

**❌ "Permission denied" Error**
- **Cause**: Token doesn't have write permissions
- **Solution**: Regenerate token with "Write" role selected

**❌ Space not found**
- **Cause**: Repository name mismatch
- **Solution**: Ensure your GitHub repository name matches the Hugging Face space name

**❌ Deployment fails**
- **Cause**: Application structure issues
- **Solution**: Check that all required files exist (`app/main.py`, `requirements.txt`, etc.)

#### Verification Steps

1. **Test Token Validity**:
   ```bash
   curl -H "Authorization: Bearer YOUR_HF_TOKEN" https://huggingface.co/api/whoami-v2
   ```

2. **Check GitHub Secret**:
   - Go to repository Settings → Secrets
   - Verify `HUGGINGFACE_TOKEN` exists and has a value

3. **Validate Space Name**:
   - GitHub repo: `your-username/ai-app-template`
   - HF Space should be: `your-username/ai-app-template`

#### Security Best Practices

- 🔒 **Never commit tokens to your repository**
- 🔒 **Use descriptive token names** for easy identification
- 🔒 **Rotate tokens regularly** for security
- 🔒 **Limit token permissions** to only what's needed (Write access)

### 📋 Deployment Checklist

- [ ] Hugging Face account created
- [ ] Access token generated with Write permissions
- [ ] GitHub secret `HUGGINGFACE_TOKEN` configured
- [ ] Repository pushed to main/master branch
- [ ] GitHub Actions workflow triggered
- [ ] Space deployed successfully
- [ ] Application accessible at HF Space URL

### 🔄 Automatic Updates

Once configured, your Hugging Face Space will automatically update when:
- You push to the `main` or `master` branch
- You create a pull request to main/master
- The GitHub Actions workflow completes successfully

The deployment process includes:
1. Code quality validation (Black, Flake8, MyPy)
2. Security scanning (Bandit, Safety)
3. Test suite execution
4. Application deployment to Hugging Face Spaces

## Configuration

### Environment Variables

Edit `.env` file to configure your application:

```bash
# Application settings
APP_NAME=AI Application
DEBUG=false

# Model settings
MODEL_NAME=default-model
# MODEL_PATH=/path/to/model

# API settings
API_HOST=0.0.0.0
API_PORT=8000

# UI settings
UI_PORT=7860

# Vector database settings
VECTOR_DB_URL=http://localhost:8000
CACHE_TTL=3600
```

### Dependencies

The template includes essential dependencies for a basic AI application. Optional dependencies are commented out for you to enable as needed:

```txt
# Core dependencies (essential)
fastapi==0.104.1
uvicorn[standard]==0.24.0

# UI dependencies (essential)
gradio==4.27.0

# Configuration and utilities (essential)
pydantic==2.5.0
python-dotenv==1.0.0

# Testing (essential)
pytest==9.0.2
httpx==0.28.1

# Optional dependencies - uncomment based on your needs:

# Data processing (optional)
# numpy==1.24.4
# pandas==2.1.3

# ML/AI dependencies (optional - heavy dependencies)
# torch==2.10.0
# transformers==5.3.0
# sentence-transformers==5.3.0

# Vector database (optional - uncomment as needed)
# pinecone-client==2.2.4
# weaviate-client==3.25.10
# chromadb==0.4.1

# Caching (optional - uncomment as needed)
# redis==5.0.1
# python-memcached==1.59

# Development tools (optional - uncomment as needed)
# black==26.3.1
# flake8==7.3.0
# mypy==1.7.1
```

#### Dependency Categories:

**Essential Dependencies** (always included):
- **FastAPI + Uvicorn**: Web framework and ASGI server
- **Gradio**: Interactive UI framework
- **Pydantic + python-dotenv**: Configuration management
- **pytest + httpx**: Testing framework

**Optional Dependencies** (uncomment as needed):
- **Data Processing**: `numpy`, `pandas` for data manipulation
- **ML/AI**: `torch`, `transformers`, `sentence-transformers` for machine learning
- **Vector Database**: `pinecone-client`, `weaviate-client`, `chromadb` for vector storage
- **Caching**: `redis`, `python-memcached` for caching solutions
- **Development Tools**: `black`, `flake8`, `mypy` for code quality

#### Quick Start with Minimal Dependencies:
```bash
pip install -r requirements.txt  # Installs only essential dependencies
```

#### Adding Optional Dependencies:
```bash
# Uncomment the dependencies you need in requirements.txt, then:
pip install -r requirements.txt
```

## Development

### Code Style

The project includes configuration for:
- **Black**: Code formatting
- **MyPy**: Type checking
- **Flake8**: Linting

#### Running Code Quality Checks

Install development dependencies:
```bash
pip install -r requirements.txt
pip install black flake8 mypy
```

Run formatting and checks:
```bash
# Check code formatting with Black
black --check --diff app/ tests/

# Format code with Black
black app/ tests/

# Run Flake8 linting (uses .flake8 configuration)
flake8 app/ tests/

# Run MyPy type checking
mypy app/ --ignore-missing-imports
```

#### Pre-commit Hook Setup

For automatic formatting and quality checks before commits, install pre-commit:

```bash
pip install pre-commit
pre-commit install
```

The template includes a comprehensive `.pre-commit-config.yaml` with:
- **Black**: Automatic code formatting
- **Flake8**: Code linting with .flake8 configuration
- **MyPy**: Static type checking
- **isort**: Import sorting
- **Security checks**: Bandit security linting
- **File validation**: YAML, JSON, TOML validation
- **General checks**: Trailing whitespace, end-of-file fixes

Run pre-commit manually:
```bash
# Run on all files
pre-commit run --all-files

# Run on specific files
pre-commit run black --files app/main.py
```

Update pre-commit hooks:
```bash
pre-commit autoupdate
```

Now your code will be automatically formatted and checked before each commit!

### Testing

Run the test suite:
```bash
pytest
pytest -v  # Verbose output
pytest tests/test_api.py  # Run specific test file
```

### Adding New Features

1. **API Endpoints**: Add to `app/api/routes.py`
2. **Business Logic**: Implement in `app/core/`
3. **Models**: Add model classes to `app/models/`
4. **Services**: External integrations in `app/services/`
5. **UI Components**: Update `app/ui/interface.py`
6. **Tests**: Add corresponding tests in `tests/`

## Docker Deployment

Build and run with Docker:

```bash
# Build image
docker build -t ai-app-template .

# Run container
docker run -p 8000:8000 ai-app-template

# Run with environment variables
docker run -p 8000:8000 -e DEBUG=true ai-app-template
```

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for your changes
5. Submit a pull request

## Support

For issues and questions:
- Create a GitHub issue
- Check the [Hugging Face documentation](https://huggingface.co/docs)
- Review FastAPI and Gradio documentation