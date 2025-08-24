# main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from io import BytesIO
from typing import List
import fitz  # PyMuPDF
from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# === AI Integration ===
from ai_integration import ai_summarize, ai_extract_keywords, ai_strengths_analysis

# === Initialize FastAPI ===
app = FastAPI()

# === CORS for frontend ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Helper Functions ===
def process_lom(text: str):
    summary = ai_summarize(text)
    strengths = ai_strengths_analysis(text)
    keywords = ai_extract_keywords(text)
    return summary, keywords, strengths

# === Upload Endpoint ===
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    text = ""

    if file.filename.endswith(".pdf"):
        doc = fitz.open(stream=content, filetype="pdf")
        text = "\n".join([page.get_text() for page in doc])
    elif file.filename.endswith(".docx"):
        doc = Document(file.file)
        text = "\n".join([p.text for p in doc.paragraphs])
    else:
        return {"error": "Unsupported file type"}

    summary, keywords, strengths = process_lom(text)

    return {
        "filename": file.filename,
        "text_preview": text[:1000],
        "full_text": text,
        "summary": summary,
        "keywords": keywords,
        "strengths": strengths
    }

# === Download PDF Endpoint ===
@app.post("/download_pdf/")
async def download_pdf(payload: dict):
    text = payload.get("text", "")
    keywords = payload.get("keywords", [])
    strengths = payload.get("strengths", [])
    
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    c.setFont("Helvetica", 12)
    y = height - 50

    for line in text.splitlines():
        while line:
            slice = line[:90]
            c.drawString(50, y, slice)
            line = line[90:]
            y -= 15
            if y < 50:
                c.showPage()
                c.setFont("Helvetica", 12)
                y = height - 50

    # Keywords
    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Keywords:")
    y -= 15
    c.setFont("Helvetica", 12)
    c.drawString(50, y, ", ".join(keywords))

    # Strengths
    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Strengths:")
    y -= 15
    c.setFont("Helvetica", 12)
    c.drawString(50, y, ", ".join(strengths))

    c.save()
    buffer.seek(0)
    
    return StreamingResponse(
        buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=output.pdf"}
    )

# === Root Endpoint ===
@app.get("/")
async def root():
    return {"message": "FastAPI backend is running. Use /upload/ to POST files."}
