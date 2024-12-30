import requests
import re


def main():
    with open('maps.md', 'r') as f1:
        with open('maps2.md', 'w', encoding='utf-8') as f2:
            lines = [line.strip() for line in f1.readlines() if line != '\n']

            for i, line in enumerate(lines):
                lineS = line.split('.')
                if len(lineS) > 1:
                    print(f"{i}", sep='', end='\r', flush=True)
                    name = lineS[1].lstrip().replace(' ', '_')
                    response = requests.get(f"https://poe2db.tw/ru/{name}")

                    if response.status_code == 200:
                        translated = re.search(r'<h4>([^<>]*)<\/h4>', response.text).group(1)
                        lines[i] += f' ({translated})'
                    else:
                        print(f'\nResponse error ({response.status_code})')
                    i += 1
                else:
                    i -= 1

            f2.write('\n'.join(lines))


if __name__ == '__main__':
    main()
