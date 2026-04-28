import os
import resend


def enviar_correo_alerta(asunto, mensaje, destino):
    resend.api_key = os.getenv("RESEND_API_KEY")

    if not resend.api_key:
        raise ValueError("Falta RESEND_API_KEY")

    response = resend.Emails.send({
        "from": "Alertas <onboarding@resend.dev>",
        "to": [destino],
        "subject": asunto,
        "html": f"""
            <h3>Mensaje desde WordPress</h3>
            <p>{mensaje}</p>
        """
    })

    return response