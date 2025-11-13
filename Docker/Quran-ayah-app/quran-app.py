# app.py
from flask import Flask

import redis
import random


app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, db=0)

ayahs = [
    {
        "arabic": "اللّهُ لا إله إلا هو الحي القيوم لا تأخذه سنة ولا نوم له ما في السماوات وما في الأرض من ذا الذي يشفع عنده إلا بإذنه يعلم ما بين أيديهم وما خلفهم ولا يحيطون بشيء من علمه إلا بما شاء وسع كرسيه السماوات والأرض ولا يؤوده حفظهما وهو العلي العظيم",
        "english": "Allah – there is no deity except Him, the Ever-Living, the Sustainer of existence. Neither drowsiness overtakes Him nor sleep. To Him belongs whatever is in the heavens and whatever is on the earth. Who is it that can intercede with Him except by His permission? He knows what is before them and what will be after them, and they encompass not a thing of His knowledge except for what He wills. His Kursi extends over the heavens and the earth, and their preservation tires Him not. And He is the Most High, the Most Great. (2:255)"
    },
    {
        "arabic": "وَعَسَى أَنْ تَكْرَهُوا شَيْئًا وَهُوَ خَيْرٌ لَكُمْ وَعَسَى أَنْ تُحِبُّوا شَيْئًا وَهُوَ شَرٌّ لَكُمْ وَاللّهُ يَعْلَم وَأَنْتُمْ لا تَعْلَمُون",
        "english": "But perhaps you hate a thing and it is good for you; and perhaps you love a thing and it is bad for you. And Allah knows, while you know not. (2:216)"
    },
    {
        "arabic": "إِنَّ مَعَ الْعُسْرِ يُسْرًا",
        "english": "Indeed, with hardship comes ease. (94:6)"
    },
    {
        "arabic": "فَاذْكُرُونِي أَذْكُرْكُمْ وَاشْكُرُوا لِي وَلا تَكْفُرُون",
        "english": "So remember Me; I will remember you. And be grateful to Me and do not deny Me. (2:152)"
    },
    {
        "arabic": "وَمَنْ يَتَّقِ اللَّهَ يَجْعَل لَهُ مَخْرَجًا وَيَرْزُقْهُ مِنْ حَيْثُ لا يَحْتَسِبُ",
        "english": "And whoever fears Allah – He will make for him a way out and provide for him from where he does not expect. (65:2-3)"
    },
    {
        "arabic": "إِنَّ رَبِّي عَلَيَّ هَادٍ",
        "english": "Indeed, my Lord is guiding me. (26:122)"
    },
    {
        "arabic": "قُلْ هُوَ اللَّهُ أَحَدٌ اللَّهُ الصَّمَدُ لَمْ يَلِدْ وَلَمْ يُولَدْ وَلَمْ يَكُن لَّهُ كُفُوًا أَحَدٌ",
        "english": "Say, He is Allah, [Who is] One, Allah, the Eternal Refuge. He neither begets nor is born, nor is there to Him any equivalent. (112:1-4)"
    },
    {
        "arabic": "وَلَقَدْ خَلَقْنَا الإِنسَانَ وَنَعْلَمُ مَا تُوَسْوِسُ بِهِ نَفْسُهُ وَنَحْنُ أَقْرَبُ إِلَيْهِ مِنْ حَبْلِ الْوَرِيدِ",
        "english": "And We have certainly created man and We know what his soul whispers to him, and We are closer to him than [his] jugular vein. (50:16)"
    },
    {
        "arabic": "وَقُلِ اعْمَلُوا فَسَيَرَى اللَّهُ عَمَلَكُمْ وَرَسُولُهُ وَالْمُؤْمِنُونَ",
        "english": "And say, 'Do [good] deeds; Allah will see your deeds, and [so will] His Messenger and the believers.' (9:105)"
    },
    {
        "arabic": "رَبَّنَا لَا تُزِغْ قُلُوبَنَا بَعْدَ إِذْ هَدَيْتَنَا وَهَبْ لَنَا مِنْ لَدُنْكَ رَحْمَةً إِنَّكَ أَنْتَ الْوَهَّابُ",
        "english": "Our Lord, let not our hearts deviate after You have guided us and grant us from Yourself mercy. Indeed, You are the Bestower. (3:8)"
    }
]


@app.route('/')
def home():
    return """
    <html>
    <head>
    <title>Quran App</title>
    <style>
        body {
            background-image: url('https://t4.ftcdn.net/jpg/00/24/89/01/360_F_24890183_P9xD5nmU2oFm3yy1aJK3Bk5wxcZJzJQF.jpg');
            background-size: cover;
            background-position: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
            color: white;
            font-size: 2em;
            text-shadow: 2px 2px 5px black;
        }
        a { color: #FFD700; text-decoration: none; font-size: 1.2em; }
        a:hover { text-decoration: underline; }
    </style>
    </head>
    <body>
        <h1>Welcome to the Quran App</h1>
        <p>May the words of Allah bring peace to your heart.</p>
        <p>To view your daily ayah, <a href="/ayah">click here!</a></p>
    </body>
    </html>
    """

@app.route('/ayah')
def ayah_page():
    count = r.incr('ayah')
    ayah = random.choice(ayahs)
    return f"""
    <html>
    <head>
        <title>Today's Ayah</title>
    </head>
    <body style="
        background-image: url('https://www.shutterstock.com/shutterstock/videos/1076042090/thumb/1.jpg?ip=x480');
        background-size: cover;
        background-position: center;
        text-align:center;
        font-size:1.5em;
        padding:50px;
        color: white;
        text-shadow: 1px 1px 2px black;
    ">
        <h1>Today's Ayah</h1>
        <p>{ayah['arabic']}</p>
        <p>{ayah['english']}</p>
        <p>You have read {count} ayahs by visiting this page!</p>
        <a href="/" style="color: #FFD700; text-decoration:none;">Back to Home</a>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)