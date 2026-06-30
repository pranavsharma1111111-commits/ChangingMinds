from models.conversation_state import ConversationState


class StateManager:

    def increase_trust(self, state: ConversationState, amount: int):
        state.trust = min(100, state.trust + amount)

    def decrease_trust(self, state: ConversationState, amount: int):
        state.trust = max(0, state.trust - amount)

    def increase_frustration(self, state: ConversationState, amount: int):
        state.frustration = min(100, state.frustration + amount)

    def decrease_frustration(self, state: ConversationState, amount: int):
        state.frustration = max(0, state.frustration - amount)

    def next_turn(self, state: ConversationState):
        state.current_turn += 1

    def end_conversation(self, state: ConversationState):
        state.conversation_ended = True

    def complete_mission(self, state: ConversationState):
        state.mission_complete = True