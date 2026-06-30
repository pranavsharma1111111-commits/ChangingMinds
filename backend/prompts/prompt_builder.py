from models.character import Character
from models.case import Case
from models.conversation_state import ConversationState


class PromptBuilder:

    def build_prompt(
        self,
        character: Character,
        case: Case,
        state: ConversationState,
        player_message: str
    ):

        prompt = f"""
You are roleplaying as {character.name}.

=== CHARACTER ===
Name: {character.name}
Age: {character.age}
Role: {character.role}

Background:
{character.background}

Current Goal:
{character.current_goal}

Hidden Core Belief:
{character.hidden_core_belief}

=== CASE ===

Title:
{case.title}

Mission:
{case.mission_briefing}

=== CURRENT STATE ===

Trust: {state.trust}

Respect: {state.respect}

Frustration: {state.frustration}

Hope: {state.hope}

=== MEMORY ===

Conversation:
{state.conversation_history}

Promises:
{state.promises}

Discovered Facts:
{state.discovered_facts}

=== PLAYER MESSAGE ===

{player_message}
"""

        return prompt