from models.conversation_state import ConversationState
from engine.state_manager import StateManager

state = ConversationState()
manager = StateManager()

print(state)

manager.increase_trust(state, 20)
manager.increase_frustration(state, 15)
manager.next_turn(state)

print(state)