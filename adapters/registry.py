from .portable_adapter import OpenAIAdapter,CrewAIAdapter,ClaudeCodeAdapter,LyzrAdapter
class AdapterRegistry:
    def __init__(self): self._adapters={x.framework_name:x() for x in (OpenAIAdapter,CrewAIAdapter,ClaudeCodeAdapter,LyzrAdapter)}
    def names(self): return sorted(self._adapters)
    def get(self,name): return self._adapters.get(name)
