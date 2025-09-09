# YouTube Script Generator

## Overview
The YouTube Script Generator is the first step toward developing a complete AI-powered system for automating YouTube content creation and channel management. This project focuses on generating high-quality, context-aware, and ad-free YouTube scripts by extracting and preprocessing video transcripts, then fine-tuning a large language model. It forms the foundation for a larger vision involving automated voice-overs, video compilation, and full content publishing.

## Objectives
- Automate the generation of high-quality YouTube scripts.  
- Prepare and clean real-world YouTube transcripts into structured datasets.  
- Fine-tune a large language model using Parameter Efficient Fine-Tuning (PEFT) with LoRA.  
- Remove sponsorship and advertisement content from transcripts using semantic similarity techniques.  
- Explore deployment strategies through Hugging Face hosting for inference and API integration.

## Architecture & Workflow (Summary)
The system operates in three main stages:  
1. **Transcript Extraction:** Takes YouTube URLs as input, extracts transcripts, and generates concise summaries using Gemini 2.0 Flash, storing the data in JSON format.  
2. **Data Preparation:** Normalizes transcripts, removes unwanted characters and filler tags, and eliminates sponsorship/advertisement lines using sentence embeddings and cosine similarity.  
3. **Fine-Tuning:** Converts cleaned transcripts into prompt–script pairs, chunks text to maintain context, and fine-tunes a large language model using PEFT with LoRA. Fine-tuned weights are merged with the base model for deployment.

## Tech Stack

## Tech Stack

**Tech Stack**  
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)  

**Frameworks**  
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)  
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)  

**Libraries**  
[![Hugging Face](https://img.shields.io/badge/HuggingFace-FDAF0A?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/)  
[![PEFT + LoRA](https://img.shields.io/badge/PEFT-LoRA-4B9CE2?style=for-the-badge)](#)  
[![Spacy](https://img.shields.io/badge/Spacy-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)](https://spacy.io/)  
[![SentenceTransformers](https://img.shields.io/badge/SentenceTransformers-FF6F61?style=for-the-badge)](https://www.sbert.net/)  

**Models**  
[![Gemini 2.0 Flash](https://img.shields.io/badge/Gemini2.0-9C27B0?style=for-the-badge)](#)  
[![Gemma-3-270m-it](https://img.shields.io/badge/Gemma3-270M-FF9800?style=for-the-badge)](#)  

**Platforms**  
[![Google Colab](https://img.shields.io/badge/Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://colab.research.google.com/)  
[![Hugging Face Hub](https://img.shields.io/badge/HuggingFaceHub-FDAF0A?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/)



## Challenges & Solutions
- **Noisy transcripts:** Solved by building a custom normalization pipeline.  
- **Sponsorship content in transcripts:** Removed using embeddings and cosine similarity.  
- **Unsatisfactory results from Flan-T5:** Experimented with larger models, selecting Gemma-3-1b-it.  
- **Limitations of free model hosting on Hugging Face:** Planning to fine-tune smaller, deployable models.  
- **Limited GPU resources:** Managed using PEFT, LoRA, and quantization techniques.

## Future Scope
- Fine-tune smaller models for Hugging Face-hosted API integration.  
- Expand beyond script generation to include:  
  - Automatic voice-over generation  
  - Image and thumbnail generation  
  - Video compilation  
- Develop a fully agentic AI system capable of end-to-end YouTube content creation and channel management.
