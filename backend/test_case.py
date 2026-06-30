from models.case import Case

case1 = Case(
    case_id="CASE_001",
    title="The Homework Rebel",
    difficulty="Easy",
    category="Family",

    mission_briefing="Convince Alex to do his homework.",
    scenario_context="Alex has refused homework for a week.",

    player_role="Parent",
    character_role="Alex",

    player_objective="Get Alex to genuinely commit to homework.",
    character_objective="Avoid homework."
)

print(case1)