import network
import urequests as requests
import time
import keys

influx_token = keys.influx_token
influx_url = keys.influx_url



def send_to_influx(measurement, fields, tags=""):
    """
    measurement: string, e.g., "sensor_data"
    fields: dict, e.g., {"temperature":25, "humidity":44}
    tags: string, e.g., "plant=Schefflera plant"
    """
    # This is where i build the line protocol: measurement[,tags] field1=value1,field2=value2
    field_str = ",".join([f"{k}={v}" for k, v in fields.items()])
    line = f"{measurement}"
    if tags:
        line += f",{tags}"
    line += f" {field_str}"
    
    
    headers = {
        "Authorization": f"Token {influx_token}",
        "Content-Type": "text/plain"
    }
    try:
        response = requests.post(influx_url, data=line, headers=headers)
        if response.status_code == 204:
            print("Data sent successfully!")
        else:
            print(f"Failed to send data, status: {response.status_code}, body: {response.text}")
        response.close()
    except Exception as e:
        print("Error sending data:", e)
