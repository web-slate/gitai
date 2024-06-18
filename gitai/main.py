import click
from gitai.predict import predict_answer

@click.command()
@click.argument('question')
def main(question):
    answer, index = predict_answer(question)
    click.echo(f'Question: {question}')
    click.echo(f'Predicted Index: {index}')
    click.echo(f'Answer: {answer}')

if __name__ == '__main__':
    main()
