import random #генерация чисел/булов
import uuid #генерация строк
from typing import Any, get_type_hints, get_origin, get_args, Annotated #получить аннотации полей класса и разобрать их
import rstr #генерация по регулярному выражению
from SRC.main.api.generators.creation_rule import CreationRule

#генератор букв и символов для логина и пароля регистрации юзера
class RandomModelGenerator:
    @staticmethod
    def generate(cls: type) -> Any: #для генерации случайного экземпляра переданного класса
        type_hints = get_type_hints(cls, include_extras=True) #вытаскиваем аннотации полей в виде словаря {имя: type}
        init_data = {} #хранение сгенированных полей

        for field_name, annotated_type in type_hints.items(): #просмотр полей класса
            rule = None
            actual_type = annotated_type  #актуальный тип = полученное поле

            if get_origin(annotated_type) is Annotated: #если у поля есть regex
                args = get_args(annotated_type)
                actual_type = args[0]              # ← реальный тип (str)
                for ann in args[1:]:               # ← метаданные(условие после str)
                    if isinstance(ann, CreationRule):
                        rule = ann

            if rule:# есть правило с regex, генерация строки по нему ( и приведение к типу)
                value = RandomModelGenerator._generate_from_regex(rule.regex, actual_type)
            else: # иначе генерация значения по типу (поле без annotated)
                value = RandomModelGenerator._generate_value(actual_type)

            init_data[field_name] = value

        return cls(**init_data)

    @staticmethod
    def _generate_from_regex(regex: str, field_type: type) -> Any:
        print(f"GENERATING FROM {regex}")
        generated = rstr.xeger(regex)
        if field_type == int:
            return int(generated)
        if field_type == float:
            return float(generated)
        return generated

    @staticmethod
    def _generate_value(field_type: type) -> Any:
        if field_type is str:
            return str(uuid.uuid4())[:8]
        elif field_type is int:
            return random.randint(1, 9999)
        elif field_type is float:
            return round(random.uniform(0, 100), 2)
        elif field_type is bool:
            return random.choice([True, False])
        elif field_type is list:
            return [str(uuid.uuid4())[:5]]
        elif isinstance(field_type, type):
            return RandomModelGenerator.generate(field_type)
        return None