import jinja2

TEMPLATES_DIR = 'templates'
JINJA_ENVIRONMENT = env = jinja2.environment.Environment(
            loader=jinja2.loaders.FileSystemLoader(
                searchpath=TEMPLATES_DIR
            ),
            autoescape=True,
            trim_blocks=True,
            lstrip_blocks=True,
            undefined=jinja2.runtime.StrictUndefined
        )

def main():
    pass

if __name__ == '__main__':
    main()