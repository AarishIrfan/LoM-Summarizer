# LoM Summarizer

This is a [Next.js](https://nextjs.org) + FastAPI project that summarizes Letters of Motivation (LoM), extracts keywords, and identifies strengths using AI. The frontend is built with React, TypeScript, TailwindCSS, and Framer Motion, while the backend uses FastAPI and lightweight AI models. PDF generation is included for download.

## Tech Stack

- **Frontend**: React, Next.js, TypeScript, TailwindCSS, Framer Motion  
- **Backend**: FastAPI, PyMuPDF, python-docx, ReportLab  
- **AI / ML**: Transformers (`distilbart-cnn-12-6`) for summarization, custom keyword & strengths logic  
- **Deployment (planned)**: Docker (backend), Vercel (frontend)  

## Getting Started

First, install dependencies and run the development server:

### Frontend
```bash
cd frontend
npm install
npm run dev
# or
yarn dev
# or
pnpm dev
````

Open [http://localhost:3000](http://localhost:3000) in your browser to see the frontend.

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to check the FastAPI backend.

---

## Usage

1. Choose one or multiple `.pdf` or `.docx` files in the frontend.
2. Click **Upload & Summarize** to process the files.
3. View:

   * **Preview** of text
   * **AI-generated Summary**
   * **Extracted Keywords**
   * **Inferred Strengths**
4. Download the results as a **PDF**.

---

## Project Structure

```
LoM-Summarizer/
├─ backend/
│  ├─ main.py
│  ├─ ai_integration.py
├─ frontend/
│  ├─ app/
│  │  ├─ page.tsx
│  │  ├─ components/
│  │  │  └─ PreviewCard.tsx
│  ├─ package.json
│  ├─ tsconfig.json

```
## Features Implemented

* Multi-file upload (`.pdf` & `.docx`)
* Text extraction from uploaded files
* AI summarization using a lightweight transformer model
* Keyword extraction (top 10 unique words)
* Simple inferred strengths analysis
* Preview of extracted text, summary, keywords, and strengths in frontend
* Download results as a PDF with summary, keywords, and strengths
* Responsive frontend with TailwindCSS and Framer Motion
* Backend API powered by FastAPI with CORS enabled
