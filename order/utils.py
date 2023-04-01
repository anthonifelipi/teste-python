import requests
from .models import Order


def calculate_freight(order: Order):
    url_melhor_envio = "https://sandbox.melhorenvio.com.br/api/v2/me/shipment/calculate"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImEzZWFiNTQ5MmU0M2Q1ZjIwZDY1NTk2MGNhNmU5NWQyMWQ5YjFiOGYwMDI2ZWJkMzA5OGI0NWViM2RmNGUwNzk4ZTU5NzMwMWMyMzJlMDdiIn0.eyJhdWQiOiI5NTYiLCJqdGkiOiJhM2VhYjU0OTJlNDNkNWYyMGQ2NTU5NjBjYTZlOTVkMjFkOWIxYjhmMDAyNmViZDMwOThiNDVlYjNkZjRlMDc5OGU1OTczMDFjMjMyZTA3YiIsImlhdCI6MTY4MDEwMjAwMCwibmJmIjoxNjgwMTAyMDAwLCJleHAiOjE3MTE3MjQ0MDAsInN1YiI6IjMxODg1OTMwLTYzZWUtNDAxOS04NWFiLTM4ZDRiODdkOTk2NyIsInNjb3BlcyI6WyJjYXJ0LXJlYWQiLCJjYXJ0LXdyaXRlIiwiY29tcGFuaWVzLXJlYWQiLCJjb21wYW5pZXMtd3JpdGUiLCJjb3Vwb25zLXJlYWQiLCJjb3Vwb25zLXdyaXRlIiwibm90aWZpY2F0aW9ucy1yZWFkIiwib3JkZXJzLXJlYWQiLCJwcm9kdWN0cy1yZWFkIiwicHJvZHVjdHMtZGVzdHJveSIsInByb2R1Y3RzLXdyaXRlIiwicHVyY2hhc2VzLXJlYWQiLCJzaGlwcGluZy1jYWxjdWxhdGUiLCJzaGlwcGluZy1jYW5jZWwiLCJzaGlwcGluZy1jaGVja291dCIsInNoaXBwaW5nLWNvbXBhbmllcyIsInNoaXBwaW5nLWdlbmVyYXRlIiwic2hpcHBpbmctcHJldmlldyIsInNoaXBwaW5nLXByaW50Iiwic2hpcHBpbmctc2hhcmUiLCJzaGlwcGluZy10cmFja2luZyIsImVjb21tZXJjZS1zaGlwcGluZyIsInRyYW5zYWN0aW9ucy1yZWFkIiwidXNlcnMtcmVhZCIsInVzZXJzLXdyaXRlIiwid2ViaG9va3MtcmVhZCIsIndlYmhvb2tzLXdyaXRlIl19.PTb06vQtUANuSa246Atljh7_OUbs7y0nmd1ARStq7PCgKSQCQ6MSaZSsRoSJ6P60EXOqSMndmiRVXfjz8c8sXW0L-cLjmuRM8mvG1DZ9VtfgLUmNd7pc-5kVpJh91ICVoQE7AQjXJkQkS3NdyJYr4HoMLlfNmuwJZGQUOpM2SS-SotXHP2zDMU43J61gjd3D-0Mcv_rVKpq46FAK5ZPfZlEE5e8ednepRY7EtVrM9XmVnVl771yUnKtE7DVvtCCpFIc2YfkCTNHLyGasG9wPCfoyXPZd5zBqsEIKJz2sbyoXrAIRdSUScoH-eD4ulLFH_z93-ej2Py8X6LogPfaIqE7RzEFyl4ZLNvdABjn7dQ1edcWbA8xQu8lMIFSdkwSBbcJ_JsNVFWlnh25DTcLItzaKF9mRSZuBmKQCz5xVuomGFQmX3ucw2uyTyoC3PItRhDQbDDhaY11IECyMbvy--nr3HhTzf2n3JpUsCFMk8vZwifvS0G6Xip_AtHqBDYiIrJXJOo4phybBLzuKw3E4SCm78AJsJAAWOkw4Y_nACF0K4l3hdrchpLPOsGA3Twi3oVIo6CM41SCC0orvfShGeRUOX1jCYxa63rkiQC1qlg-FnI3_aHrML01XI4wTHf-QS_MEXWNl8rQtmEYUkZBqcS5LTV0-wb3FHi691FwlD9A",
    }

    data = {
        "from": {
            "postal_code": str(order.zip_from),
        },
        "to": {
            "postal_code": str(order.zip_to),
        },
        "package": {
            "height": str(order.height),
            "width": str(order.height),
            "length": str(order.height),
            "weight": str(order.height),
        },
        "options": {
            "insurance_value": 100.00,
            "receipt": False,
            "own_hand": True,
        },
        "services": str(order.courier_choice),
    }
    response = requests.post(
        url_melhor_envio,
        json=data,
        headers=headers,
    )

    if response.status_code == 200:
        freight_data = response.json()

        for item in freight_data["packages"]:
            insurance_value = item["insurance_value"]

        freight = {
            "order": order,
            "carrier": freight_data["name"],
            "delivery_time": freight_data["delivery_time"],
            "delivery_cost": freight_data["custom_price"],
            "external_freight_id": freight_data["id"],
            "ensurance_price": insurance_value,
        }
        return freight
    else:
        return print("deu errado")
