from __future__ import annotations
from abc import ABC, abstractmethod
from core.agent_core import ConstructionProjectMonitoringAgent
class AgentAdapter(ABC):
    framework_name="framework-independent"
    @abstractmethod
    def invoke(self, agent:ConstructionProjectMonitoringAgent, tool:str, inputs:dict): ...
class OpenAIAdapter(AgentAdapter):
    framework_name="openai-sdk"
    def invoke(self,agent,tool,inputs): return agent.inspect(tool,inputs)
class CrewAIAdapter(AgentAdapter):
    framework_name="crewai"
    def invoke(self,agent,tool,inputs): return agent.inspect(tool,inputs)
class ClaudeCodeAdapter(AgentAdapter):
    framework_name="claude-code"
    def invoke(self,agent,tool,inputs): return agent.inspect(tool,inputs)
class LyzrAdapter(AgentAdapter):
    framework_name="lyzr"
    def invoke(self,agent,tool,inputs): return agent.inspect(tool,inputs)
