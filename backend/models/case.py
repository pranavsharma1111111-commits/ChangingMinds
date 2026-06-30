from dataclasses import dataclass, field


@dataclass
class Case:
    # Basic Information
    case_id: str
    title: str
    difficulty: str
    category: str

    # Mission
    mission_briefing: str
    scenario_context: str

    # Roles
    player_role: str
    character_role: str

    # Objectives
    player_objective: str
    character_objective: str

    # Rules
    constraints: list = field(default_factory=list)
    message_limit: int = 25

    # Conversation
    opening_dialogue: str = ""

    # Character
    character_file: str = ""

    # Win / Lose
    victory_condition: str = ""
    failure_conditions: list = field(default_factory=list)

    # Optional
    dynamic_events: list = field(default_factory=list)
    learning_objective: str = ""
    case_theme: str = ""

    # Metadata
    version: str = "1.0"
    status: str = "Draft"