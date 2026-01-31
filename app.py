import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="QR Code Generator", page_icon="🚀")

st.title("🖼️ Générateur de QR Code")
st.write("Entrez un texte ou un lien ci-dessous pour générer son QR code instantanément.")

# Entrée utilisateur
url = st.text_input("Texte ou URL :", placeholder="https://www.exemple.com")

if url:
    # Génération du QR Code
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Conversion pour Streamlit et téléchargement
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    # Affichage
    st.image(byte_im, caption="Clic droit pour enregistrer l'image", use_column_width=True)
    
    # Bouton de téléchargement
    st.download_button(
        label="📥 Télécharger le QR Code",
        data=byte_im,
        file_name="mon_qrcode.png",
        mime="image/png"
    )
