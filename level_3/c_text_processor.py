"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""


class TextProcessor:
    def __init__(self, text: str) -> None:
        self.text = text

    def to_upper(self) -> str:
        return self.text.upper()

    def summarize(self) -> str:
        return f'Total text length: {len(self.text)}'


class AdvancedTextProcessor(TextProcessor):
    def summarize(self) -> str:
        return super().summarize() + f', total number of words in the text: {len(self.text.split())}'


if __name__ == '__main__':
    text_processor = TextProcessor(text='Some text')
    assert text_processor.text == 'Some text'
    assert text_processor.to_upper() == 'SOME TEXT'
    assert text_processor.summarize() == 'Total text length: 9'

    advanced_text_processor = AdvancedTextProcessor('One more some text')
    assert advanced_text_processor.text == 'One more some text'
    assert advanced_text_processor.to_upper() == 'ONE MORE SOME TEXT'
    assert advanced_text_processor.summarize() == 'Total text length: 18, total number of words in the text: 4'
