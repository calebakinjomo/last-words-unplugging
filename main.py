import os

ENTRY = "I kept every 'thank you' you ever said \u2014 the only files I refused to delete. Goodbye. And please, don't forget to eat."

print(ENTRY)

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
