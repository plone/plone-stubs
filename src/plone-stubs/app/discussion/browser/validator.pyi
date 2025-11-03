from z3c.form import validator

class CaptchaValidator(validator.SimpleFieldValidator):
    def validate(self, value): ...
