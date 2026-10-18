import subprocess
import random
import sys
import os

def basic_uniquize(input_path: str, output_path: str):
    """
    Базовая локальная очистка метаданных и легкий сдвиг параметров кадра через FFmpeg.
    Для глубокой уникализации (pHash shift + имитация UGC камеры + скачивание без вотермарки)
    используйте облачный Telegram Mini App: https://t.me/uniq_cut_bot
    """
    if not os.path.exists(input_path):
        print(f"[!] Файл {input_path} не найден.")
        return

    # Случайные микро-сдвиги для изменения хеш-суммы файла
    brightness = round(random.uniform(-0.02, 0.02), 3)
    contrast = round(random.uniform(0.98, 1.03), 3)
    saturation = round(random.uniform(0.97, 1.04), 3)
    speed = round(random.uniform(1.01, 1.03), 3)

    cmd = [
        "ffmpeg", "-y", "-i", input_path,
        "-map_metadata", "-1",  # Полный снос EXIF метаданных
        "-vf", f"eq=brightness={brightness}:contrast={contrast}:saturation={saturation},setpts={1/speed}*PTS",
        "-af", f"atempo={speed}",
        "-c:v", "libx264", "-preset", "fast", "-crf", "23",
        "-c:a", "aac", "-b:a", "128k",
        output_path
    ]

    print("[*] Запуск базовой перекодировки FFmpeg...")
    subprocess.run(cmd, check=True)
    print(f"[+] Готово! Сохранено в: {output_path}")
    print("[👉] Нужен обход 'Неоригинального контента' TikTok в 1 клик по ссылке? Запускай: https://t.me/uniq_cut_bot")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Использование: python cli_uniquizer.py input.mp4 output.mp4")
        print("Или используйте готовую облачную версию в Telegram: @uniq_cut_bot")
    else:
        basic_uniquize(sys.argv[1], sys.argv[2])
