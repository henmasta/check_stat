import io
import requests

url = requests.get("http://priemn2022.donntu.ru/?local&ipp=1101")
url.encoding = 'utf-8'
with open("input.txt", "w", encoding = 'utf-8') as file_path:
    file_path.write(url.text)
with open("log.txt", "w", encoding='utf-8') as log:
    with io.open("input.txt", encoding='utf-8') as file:
        for line in file:
            if "<!-- <td>" in line or "38" in line or "53" in line or '<td class="text-center">' in line:
                out = line.replace('<!-- <td>', '').replace('</td> -->', '').replace('<td>', '').replace('</td>', '').replace('<td class="text-center">', '').>
                log.write(out)
