from models.character import Character
from models.case import Case
from models.conversation_state import ConversationState
from prompts.prompt_builder import PromptBuilder

alex = Character(
    name="Alex",
    age=13,
    gender="Male",
    occupation="Student",
    role="Child",
    relationship="Son",
    background="Recently started hating school.",
    hidden_core_belief="I'm bad at school anyway.",
    current_goal="Avoid homework"
)

case = Case(
    case_id="CASE_001",
    title="The Homework Rebel",
    difficulty="Easy",
    category="Family",
    mission_briefing="Convince Alex to do homework.",
    scenario_context="",
    player_role="Parent",
    character_role="Alex",
    player_objective="Convince Alex",
    character_objective="Avoid homework"
)

state = ConversationState()

builder = PromptBuilder()

prompt = builder.build_prompt(
    alex,
    case,
    state,
    "Homework will help your future."
)

print(prompt)