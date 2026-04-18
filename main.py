from risk_rules import analyze_risk

user_input = input("Enter your AI prompt/use case: ")

result = analyze_risk(user_input)

print("\n--- Risk Analysis ---")
print(f"Risk Level: {result['level']}")
print(f"Risk Types: {', '.join(result['types'])}")
print(f"Risk Score: {result['score']}")
