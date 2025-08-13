import network
import urequests as requests
import time
import keys

influx_token = keys.influx_token
influx_url = keys.influx_url    

influx_token = "uxJhhOdZDRqtAs7E7JWmjzjiz4kCttpgh0rUMH28mpqsnFRJtl7XXZ4QcQuTljIo6YB7fiVq_iw0g5KuSI8tKQ=="
influx_url = "https://eu-central-1-1.aws.cloud2.influxdata.com/api/v2/write?org=IoT&bucket=data&precision=s"

 
def send_to_influx(measurement, fields, tags="", retries=3, delay=5):
    """
    Send sensor data to InfluxDB with retries on failure.
    measurement: string, e.g., "sensor_data"
    fields: dict, e.g., {"temperature":25, "humidity":44}
    tags: string, e.g., "plant=Schefflera plant"
    retries: number of attempts if sending fails (default 3)
    delay: seconds to wait between retries (default 5)
    """
    field_str = ",".join([f"{k}={v}" for k, v in fields.items()])
    line = f"{measurement}"
    if tags:
        line += f",{tags}"
    line += f" {field_str}"
    
    headers = {
        "Authorization": f"Token {influx_token}",
        "Content-Type": "text/plain"
    }
    
    attempt = 0
    while attempt < retries:
        try:
            response = requests.post(influx_url, data=line, headers=headers)
            if response.status_code == 204:
                print("Data sent successfully!")
                response.close()
                return True
            else:
                print(f"Failed to send data, status: {response.status_code}, body: {response.text}")
                response.close()
        except Exception as e:
            print(f"Error sending data on attempt {attempt + 1}: {e}")
        
        attempt += 1
        print(f"Retrying in {delay} seconds...")
        time.sleep(delay)
    
    print("Failed to send data after multiple attempts.")
    return False
