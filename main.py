from risk_rules import analyze_risk

user_input = input("Enter your AI prompt/use case: ")

result = analyze_risk(user_input)

print("\n--- Risk Analysis ---")
print(f"Risk Level: {result['level']}")
print(f"Risk Types: {', '.join(result['types'])}")
print(f"Risk Score: {result['score']}")
print(f"Base Score: {result['base_score']}")
print(f"Context Multiplier: {result['context_multiplier']}")
print(f"Intent Multiplier: {result['intent_multiplier']}")
print(f"Final Risk Score: {result['score']}")
