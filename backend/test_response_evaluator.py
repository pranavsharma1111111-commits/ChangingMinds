from engine.response_evaluator import ResponseEvaluator

evaluator = ResponseEvaluator()

response1 = "Okay... I'll do my homework."
response2 = "No, leave me alone."

print(evaluator.evaluate(response1))
print(evaluator.evaluate(response2))