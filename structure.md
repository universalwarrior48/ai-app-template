ai-app/
│
├── app/
│   ├── ui/                 # Gradio layer
│   │   └── interface.py
│   │
│   ├── api/                # FastAPI endpoints
│   │   └── routes.py
│   │
│   ├── core/               # business logic
│   │   ├── inference.py
│   │   ├── pipeline.py
│   │   └── config.py
│   │
│   ├── models/             # model loading / wrappers
│   │   └── model_loader.py
│   │
│   ├── services/           # external integrations
│   │   ├── vector_db.py
│   │   └── cache.py
│   │
│   └── main.py             # app entrypoint
│
├── tests/
│   ├── test_api.py
│   ├── test_inference.py
│   └── test_pipeline.py
│
├── requirements.txt
├── Dockerfile
├── .env
└── pyproject.toml
