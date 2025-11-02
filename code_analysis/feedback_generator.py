def progress_bar(value, total=10, length=20):
    """
    Creează o bară vizuală de progres (ex: [██████----] 6/10)
    """
    filled = int((value / total) * length)
    empty = length - filled
    return f"[{'█' * filled}{'-' * empty}] {value}/10"

def generate_feedback(scores, total):
    """
    Creează mesajul bilingv (RO + EN) și afișarea grafică.
    """
    # Header
    mesaj = "🎉 Felicitări! Ai trecut toate testele!\n"
    mesaj += f"Codul tău a fost analizat și a obținut un scor total de {total}/100.\n\n"

    if total > 90:
        mesaj += "🌟 Super! Codul tău este foarte bine structurat și eficient!\n"
    elif total > 70:
        mesaj += "👍 Foarte bine! Doar câteva îmbunătățiri mici la claritate sau eficiență.\n"
    else:
        mesaj += "💡 Poți îmbunătăți logica și structura codului pentru un rezultat și mai bun!\n"

    mesaj += "\n📘 Rezumat pe criterii:\n"
    for k, v in scores.items():
        label = k.replace('_', ' ').title().ljust(22)
        bar = progress_bar(v)
        mesaj += f" {label} {bar}\n"

    mesaj += "\n✨ Ține-o tot așa! Cu puțin exercițiu, codul tău va fi perfect!\n"

    # --- traducere în engleză ---
    mesaj += "\n\n🌍 English version:\n"
    mesaj += "🎉 Congratulations! You passed all the tests!\n"
    mesaj += f"Your code has been analyzed and received a total score of {total}/100.\n\n"

    if total > 90:
        mesaj += "🌟 Great job! Your code is very well structured and efficient!\n"
    elif total > 70:
        mesaj += "👍 Very good! Just a few small improvements for clarity or efficiency.\n"
    else:
        mesaj += "💡 You can improve the logic and structure for an even better result!\n"

    mesaj += "\n📘 Category summary:\n"
    for k, v in scores.items():
        label = k.replace('_', ' ').title().ljust(22)
        bar = progress_bar(v)
        mesaj += f" {label} {bar}\n"

    mesaj += "\n✨ Keep going! With a bit of practice, your code will be awesome!"

    return mesaj
