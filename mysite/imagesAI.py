import requests

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/core",
    headers={
        "authorization": f"Bearer sk-DenBBoQ8dZPyFKDHt1k3N5JWSaZ67X9Sh5Nzp7fWqgRQlDA2",
        "accept": "image/*",
    },
    files={"none": ""},
    data={
        "prompt": "Patrick from Sponge Bob is sitting on chair and programming Python code while listening to heavy metal",
        "output_format": "webp",
    },
)

if response.status_code == 200:
    with open("./lighthouse.webp", "wb") as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))
