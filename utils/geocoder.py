import requests


def geocoder(latitude, longitude):
    token = 'pk.4423f82f7369c3e42f3b6246a541b288'
    headers = {"Accept-Language": "ru"}
    address = requests.get(
        f'https://eu1.locationiq.com/v1/reverse.php?key={token}&lat={latitude}&lon={longitude}&format=json',
        headers=headers).json()
    display_name = address.get("display_name", "")
    parts = display_name.split(", ")
    if len(parts) >= 2:
        return f"{parts[1]}, {parts[0]}"
    elif len(parts) == 1:
        return parts[0]
    else:
        return ''
