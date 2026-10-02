from adapters import AdapterRegistry
def test_adapters():
 r=AdapterRegistry(); assert set(r.names())=={"claude-code","crewai","lyzr","openai-sdk"}
