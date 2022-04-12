from email.policy import default
import click
from schema import SchemaFile

@click.group()
def cli():
    pass

@cli.command()
@click.option("--filename", default="test.json")
def write(filename):
    """
    Adds a json-cli write option for the user to be able to write the json file.
    """

    schema = SchemaFile(output_file=filename)
    output_schema = {}
    for key in schema.value.keys():
        value = click.prompt(f"What is the value for {key}")
        output_schema[key] = value

    schema.set_values(output_schema)


if __name__ == '__main__':
    cli()