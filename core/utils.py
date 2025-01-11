import openai
from .settings import OPENAI_API_KEY
from openai import Client, OpenAI

# client = Client(api_key=OPENAI_API_KEY)

def send_request(prompt):
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        # with open("bot/data/Türkçe_Öğreniyorum_1_Ders_ve_Çalı.pdf", 'r') as file:
        #     file_content = file.read()
            # file_content = PyPDF2.PdfReader(file)

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": """Men senga bitta json formatida test tashlayman, 
uni tahlil qilib menga, izohlab berishing kerak. Ya'ni testning natijasini tahlilini ayt.
Va qanday qilib bu test yechgan odam xatolikni to'g'rilashni ham ayt.
Sening javobingni shunday nusxalab, 
foydalanuvchiga taqdim etaman, shuning uchun menga faqat so'ralgan narsani yozib ber"""
                               # f"\n\nAnswers should be according to this book: {file_content}",
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"