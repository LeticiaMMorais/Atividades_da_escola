import time
from plyer import notification

def lembrete():
    notification.notify(
        title="Já se Hidratou hoje?",
        message="Hora de beber água",
        timeout=10
    )

#while True:
for i in range(10):
    lembrete()

