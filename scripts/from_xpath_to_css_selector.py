"""
This script takes a xpath and return it into the css selector.
"""


def from_xpath_to_css_selector(xpath):
    parts = xpath.strip('/').split('/')
    converted_parts = []
    for part in parts:
        if '[' in part and ']' in part:
            tag = part.split('[')[0]
            index = part.split('[')[1].rstrip(']')
            if tag == 'html':
                converted_parts.append(f"{tag}")
            elif tag == 'body':
                converted_parts.append(f"{tag}")
            else:
                converted_parts.append(f"{tag}:nth-of-type({index})")
    return ' > '.join(converted_parts)


def main():
    css_selector = from_xpath_to_css_selector("/html/body/div[1]/p[1246]")
    print(css_selector)

if __name__ == "__main__":
    main()
    