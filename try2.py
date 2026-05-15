import time
import sys

def print_lyrics():
    lyr = [
        "Jana tu ata nahi, sapnoo sa jata nahi",
        "Mil jaya kia hi bat thi, kamal ho jata wohee\n",
        "Jana maira swalo ka manzar tu",
        "Haan ma sokha sa sara samundar tu",
        "Haan gulabi c surkhi jo dikhtee thi",
        "Phir sa dikh jai tu jee bhar ka sah bhar loo",
        "Katein kitnee thi ratai nai soya mai",
        "Tujh ko kitna bulaya fr roya mein",
        "Tairi sari wo batein ku sona nai daiti",
        "Ku staya mujha ha fr khoya ma\n",
        "Janaa!Tu ata nahi, Sapnoo sa jata nahi",
        "Mil jay kia hi bat thi, Kamal ho jata wohee",
        "Jo bh wo raz ha taira",
        "Mujh ko btata nahi",
        "Mil jay kia hi baaat thi, Kamal ho jata wohee\n",

        "Smbhaal ka rkha wo phool mera tu",
        "Meri shayari mein zroor rha tu",
        "Jo ankho mein piyari si dunya bassayi",
        "Wo duniya bh tha tu, wo lmha bh tha tu",
        "Haan lagtay hein mujh ko ye kisa stanei",
        "Deta na dil mera tujh ko bhulanaa",
        "Adhoray sa waday, adhore si yadei",
        "Rehna tha ban ka hamdam taira",
        "Aisa jana hi tha fr tu ku tehra",
        "Ab na manai maira dil",
        "ka na taira kabal thi ik arzo",

        "Mai kehta rha pr to aataa nahi",
        "Sapnoo sa jata nahi"
    ]
    delay = [0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.4,0.5,0.5,0.7,0.7,1.0,1.0,1.0,0.1,0.1,0.1,0.1]
    print ("Finding Her\n\n")

    for i, line in enumerate(lyr):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        time.sleep(delay[i])
print_lyrics()