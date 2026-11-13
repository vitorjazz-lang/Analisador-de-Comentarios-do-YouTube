import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from yt_dlp import YoutubeDL
from transformers import pipeline
import pandas as pd

# Limite de caracteres por comentário (ajustável)
MAX_CHARS = 3000

def executar():
    video_url = entry.get()

    if not video_url:
        messagebox.showerror("Erro", "Cole o link do vídeo!")
        return

    caminho_arquivo = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Arquivo Excel", "*.xlsx")],
        title="Salvar arquivo como"
    )

    if not caminho_arquivo:
        return

    try:
        # 🔄 modo indeterminado (carregando)
        progress.start()
        status_label.config(text="🔄 Coletando comentários...")
        janela.update_idletasks()

        opts = {
            "getcomments": True,
            "skip_download": True,
            "quiet": True,
            "extractor_args": {
                "youtube": {
                    "max_comments": ["all"],
                }
            },
        }

        with YoutubeDL(opts) as yt:
            info = yt.extract_info(video_url, download=False)

        comments = info.get("comments") or []

        rows = []
        for c in comments:
            rows.append({
                "author": c.get("author"),
                "text": c.get("text"),
            })

        df = pd.DataFrame(rows)

        # 🔹 parar animação e mudar para modo determinado
        progress.stop()
        progress["mode"] = "determinate"
        progress["maximum"] = len(df)
        progress["value"] = 0

        status_label.config(text="🤖 Analisando sentimentos...")
        janela.update_idletasks()

        # 🔹 Pipeline com truncation=True para evitar erro de tensor
        classifier = pipeline(
            "sentiment-analysis",
            model="nlptown/bert-base-multilingual-uncased-sentiment",
            tokenizer_kwargs={"truncation": True}
        )

        def traduzir(label):
            if "1" in label or "2" in label:
                return "negativo"
            elif "3" in label:
                return "neutro"
            else:
                return "positivo"

        sentimentos = []

        # 🔹 progresso real
        for i, texto in enumerate(df["text"]):
            try:
                # cortar texto longo
                texto_cortado = str(texto)[:MAX_CHARS]
                resultado = classifier(texto_cortado)[0]["label"]
                sentimentos.append(traduzir(resultado))
            except:
                sentimentos.append("erro")

            progress["value"] = i + 1
            janela.update_idletasks()

        df["sentimento"] = sentimentos

        df.to_excel(caminho_arquivo, index=False)

        status_label.config(text="✅ Concluído!")
        messagebox.showinfo("Sucesso", f"Arquivo salvo em:\n{caminho_arquivo}")

    except Exception as e:
        messagebox.showerror("Erro", str(e))


# 🔹 Interface
janela = tk.Tk()
janela.title("Analisador de Comentários do YouTube")
janela.geometry("420x260")

tk.Label(janela, text="Cole o link do vídeo:").pack(pady=10)

entry = tk.Entry(janela, width=50)
entry.pack()

tk.Button(janela, text="Executar", command=executar).pack(pady=10)

# 🔹 Barra de progresso
progress = ttk.Progressbar(janela, orient="horizontal", length=300, mode="indeterminate")
progress.pack(pady=10)

status_label = tk.Label(janela, text="")
status_label.pack()

janela.mainloop()

