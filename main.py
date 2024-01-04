import customtkinter as ctk
import requests

ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("blue")  

languages = {
    "Русский": "ru",
    "Турецкий": "tr",
    "Арабский": "ar",
    "Английский": "en",
    "Испанский": "es",
    "Француский": "fr",
    "Германский": "de",
    "Италский": "it",
    "Португальский": "pt",
    "Китайский": "zh-CN",
    "Японский": "ja",
    "Китайский": "ko",
    "Индийский": "hi",
    "Индизианский": "id",
    "Перский": "fa",
    "Дутский": "nl",
    "Сведский": "sv",
}

def translate_text():
    """Translates the input text to the selected language using Google Translate."""
    input_text = text_input.get("1.0", "end-1c")
    source_language = language_select.get()
    target_language = translate_to_select.get()
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={languages[source_language]}&tl={languages[target_language]}&dt=t&q={input_text}"
    response = requests.get(url)
    translation = response.json()[0][0][0]
    text_output.delete("1.0", "end")
    text_output.insert("1.0", translation)

root = ctk.CTk()
root.title("Multilingual Translator")
root.geometry("500x450")
root.configure(bg="#2a2d2e")

frame_padx = 20
frame_pady = 10
widget_width = 400
widget_height = 120
corner_radius = 15

frame = ctk.CTkFrame(root, corner_radius=corner_radius)
frame.pack(pady=frame_pady, padx=frame_padx, fill="both", expand=True)

text_input = ctk.CTkTextbox(frame, width=widget_width, height=widget_height, corner_radius=corner_radius)
text_input.grid(row=0, column=0, columnspan=2, padx=frame_padx, pady=frame_pady)

text_output = ctk.CTkTextbox(frame, width=widget_width, height=widget_height, corner_radius=corner_radius)
text_output.grid(row=1, column=0, columnspan=2, padx=frame_padx, pady=frame_pady)

language_select = ctk.CTkComboBox(frame, values=list(languages.keys()), width=180, height=30, corner_radius=10)
language_select.set("Русский")
language_select.grid(row=2, column=0, padx=frame_padx, pady=frame_pady)

translate_to_select = ctk.CTkComboBox(frame, values=list(languages.keys()), width=180, height=30, corner_radius=10)
translate_to_select.set("Английский")
translate_to_select.grid(row=2, column=1, padx=frame_padx, pady=frame_pady)

translate_button = ctk.CTkButton(root, text="Translate", command=translate_text, width=120, height=40, corner_radius=20)
translate_button.pack(pady=20)

root.mainloop()
