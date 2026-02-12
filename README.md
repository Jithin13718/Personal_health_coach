#  Personal Health Coach Agent

A modular, extensible AI-powered **personal health coach agent** that ingests health data, normalizes it, generates recommendations, and delivers empathetic coaching responses.

Designed with **clean architecture**, **developer experience**, and **scalability** in mind.
-  Modular agent-based architecture
-  Ingestion from wearables & manual inputs
-  Unified health data normalization
-  Trend compression (rolling averages)
-  Rule-based + ML-ready recommendation engine
-  Conversational coaching layer
-  Developer-friendly, extensible codebase

## Architecture Overview
Ingestion → Core → Recommender → Coach → Output
### Layers
- **Ingestion**: Collects raw health data
- **Core**: Normalizes & compresses metrics
- **Recommender**: Generates actionable insights
- **Coach**: Produces empathetic responses
- **Utils**: Logging & configuration
- **Docs**: Architecture & usage guides

---

## Running the Agent
python main.py

## Sample Output
Health Coach Response:
You’ve got this  Small steps today lead to big results.
You’re a bit low on movement today. A 15–20 min walk would help.

